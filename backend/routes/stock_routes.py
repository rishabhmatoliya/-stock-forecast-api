from flask import Blueprint, request, jsonify
from backend.services.stock_service import get_stock_details, get_historical_data, get_prediction_vs_reality, get_news, get_activity

stock_routes = Blueprint('stock_routes', __name__)

@stock_routes.route('/api/stocks/<ticker>', methods=['GET'])
def stock_details(ticker):
    return jsonify(get_stock_details(ticker))

@stock_routes.route('/api/stocks/<ticker>/history', methods=['GET'])
def historical_prices(ticker):
    timeframe = request.args.get("timeframe", "1M")
    return jsonify(get_historical_data(ticker, timeframe))

@stock_routes.route('/api/stocks/<ticker>/prediction', methods=['GET'])
def prediction(ticker):
    return jsonify(get_prediction_vs_reality(ticker))

@stock_routes.route('/api/stocks/<ticker>/news', methods=['GET'])
def news(ticker):
    return jsonify(get_news(ticker))

@stock_routes.route('/api/stocks/<ticker>/activity', methods=['GET'])
def activity(ticker):
    return jsonify(get_activity(ticker))
