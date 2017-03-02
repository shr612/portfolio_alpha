import pandas as pd
import numpy as np
import requests, io

## objective to make a portfolio based on equal weights

## importting a sample portfolio
df = pd.read_csv('portfolio-dolly-khanna.csv')
symbols = np.unique(np.array(df['1'][1:]))

## selecting if symbol belongs to bse or nse 
ticker = []
for t in symbols:
    if t[0] == '5' and len(str(t)) == 6:
        ## change number to name
        url = 'https://in.finance.yahoo.com/q?s={}.BO'.format(str(t))
        pg = requests.get(url).text
        z = (pg.split("<title>")[1].split(": Summary")[0]).strip()
        ticker.append(z)

    else:
        ticker.append(t + '.NS')

    ## assigning weights
wx = np.ones(len(ticker)) * 1.0 / len(ticker)


# print wx

## defining function to calculate returns
def calc_returns(prices):
    r = []
    for i in range(len(prices) - 1):
        t = (prices[i + 1] - prices[i]) / prices[i]
        r.append(t)
    return np.mean(r)


## downloading data from yahoo finance -- last 1 year + calculating returns
rf = 0.03  # risk free rate
rp = []
for x in ticker:
    url = "http://real-chart.finance.yahoo.com/table.csv?s={}&a=00&b=2&c=2016&d=01&e=21&f=2017&g=d&ignore=.csv".format(
        x)
    #	print url
    urlData = requests.get(url).content
    df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    # print len(df['Close'])
    rp.append(calc_returns(np.array(df['Close'])))

# displaying ticker vs returns
print(pd.DataFrame({'ticker_symbol': ticker, 'returns': rp}))

## calculating sharpe's ratio
print("Sharpe's Ratio :", (np.mean(rp) - rf) / np.std(rp))
# think I am making a mistake -- value should not be so low
