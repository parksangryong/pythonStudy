from pydantic import BaseModel, Field

class StockInfoInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드(예: AAPL)")

class StockHistoryInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드(예: AAPL)")
    period: str = Field(..., title="기간", description="주식 데이터 조회 기간(예: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y ... 등)")

class StockRecommendationsInput(BaseModel):
    ticker: str = Field(..., title="주식 코드", description="주식 코드(예: AAPL)")