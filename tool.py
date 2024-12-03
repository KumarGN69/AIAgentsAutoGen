import yfinance as yf
from pprint import pprint

def get_news(ticker_symbol:str,period:str) -> list[dict[str, any]] :
    """Get mkt news of the ticker"""
    pprint("Entered the get news function")
    ticker =yf.Ticker(ticker_symbol)
    ticker.history(period=period)
    return ticker.get_news()

# pprint(get_news("TSLA",period="5d"))
