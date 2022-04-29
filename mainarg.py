#Web-APP that identifies proper market entrances
#importing necesary resources 

import yfinance as yf
import matplotlib
import requests
import time
import urllib.request
import json
import pprint
import numpy as np

#WEATHER MAP API KEYS
api_key = '82e12f4da82605a5564356a9f44740d5'
msft = yf.Ticker("MSFT")






def stock(ticker):
    share = yf.Ticker(ticker)
    #now a callable dictionary, need to look at ouput for keys 
    b = share.info
    return 'day high',b['dayHigh'],'52 week low',b['fiftyTwoWeekLow'],'regular market open',b['regularMarketOpen']
    

def convertlst(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


def geo():
    #cities we want to extract weather data from
    #city_name1 = 'miami'
    #city_name2 = 'london'
    #city_name3 = 'sanfrancisco'
    #city_name4 = 'austin'
    #individual API calls for given city
    keys = {'miami','austin','london',}
    store = []
    pp = pprint.PrettyPrinter(indent=4)
    for i in keys:
        weburl = urllib.request.urlopen(f'http://api.openweathermap.org/geo/1.0/direct?q={i}&limit={5}&appid={api_key}')
        response = weburl.read().decode('utf-8')
        response2 = json.loads(response)
        
        a = response2[0]['lat']
        b = response2[0]['lon']
        #print(a)
        #print(b)
        c = {i:[a,b]}

        store.append(c)
        #pp.pprint(response2)
    
    #print(store)
    return store


def goodmood():

    pp = pprint.PrettyPrinter(indent=4)
    files = geo()
    v,b,n = files[0],files[1],files[2]

    key1, val = next(iter(v.items()))
    key2, val = next(iter(b.items()))
    key3, val = next(iter(n.items()))
    
    coordinates1 = files[0][key1]
    coordinates2 = files[1][key2]
    coordinates3 = files[2][key3]
    
    r1,r2 = coordinates1
    b1,b2 = coordinates2
    c1,c2 = coordinates3
    
    sourcelat = [r1,b1,c1]
    sourcelng = [r2,b2,c2]

    weather =[]

    sourcelist = [f'https://api.openweathermap.org/data/2.5/weather?lat={r1}&lon={r2}&appid={api_key}',
        f'https://api.openweathermap.org/data/2.5/weather?lat={b1}&lon={b2}&appid={api_key}',
        f'https://api.openweathermap.org/data/2.5/weather?lat={c1}&lon={c2}&appid={api_key}']

    for i in sourcelist:
        
       
        weburl2 = urllib.request.urlopen(i)
        response = weburl2.read().decode('utf-8')
        response2 = json.loads(response)
        z = response2['weather'][0]['description']
        print(z)
        weather.append(z)
        #pp.pprint(z)
        pp.pprint(response2['weather'][0]['description'])
    return weather




def coinbaseorderid():
    url = "https://api.exchange.coinbase.com/currencies"

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)
    return response.text

def coinbaseorder():
    url = "https://api.exchange.coinbase.com/orders"

    payload = {

    "profile_id": "hhh", 
    "type": "limit",
    "side": "buy",
    "stp": "dc",
    "stop": "loss",
    "time_in_force": "GTC",
    "cancel_after": "min",
    "post_only": "false",
    "product_id": "sol-usd",
    "stop_price": "98.76",
    "price": "98.54",
    "size": ".5"}
                
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"}
                                

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    


    #response : 200, ORDER SUCCESFUL 401, UNAUTHORIZED, 500, UNEXPECED ERROR

x = np.array([0,0,1],
             [0,0,1],
             [1,0,1],)   

   

    


    









    
x = stock('AAPL')
zzz = stock('MSFT')
xxx = stock('TSLA')
nnn = stock('NFLX')
z = convertlst(x)#AAPL
zz = convertlst(zzz)#MSFT
xx = convertlst(xxx)#TSLA
nn = convertlst(nnn)#NTFLX




if __name__ == '__main__':
    #geo()
    #print(goodmood())
    print(coinbaseorderid())




#TESTING TESTING TESTING TESTING

#print(z)
#print(stockanalysis(z))


#Testing output 
#print(stock('AAPL'))
#succesfully converted list into dictionary 

#print(z)



