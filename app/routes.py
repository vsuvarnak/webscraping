from flask import Flask, jsonify, request, render_template
from app import app
from app.models import Price, session
from app.scraper import scrape_ebay, scrape_amazon,scrape_flipkart

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prices',methods= ['GET'])
def get_prices():
    product_name = request.args.get('product_name')
    amazon_prices =scrape_amazon(product_name)
    ebay_prices= scrape_ebay(product_name)
    flipkart_prices= scrape_flipkart(product_name)

    prices = []
    for price in amazon_prices:
        prices.append({'site': 'Amazon', 'price': price})
    for price in ebay_prices:
        prices.append({'site': 'eBay', 'price': price})
    for price in flipkart_prices:
        prices.append({'site': 'Flipkart', 'price': price})

    return jsonify(prices)