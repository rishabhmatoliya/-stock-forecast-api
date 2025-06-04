from flask import Blueprint, request, jsonify
from backend.services.trade_service import handle_trade

trade_routes = Blueprint("trade_routes", __name__)

@trade_routes.route("/api/trade", methods=["POST"])
def trade():
    try:
        data = request.get_json()

        user = data.get("user")
        action = data.get("action")  # "buy" or "sell"
        ticker = data.get("ticker")
        shares = int(data.get("shares"))

        if not all([user, action, ticker, shares]):
            return jsonify({"error": "Missing required fields"}), 400

        result = handle_trade(user, action, ticker, shares)
        return jsonify(result)

    except Exception as e:
        print("Error in trade route:", e)
        return jsonify({"error": "Internal server error"}), 500
