import requests
from bs4 import BeautifulSoup
from utils import clean_price

def flipkart_price(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"lxml")
    price=soup.find("div",{"class":"Nx9bqj CxhGGd"})
    
    if price:
        return {
            "ok": True,
            "price":clean_price(price.text)
            }
    return {"ok":False}

