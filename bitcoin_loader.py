import json
import requests
import time

def download_json(url):
    param = dict()
    resp = requests.get(url= url, params=param)
    data = resp.json()
    return data

def main():
    while True:
        json_file = download_json("http://api.coindesk.com/v1/bpi/currentprice.json")
        print(json_file["bpi"]["EUR"]["rate_float"])
        time.sleep(60)

if __name__ == '__main__':
    main()

