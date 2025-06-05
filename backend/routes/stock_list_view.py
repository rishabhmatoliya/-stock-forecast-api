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
        url = f"https://finnhub.io/api/v1/stock/symbol?exchange=US&token=d0rk6n1r01qumepenvv0d0rk6n1r01qumepenvvg"
        response = requests.get(url)
        data = response.json()

        # DEBUG PRINT - Check what API returned
        print("Finnhub response:", data)

        # Handle API errors
        if isinstance(data, dict) and ("error" in data or "message" in data):
            return jsonify({"error": "Finnhub API error", "details": data}), 500

        if not isinstance(data, list):
            return jsonify({"error": "Unexpected response format", "raw": data}), 500

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
