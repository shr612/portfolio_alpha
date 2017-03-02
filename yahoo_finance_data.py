import requests
import pandas as pd
import io

# can be used  both for BSE and NSE data
# sample for a stock 
# note : does not work for numbers in BSE part :
# For TCS : TCS.BO , 532540.BO (will not work)

symbol = 'AMRUTANJAN'
url = "http://real-chart.finance.yahoo.com/table.csv?s={}.BO&a=00&b=2&c=1991&d=01&e=21&f=2017&g=d&ignore=.csv".format(symbol)
#df = requests.get(url).text
#print df

## to convert results to DataFrame


urlData = requests.get(url).content
df = pd.read_csv(io.StringIO(urlData.decode('utf-8')))

"""
#  output of df.info()

Data columns (total 7 columns):

Date         3685 non-null object
Open         3685 non-null float64
High         3685 non-null float64
Low          3685 non-null float64
Close        3685 non-null float64
Volume       3685 non-null int64
Adj Close    3685 non-null float64


"""