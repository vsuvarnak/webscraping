import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

def scrape_amazon(product_name):
    url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.find_all('div', {'data-component-type': 's-search-result'}):
        product = {}
        title_element = item.find('span', {'class': 'a-size-medium'})
        if title_element:
            product['title'] = title_element.text.strip()

        price_element = item.find('span', {'class': 'a-price-whole'})
        if price_element:
            product['price'] = price_element.text.strip()

        image_element = item.find('img', {'class': 's-image'})
        if image_element:
            product['image'] = image_element['src']

        link_element = item.find('a', {'class': 'a-link-normal'})
        if link_element:
            product['url'] = 'https://www.amazon.in' + link_element['href']

        products.append(product)

    return products

def scrape_ebay(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name.replace(' ', '+')}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.find_all('div', {'class': 's-item__info'}):
        product = {}
        title_element = item.find('h3', {'class': 's-item__title'})
        if title_element:
            product['title'] = title_element.text.strip()

        price_element = item.find('span', {'class': 's-item__price'})
        if price_element:
            product['price'] = price_element.text.strip()

        image_element = item.find('img', {'class': 's-item__image-img'})
        if image_element:
            product['image'] = image_element['src']

        link_element = item.find('a', {'class': 's-item__link'})
        if link_element:
            product['url'] = link_element['href']

        products.append(product)

    return products

def scrape_flipkart(product_name):
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

    # req = Request
    # uClient = uReq(url)uuu
    # page_html = uClient.read()
    # uClient.close()
    # soup = BeautifulSoup(page_html, "html.parser")
    #
    # print(soup)

    products = []
    for item in soup.find_all('div', {'class': '_2kHMtA'}):
        product = {}
        title_element = item.find('a', {'class': 'IRpwTa'})
        if title_element:
            product['title'] = title_element.text.strip()

        price_element = item.find('div', {'class': '_30jeq3'})
        if price_element:
            product['price'] = price_element.text.strip()

        image_element = item.find('img', {'class': '_396cs4'})
        if image_element:
            product['image'] = image_element['src']

        link_element = item.find('a', {'class': '_2UzuFa'})
        if link_element:
            product['url'] = 'https://www.flipkart.com' + link_element['href']

        products.append(product)
    print(products)

    return products

