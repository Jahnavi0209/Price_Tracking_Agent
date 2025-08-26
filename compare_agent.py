from typing import Tuple, Optional
from amazon_agent import amazon_price
from flipkart_agent import flipkart_price

def compare_prices(goal):
    prices={}
    if goal["amazon_url"]:
        price=amazon_price(goal["amazon_url"])
        if price:
            prices["amazon"]=price
    if goal["flipkart_url"]:
        price=flipkart_price(goal["flipkart_url"])
        if price:
            prices["flipkart"]=price
    if not prices:
        return None,{}

    best_site=min(prices)
    best_price=prices[best_site]
    return (best_site,best_price),prices
    
