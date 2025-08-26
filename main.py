from amazon_agent import amazon_price 
from flipkart_agent import flipkart_price
from config import (amazon_url,flipkart_url,
CHECK_INTERVAL_MIN,TARGET_PRICE , PRODUCT_NAME, EMAIL_SUBJECT_PREFIX)
from compare_agent import compare_prices

from notifier_agent import send_email
from apscheduler.schedulers.blocking import BlockingScheduler
 
def run():
    # amazon_url="https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY?th=1"
    # flipkart_url="https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W"
    # import pdb; pdb.set_trace()
    # # price1=amazon_price(amazon_url)
    # price2=flipkart_price(flipkart_url)
    # print(price2)
    # import pdb; pdb.set_trace()
    app,price,a,f=compare_prices(amazon_url,flipkart_url)
    if price is not None and price<=TARGET_PRICE:
        subject= EMAIL_SUBJECT_PREFIX+" "+PRODUCT_NAME+" at $"+str(price)+" "+app
        body=(
            "Gread news!"+"\n"+PRODUCT_NAME+" is at lower than target on "+app+ " at $"+str(price)+"\n"   
        )
        send_email(subject,body)


scheduler=BlockingScheduler()
@scheduler.scheduled_job("interval",minutes=CHECK_INTERVAL_MIN)
def job():
    run()
if __name__=="__main__":
    print("----starting----")
    scheduler.start()