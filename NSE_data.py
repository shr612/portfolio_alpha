import pandas as pd
import requests
pd.set_option('max_colwidth',4000)

symbol = 'CRISIL' # sample example
# get data for last 3 months
url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol={}&segmentLink=3&symbolCount=1&series=ALL&dateRange=3month&fromDate=&toDate=&dataType=PRICEVOLUME".format(symbol)
#print (url)
df = requests.get(url).text
tab =  pd.read_html(df)

print tab