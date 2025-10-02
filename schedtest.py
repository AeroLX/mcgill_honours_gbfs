import schedule
import time
from os import makedirs

makedirs('logs', exist_ok=True)

with open (f"logs/log_mtl.txt", "a") as f:
    f.write("Montreal BIXI GBFS data:")
    f.close()
    
with open (f"logs/log_ham.txt", "a") as f:
    f.write("Hamburg StadtRAD GBFS data:")
    f.close()
    
def job():
    print("I'm working...")
    with open (f"logs/log_mtl.txt", "a") as f:
        f.write("Montreal BIXI GBFS data:")
        f.close()
    with open (f"logs/log_ham.txt", "a") as f:
        f.write("Hamburg StadtRAD GBFS data:")
        f.close()

def pulldata():
    schedule.every(15).minutes.until("23:59").do(job)
    return()

#schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

def dailyroutine():
    schedule.every().day.at("5:59").do(pulldata)

dailyroutine()

while 1:
    schedule.run_pending()
    time.sleep(1)