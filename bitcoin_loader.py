import json
import requests
import time

from requests.api import get

def download_json(url):
    param = dict()
    resp = requests.get(url= url, params=param)
    data = resp.json()
    return data

def get_timezone_datetime(json_file, utc_offset):
    #edit time substring
    date_time = json_file["time"]["updated"].split(" ")
    time = date_time[3].split(":")
    hour = int(time[0])
    timezone_hour = hour + utc_offset
    timezone_time = str(timezone_hour) + ":" + time[1] + ":" + time[2]

    #add utc-offset to UTC
    timezone_utc = date_time[4] + "+" + str(utc_offset)

    #add the parts to the original string
    timezone_date_time = date_time[0] + " " + date_time[1] + " " + date_time[2] + " " + timezone_time + " " + timezone_utc
    print(timezone_date_time)

def main():
    json_file = download_json("http://api.coindesk.com/v1/bpi/currentprice.json")

    eur_code = str(json_file["bpi"]["EUR"]["code"]) + " "
    gbp_code = str(json_file["bpi"]["GBP"]["code"]) + " "
    usd_code = str(json_file["bpi"]["USD"]["code"]) + " "

    eur_description = "(" + str(json_file["bpi"]["EUR"]["description"]) + ")"
    gbp_description = "(" + str(json_file["bpi"]["GBP"]["description"]) + ")"
    usd_description = "(" + str(json_file["bpi"]["USD"]["description"]) + ")"

    print("------------------------------------------------------------")

    while True:
        json_file = download_json("http://api.coindesk.com/v1/bpi/currentprice.json")
        get_timezone_datetime(json_file, 2)
        print("1 bitcoin equals: ")

        eur_price = str(json_file["bpi"]["EUR"]["rate_float"]) + " € "
        gbp_price = str(json_file["bpi"]["GBP"]["rate_float"]) + " £ "
        usd_price = str(json_file["bpi"]["USD"]["rate_float"]) + " $ "

        print(eur_code + eur_price  + eur_description)
        print(gbp_code + gbp_price  + gbp_description)
        print(usd_code + usd_price  + usd_description)
        print("------------------------------------------------------------")
        time.sleep(60)

if __name__ == '__main__':
    main()

