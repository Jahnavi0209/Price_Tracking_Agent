import requests
from bs4 import BeautifulSoup
from utils import clean_price

def amazon_price(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }
    # import pdb; pdb.set_trace()
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,"lxml")
    price=soup.find("span",{"class":"a-price-whole"})

    if price:
        #  return clean_price(price.text)
        return {
            "ok": True,
            "price":clean_price(price.text)
        }
    return {"ok":False}

