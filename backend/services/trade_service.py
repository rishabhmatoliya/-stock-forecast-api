user_portfolios = {}

def record_trade(data):
    username = data.get("username")
    action = data.get("action")
    ticker = data.get("ticker")
    shares = data.get("shares")
    price = data.get("price")

    if username not in user_portfolios:
        user_portfolios[username] = {
            "trades": [],
            "buying_power": 10000
        }

    user = user_portfolios[username]

    cost = price * shares if action == "buy" else -price * shares
    user["buying_power"] -= cost
    user["trades"].append({"ticker": ticker, "shares": shares, "action": action, "price": price})

    return {"message": "Trade recorded", "buying_power": user["buying_power"]}

def get_user_portfolio(username):
    return user_portfolios.get(username, {"buying_power": 10000, "trades": []})

def handle_trade(user, action, ticker, shares):
    # Mocked logic — replace with DB logic later
    print(f"{user} performed {action} of {shares} shares of {ticker}")
    
    # Example: determine gain/loss dummy
    import random
    change = round(random.uniform(-5, 5), 2)
    result = {
        "user": user,
        "ticker": ticker,
        "action": action,
        "shares": shares,
        "change_percent": f"{change}%",
        "status": "success"
    }
    return result
