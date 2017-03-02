import pandas as pd
pd.set_option('max_colwidth',4000)
df = pd.read_csv('portfolio_links.csv')
links = df['x']
for link in links:
	link = link.strip()
	name = str(str(link).split("/")[-2]+'.csv')
	mdf = pd.read_html(link)
	table = mdf[0]
	table.to_csv(name)