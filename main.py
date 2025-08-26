from amazon_agent import amazon_price 
from flipkart_agent import flipkart_price
from config import Goals
from compare_agent import compare_prices

from notifier_agent import send_email
from apscheduler.schedulers.blocking import BlockingScheduler
 
def run():
    for goal in Goals:
       best,all_prices=compare_prices(goal)
       if not best: 
        print("could not fetch the price for"+goal[product])
       site,price=best
       if price<=goal["threshold"]:
        print(goal["product"]+" best price in site is "+ str(price)+" in "+site)
        subject= " "+goal["product"]+" at $"+str(price)+" "+site
        body=(
        "Gread news!"+"\n"+site+" at lower  "+str(price)+ " than "+str(goal["threshold"]))
        if goal["notify"]=="email":
            send_email(subject,body)


scheduler=BlockingScheduler()
@scheduler.scheduled_job("interval",seconds=60)
def job():
    run()
if __name__=="__main__":
    print("----starting----")
    scheduler.start()
   