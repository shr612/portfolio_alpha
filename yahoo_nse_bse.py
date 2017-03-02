import pandas as pd
import requests
import numpy as np

def number_to_symbol(x):
        url = 'https://in.finance.yahoo.com/q?s={}.BO'.format(x)  # example for Bharti Airtel
        pg = requests.get(url).text
        return (pg.split("<title>")[1].split(": Summary")[0]).strip()

def symbols_from_file(x):
        df = pd.read_csv(x)
        sym = np.asarray(np.unique(df['1'][1:]))
        ticker = []
        for t in sym:
            if t[0] == '5' and len(str(t)) == 6:
                ## change number to name
                url = 'https://in.finance.yahoo.com/q?s={}.BO'.format(str(t))
                pg = requests.get(url).text
                z = (pg.split("<title>")[1].split(": Summary")[0]).strip()
                ticker.append(z)
            else:
                ticker.append(t + '.NS')
        return np.unique(np.asarray(ticker))




