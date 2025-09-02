from langchain_core.tools import tool
from datetime import datetime
import pytz
import yfinance as yf
from . import tools_pydantic 


@tool
# 시간 출력 함수
def get_current_time(tz: str , location: str ) -> str:
    """
    현재 시간을 반환하는 함수

    Args:
        tz(str): 타임존(예 : Asia/Seoul). 실제 존재해야함
        location(str): 지역명, 타임존은 모든 지명에 대응하지 않으므로 이후 llm 답변 생성에 사용됨
    """
    tz = pytz.timezone(tz)
    now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    location_and_local_time = f"{location} 현지 시각 {now}"

    return location_and_local_time

@tool
# 종목 정보 가져오기 함수
def get_yf_stock_info(stock_info_input: tools_pydantic.StockInfoInput) -> str:
    """
    주식 종목의 정보를 조회하는 함수
    """
    stock = yf.Ticker(stock_info_input.ticker)
    info = stock.info
    return str(info)

@tool
# 최근 주가 기록 
def get_yf_stock_history(stock_history_input: tools_pydantic.StockHistoryInput) -> str:
    """
    주식 종목의 일정 기간의 정보를 조회하는 함수
    """
    stock = yf.Ticker(stock_history_input.ticker)
    history = stock.history(period = stock_history_input.period)
    history_md = history.to_markdown() # 데이터 프레임을 마크다운으로 변환
    return history_md
		
@tool
# 추천 정보
def get_yf_stock_recommendations(stock_recommendations_input: tools_pydantic.StockRecommendationsInput) -> str:
    """
    주식 종목의 추천 정보를 조회하는 함수
    """
    stock = yf.Ticker(stock_recommendations_input.ticker)
    recommendations = stock.recommendations
    recommendations_md = recommendations.to_markdown()
    return str(recommendations_md)