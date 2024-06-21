from flask import jsonify, request, render_template
from app import app
from app.scraper import  scrape_flipkart ,scrape_ebay, scrape_amazon


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prices', methods=['GET'])
def get_prices():
    product_name = request.args.get('product_name')
    amazon_products = scrape_amazon(product_name)
    ebay_products = scrape_ebay(product_name)
    flipkart_products = scrape_flipkart(product_name)

    products = []

    for product in amazon_products:
        product['site'] = 'Amazon'
        products.append(product)

    for product in ebay_products:
        product['site'] = 'eBay'
        products.append(product)

    for product in flipkart_products:
        product['site'] = 'Flipkart'
        products.append(product)

    return jsonify(products)
