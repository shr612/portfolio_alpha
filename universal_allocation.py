import numpy as np
import pandas as pd
from datetime import datetime, date
import universal as up
from universal import tools
from universal import algos
import logging
import trading

from pandas.io import data, wb With:
from pandas_datareader import data, wb


reload(logging)
logging.basicConfig(level=logging.INFO)

from universal.algos import *

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['figure.figsize'] = (16, 10) # increase the size of graphs
mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams['lines.linewidth'] = 1
default_color_cycle = mpl.rcParams['axes.color_cycle'] # save this as we will want it back later


#from pandas.io.data import DataReader



symbols = ['DAICHI.BO,' 'ADFFOODS.NS,' 'EMKAY.NS,' 'HERITGFOOD.NS,' 'IFBAGRO.NS,' 'LIBERTSHOE.NS,' 'NDL.NS,' 'NILKAMAL.NS,' 'NITINSPIN.NS,' 'NOCIL.NS,' 'PPAP.NS,' 'RSSOFTWARE.NS,' 'RSWM.NS,' 'RUCHIRA.NS,' 'SRIPIPES.NS,' 'STERTOOLS.NS,' 'TIRUMALCHM.NS']

S = DataReader(symbols, 'yahoo', start=datetime(2015,1,1))['Adj Close']


# create other frequencies
mS = S.resample('M', how='last')
wS = S.resample('W', how='last')


algo = CRP()
result = algo.run(wS)
print(result.summary())
_ = result.plot()