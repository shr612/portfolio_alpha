# script to get name for number code
# example for TCS 
# For TCS : TCS.BO , 532540.BO

import requests
url = 'https://in.finance.yahoo.com/q?s={}.BO'.format(532454) #example for Bharti Airtel
pg = requests.get(url).text
print (pg.split("<title>")[1].split(": Summary")[0]).strip()

