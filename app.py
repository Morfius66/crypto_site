from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.coingecko.com/api/v3"

def fetch_crypto_data():
    """Получает данные топ-250 монет."""
    params = {
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 250,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(f"{API_URL}/coins/markets", params=params)
    response.raise_for_status()
    return response.json()

def fetch_coin_details(coin_id):
    """Получает детальную информацию о монете."""
    response = requests.get(f"{API_URL}/coins/{coin_id}")
    response.raise_for_status()
    return response.json()

@app.route('/')
def index():
    crypto_data = fetch_crypto_data()
    return render_template('index.html', crypto_data=crypto_data)

@app.route('/coin/<coin_id>')
def coin_details(coin_id):
    coin_data = fetch_coin_details(coin_id)
    return render_template('coin.html', coin=coin_data)

if __name__ == '__main__':
    app.run(debug=True)
