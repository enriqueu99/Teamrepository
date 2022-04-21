#Web-APP that identifies proper market entrances
import yfinance as yf



msft = yf.Ticker("MSFT")




def stock(ticker):
    share = yf.Ticker(ticker)
    #now a callable dictionary, need to look at ouput for keys 
    b = share.info
    
    
    return 'day high',b['dayHigh'],'52 week low',b['fiftyTwoWeekLow'],'regular market open',b['regularMarketOpen']
    

#modify ticker to change output
x = stock('AAPL')
zzz = stock('MSFT')
xxx = stock('TSLA')
nnn = stock('NFLX')


def convertlst(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
#Endpoint whereby the data has been converted 
z = convertlst(x)#AAPL
xx = convertlst(zzz)#MSFT


def stockanalysis(z):
    bb = z['day high']
    bb = int(bb) *45 
    return 

#print(stockanalysis(z))


#Testing output 
print(stock('AAPL'))
#succesfully converted list into dictionary 

#print(z)



