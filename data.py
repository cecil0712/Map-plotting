# 6/2/2024 19:09
import requests
from decimal import Decimal
# from urllib import parse  ~parse.quote

def get_data(addr,key):
    url = f"https://restapi.amap.com/v3/geocode/geo?address={(addr)}&output=JSON&key={key}"  # GaoDe api
    print(url)
    req = requests.get(url)  # request the data
    req = req.json()  # encode with json
    print(req)
    m = req["geocodes"]["0"]["location"].split(',') #get the latitude and longitude value and seperate them by ','
    la,lo=Decimal(m[0]),Decimal(m[1])
    print(la,lo)
    return la,lo

# get_data("杭州市西湖",'JACBZ-2DY6L-DEOPD-M4XTS-RYTGF-EJB6D')