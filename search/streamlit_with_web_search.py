from langchain_core.tools import tool
from datetime import datetime
import pytz

# 웹 검색
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
# 유튜브 검색
from youtube_search import YoutubeSearch
from langchain_community.document_loaders import YoutubeLoader
from typing import List

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 모델 초기화
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

@tool
def get_current_time(timezone: str, location: str) -> str:
    """현재 시간을 반환하는 함수"""
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        result = f"{timezone} ({location} 현지 시각 {now})"
        print(result)
        return result
    except pytz.UnknownTimeZoneError as e:
        return f"알 수 없는 타임존: {timezone}"


@tool
def get_web_search(query: str, search_period: str) -> str:
    """
    웹 검색을 수행하는 함수

    Args: 
        query(str): 검색 질문
        search_period(str): 검색 기간(예: "w" for past week, "m" for past month, "y" for past year)

    Returns:
        str: 검색 결과
    """
    wrapper = DuckDuckGoSearchAPIWrapper(region="kr-kr", time=search_period)
    print("---------- WEB SEARCH ----------")
    print(query)
    print(search_period)
    search = DuckDuckGoSearchResults(results_separator=";\n", api_wrapper=wrapper)
    docs = search.invoke(query)
    return docs

@tool
def get_youtube_search(query: str) -> List:
    """
    유튜브 검색한 뒤, 영상들의 내용을 반환하는 함수

    Args:
        query(str): 검색 질문

    Returns:
        List: 검색 결과
    """
    print("---------- YOUTUBE SEARCH ----------")
    print(query)
    videos = YoutubeSearch(query, max_results=5).to_dict()

    videos = [video for video in videos if len(video["duration"]) < 5]

    for video in videos:
        video['video_url'] = ("https://www.youtube.com" + video["url_suffix"])
        loader = YoutubeLoader.from_youtube_url(video['video_url'], language=["en", "ko"], add_video_info=True)
        video['content'] = loader.load()
    return videos

tools = [get_current_time, get_web_search, get_youtube_search]
tool_dict = {
    "get_current_time": get_current_time,
    "get_web_search": get_web_search,
    "get_youtube_search": get_youtube_search
}

llm_with_tools = llm.bind_tools(tools)

messages = [
    SystemMessage(content="너는 사용자의 질문에 답변을 하기 위해 tools를 사용할 수 있다."),
    HumanMessage(content="부산에 요즘 많이 뜨는 기사가 뭐야?")
]

response = llm_with_tools.invoke(messages)
print(response)