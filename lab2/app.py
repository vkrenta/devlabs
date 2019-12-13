import requests
import time
from datetime import datetime
import ntplib

def get_time_if_url_not_work():
    c = ntplib.NTPClient()
    response = c.request('0.ua.pool.ntp.org', version=3)
    t = datetime.fromtimestamp(response.tx_time).time().strftime('%H:%M:%S %p')
    d = datetime.fromtimestamp(response.tx_time).date().strftime('%Y-%m-%d')
    date = {"date": d, "time": t}
    return date


def check_time(d):
    if "time" in d.keys():
        print("Time is: ", d['time'])
        home_work(d['time'])
    try:
        print("Date is: ", d['date'])
    except KeyError:
        print("No date in response!!!")
        raise KeyError
        
def main(url=''):
    if not url:
        print("No URL passed to function")
        return False

    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError

    if r:
        check_time(r.json())
    else:
        check_time(get_time_if_url_not_work())
    return True


def home_work(t):
    "DateTime Function"
    
    if "AM" in t:
        print("AM")
        return "am"
    elif "PM" in t:
        print("PM")
        return "pm"
    else:
        print("error")
        return 0

if __name__ == "__main__":
    a = "="*40
    print(a + "\nРезультат без параметрів: \n" + a + "\n")
    main()
    print(a + "\nРезультат з правильною URL: \n" + a + "\n")
    main('http://date.jsontest.com/')