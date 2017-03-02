## all scripts which can be used to download any kind of porfolios from anywhere


import pandas as pd
pd.set_option('max_colwidth',4000)
#df = pd.read_csv('portfolio_links.csv')
#links = df['x']
link = "http://alphaideas.in/2016/11/17/portfolio-sundar-iyer/"
link = link.strip()
name = str(str(link).split("/")[-2]+'.csv')
mdf = pd.read_html(link)
table = mdf[0]
table.to_csv(name)

"""
def calc(link):
	try:
		link = link.strip()
		name = str(str(link).split("/")[-2]+'.csv')
		mdf = pd.read_html(link)
		table = mdf[0]
		table.to_csv(name)
	except:
		pass

"""

