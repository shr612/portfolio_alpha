#!/usr/bin/python2.7

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import pandas as pd
from datetime import datetime, date
import universal as up
from universal import tools
from universal import algos
import logging
#import trading


reload(logging)
logging.basicConfig(level=logging.INFO)
pd.set_option('max_colwidth',4000)

from universal.algos import *
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['figure.figsize'] = (16, 10) # increase the size of graphs
mpl.rcParams['legend.fontsize'] = 5
mpl.rcParams['lines.linewidth'] = 1
default_color_cycle = mpl.rcParams['axes.color_cycle'] # save this as we will want it back later

from yahoo_nse_bse import symbols_from_file
from pandas.io.data import DataReader

# load assets
#symbols = symbols_from_file('portfolio-saif-advisors-india.csv')
symbols = ['AUROPHARMA.BO','APTECHT.BO','ANANTRAJ.BO','ATFL.BO','ADIEXRE.BO','A2ZINFRA.BO','AUTOIND.BO','BI.BO','CRISIL.BO','DBREALTY.BO','DELTACORP.BO', 'DHFL.BO', 'ESCORTS.BO', 'EDELWEISS.BO', 'FEDERALBNK.BO','FSL.BO', 'GEOJITBNPP.BO', 'GEOMETRIC.BO', 'HINDOILEXP.BO','HTMEDIA.BO', 'IONEXCHANG.BO', 'KARURVYSYA.BO','KESORAMIND.BO', 'LUPIN.BO', 'MBECL.BO', 'MCX.BO','NCC.BO','ORIENTCEM.BO','RDEL.BO','POLARIS.BO','PRAKASH.BO','PFOCUS.BO', 'PROZONINTU.NS','RALLIS.BO','RADICO.BO','SPICEJET.BO','TITAN.BO','TV18BRDCST.BO','VIPIND.BO','VICEROY.NS','JETAIRWAYS.BO','ADLABS.BO', 'ICICIPRULI.BO']
omitted_symbols = ['STERLINH.BO','TMRVL.BO',]

#print (symbols)

S = DataReader(symbols, 'yahoo', start=datetime(2016,1,1))['Adj Close']

# create other frequencies
#mS = S.resample('M', how='last')
#wS = S.resample('W', how='last')

mS = S.resample('M').last()
wS = S.resample('W').last()


## different methods and results

"""
algo = CRP()
result = algo.run(wS)
print(result.summary())
_ = result.plot()


"""
algo = DynamicCRP(n=52, min_history=8)
result = algo.run(wS)
print(result.summary())
_ = result.plot()

"""
algo = DynamicCRP(n=52, min_history=8, metric='sharpe', alpha=0.01)
result = algo.run(wS)
print(result.summary())
_ = result.plot(title='Using risk-aversion(alpha) parameter')

"""
"""
algo = DynamicCRP(n=52, min_history=8, metric='sharpe', no_cash=True)
result = algo.run(wS)
print(result.summary())
_ = result.plot(title='Using no cash constraint')
"""
"""
#algo = MPT(window=52, min_history=4, mu_estimator='historical', cov_estimator='empirical', method='mpt', q=0.)
algo = MPT(min_history=4, mu_estimator='historical', cov_estimator='empirical', method='mpt', q=0.05)
result = algo.run(wS)
print(result.summary())
_ = result.plot(title='Minimum-variance portfolio')

"""
