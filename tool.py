import yfinance as yf

def get_stocknews(ticker_symbol: str, period: str) -> list[dict[str, any]]:
    ticker = yf.Ticker(ticker_symbol)
    ticker.history(period=period)
    return ticker.get_news()