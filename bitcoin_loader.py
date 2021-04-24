import json
import requests
import time

def download_json(url):
    param = dict()
    resp = requests.get(url= url, params=param)
    data = resp.json()
    return data

def main():
    json_file = download_json("http://api.coindesk.com/v1/bpi/currentprice.json")

    eur_code = str(json_file["bpi"]["EUR"]["code"]) + " "
    gbp_code = str(json_file["bpi"]["GBP"]["code"]) + " "
    usd_code = str(json_file["bpi"]["USD"]["code"]) + " "

    eur_description = "(" + str(json_file["bpi"]["EUR"]["description"]) + ")"
    gbp_description = "(" + str(json_file["bpi"]["GBP"]["description"]) + ")"
    usd_description = "(" + str(json_file["bpi"]["USD"]["description"]) + ")"


    while True:
        json_file = download_json("http://api.coindesk.com/v1/bpi/currentprice.json")
        print("1 bitcoin equals: ")

        eur_price = str(json_file["bpi"]["EUR"]["rate_float"]) + " € "
        gbp_price = str(json_file["bpi"]["GBP"]["rate_float"]) + " £ "
        usd_price = str(json_file["bpi"]["USD"]["rate_float"]) + " $ "

        print(eur_code + eur_price  + eur_description)
        print(gbp_code + gbp_price  + gbp_description)
        print(usd_code + usd_price  + usd_description + "\n")
        time.sleep(60)

if __name__ == '__main__':
    main()

