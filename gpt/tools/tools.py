from langchain_core.tools import tool
from datetime import datetime
import pytz
import yfinance as yf


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
def get_yf_stock_info(ticker: str) -> str:
    """
    종목 정보를 가져오는 함수

    Args:
        ticker(str): 종목 코드(예: AAPL)
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    return str(info)

@tool
# 최근 주가 기록 
def get_yf_stock_history(ticker: str, period: str) -> str:
    """
    최근 주가 기록을 가져오는 함수

    Args:
        ticker(str): 종목 코드(예: AAPL)
        period(str): 기간(예: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y ... 등)
    """
    stock = yf.Ticker(ticker)
    history = stock.history(period = period)
    history_md = history.to_markdown() # 데이터 프레임을 마크다운으로 변환
    return history_md
		
@tool
# 추천 정보
def get_yf_stock_recommendations(ticker: str) -> str:
    """
    추천 정보를 가져오는 함수

    Args:
        ticker(str): 종목 코드(예: AAPL)
    """
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations
    recommendations_md = recommendations.to_markdown()
    return str(recommendations_md)