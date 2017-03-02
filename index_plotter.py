import pandas as pd
import requests
import numpy as np
import io
import datetime
import matplotlib
import matplotlib.pyplot as plt


u = []
for date in dates:
	u.append(datetime.datetime.strptime(date, "%Y-%m-%d").date())

plt.plot(u,np.array(rawData['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price (INR) ')
plt.title("{}.BO".format(index))
plt.show()