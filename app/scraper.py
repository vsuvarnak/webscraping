import requests
from bs4 import BeautifulSoup

def scrape_amazon(product_name):
    url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
    response =requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    prices=[]
    for item in soup.find_all('span',{'class': 'a-price-whole'}):
        prices.append(item.text)

    return prices


def scrape_ebay(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    prices = []
    for item in soup.find_all('span', {'class': 's-item__price'}):
        prices.append(item.text)

    return prices


def scrape_flipkart(product_name):
    # Construct the search URL for Flipkart
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"

    # Define the headers with a user agent string
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    # Send an HTTP GET request to the URL
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to store the prices
    prices = []

    # Extract prices from the HTML
    for item in soup.find_all('div', {'class': '_30jeq3'}):
        prices.append(item.text)

    # Return the list of extracted prices
    return prices