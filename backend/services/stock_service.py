import requests
import random
import datetime

FINNHUB_API_KEY = 'd0rk6n1r01qumepenvv0d0rk6n1r01qumepenvvg'
ALPHA_VANTAGE_KEY = 'FU569QGEIYR8YQ1X'

def get_stock_details(ticker):
    finnhub_url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={FINNHUB_API_KEY}"
    profile_url = f"https://finnhub.io/api/v1/stock/profile2?symbol={ticker}&token={FINNHUB_API_KEY}"

    quote = requests.get(finnhub_url).json()
    profile = requests.get(profile_url).json()

    return {
        "name": profile.get("name", ticker),
        "symbol": ticker,
        "currentPrice": quote.get("c"),
        "change": round(quote.get("c", 0) - quote.get("pc", 0), 2),
        "percentChange": round((quote.get("c", 0) - quote.get("pc", 0)) / quote.get("pc", 1) * 100, 2),
        "previousClose": quote.get("pc"),
        "avgVolume": random.uniform(5, 15),
        "peRatio": round(random.uniform(15, 30), 1),
        "exchange": profile.get("exchange", "NASDAQ"),
        "description": f"{profile.get('name', ticker)} is a company in {profile.get('finnhubIndustry', 'technology')}."
    }

def get_historical_data(ticker, timeframe):
    timeframes = {"1D": "60min", "1W": "60min", "1M": "daily", "6M": "daily"}
    interval = timeframes.get(timeframe.upper(), "daily")

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_{interval.upper()}&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}"
    res = requests.get(url).json()
    
    key = list(res.keys())[-1]
    values = res[key]
    
    return [{"date": date, "price": float(values[date]['4. close'])} for date in list(values.keys())[:30]]

def get_prediction_vs_reality(ticker):
    return [
        {"quarter": "Q1 2023", "prediction": 1.75, "reality": 1.60},
        {"quarter": "Q2 2023", "prediction": 2.10, "reality": 2.00},
        {"quarter": "Q3 2023", "prediction": 2.35, "reality": 2.40},
        {"quarter": "Q4 2023", "prediction": 2.05, "reality": 1.95}
    ]

def get_news(ticker):
    url = f"https://finnhub.io/api/v1/company-news?symbol={ticker}&from=2024-01-01&to=2025-01-01&token={FINNHUB_API_KEY}"
    news = requests.get(url).json()[:2]
    return [{"title": n["headline"], "summary": n["summary"]} for n in news]

def get_activity(ticker):
    return [
        {"user": "Alex Johnson", "action": "Bought 5 shares of ABC Inc.", "gain": 3.2},
        {"user": "Maria Garcia", "action": "Sold 10 shares of XYZ Corp.", "gain": -1.5},
        {"user": "Sam Lee", "action": "Bought 2 shares of DEF Ltd.", "gain": 0.8}
    ]
