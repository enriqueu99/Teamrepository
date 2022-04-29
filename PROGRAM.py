
import yfinance as yf
import matplotlib
import requests
import time
import urllib.request
import json
import pprint
import numpy as np
from mainarg import stock,convertlst,goodmood,sigmoid,sigmoidderivative,geo

api_key = '82e12f4da82605a5564356a9f44740d5'
msft = yf.Ticker("MSFT")
api_token = 3


x = stock('AAPL')
zzz = stock('MSFT')
xxx = stock('TSLA')
nnn = stock('NFLX')
z = convertlst(x)#AAPL
zz = convertlst(zzz)#MSFT
xx = convertlst(xxx)#TSLA
nn = convertlst(nnn)#NTFLX






x1 =  ((xx['regular market open']- xx['previousclose'])/xx['previousclose'])
if x1 > 0:
    x1 = 1
elif x1 <0:
    x1 = 0



z1 = goodmood()[0]
if z1 == 'clear sky' or 'scattered clouds' or 'few clouds':
    z1 = 1
else: z1 = 0

#addedbias
n1 = 0



m = 0
if xx['previousclose'] < xx['regularmarketprice']:
    m = 1
else: m=0

traininginputs = np.array([[x1,z1,n1]]          
                                    
                                    )

trainingoutputs = np.array([[m]]).T
   

np.random.seed(1)

synapticweights = 2* np.random.random((3,1))-1
print('random synaptic weights:')
print(synapticweights)


for iteration in range(100):
    inputlayer = traininginputs
    outputs = sigmoid(np.dot(inputlayer,synapticweights))
    error = trainingoutputs - outputs
    adjustment = error *sigmoidderivative(outputs)
    synapticweights += np.dot(inputlayer.T,adjustment)
    
print("outputs after training:")
print(outputs)

def buysell():
    if outputs > .6 :
        return 'buy'
    else: return 'sell'


decision = buysell()



    


