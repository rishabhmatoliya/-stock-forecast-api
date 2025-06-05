from flask import Blueprint, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

stock_list_view = Blueprint("stock_list_view", __name__, url_prefix="/api/stocklist")

@stock_list_view.route("/stocks", methods=["GET"])
def get_stocks():
    try:
        FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
        url = f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token={FINNHUB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        # Make sure 'data' is a list
        if not isinstance(data, list):
            return jsonify({"error": "Unexpected response format from API"}), 500

        stocks = [
            {
                "symbol": item.get("symbol", ""),
                "name": item.get("description", "")
            }
            for item in data[:20]
        ]

        return jsonify(stocks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
