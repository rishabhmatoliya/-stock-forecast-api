from flask import Flask
from backend.routes.stock_routes import stock_routes
from backend.routes.trade_routes import trade_routes

app = Flask(__name__)

# Register blueprints
app.register_blueprint(stock_routes)
app.register_blueprint(trade_routes)

@app.route("/")
def home():
    return "Stock Predictor Backend is running!"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000), debug=True)
