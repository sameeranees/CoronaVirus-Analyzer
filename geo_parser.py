from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Firefox()
tots=None
sinds=None
puns=None
nws=None
bals=None
all_strings=[]

driver.get("https://www.geo.tv/latest/279045-coronavirus-updates-march-25-latest-news-on-the-coronavirus-pandemic-from-pakistan-and-around-the-world")
content = driver.page_source
soup = BeautifulSoup(content,features="html5lib")

for a in soup.findAll('span'):
    all_strings.append(a.get_text())

tots=all_strings[5].split()[-1]
sinds=all_strings[6].split()[-1]
puns=all_strings[7].split()[-1]
nws=all_strings[8].split()[-1]
bals=all_strings[9].split()[-1]

with open('document.csv','a') as fd:
    fd.write(tots.replace(',','')+','+sinds.replace(',','')+','+puns.replace(',','')+','+nws.replace(',','')+','+bals.replace(',','')+'\n')

driver.quit()

df=pd.read_csv("document.csv")

df.loc[-1] = [0,0,0,0,0]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index

ax = plt.gca()
plt.title("Cases in Pakistan")
plt.xlabel("Days")
plt.ylabel("Cases")
df.plot(kind='line',y='Total',ax=ax,marker='o')
df.plot(kind='line',y='Sindh',ax=ax,marker='o')
df.plot(kind='line',y='Punjab',ax=ax,marker='o')
df.plot(kind='line',y='NWFP',ax=ax,marker='o')
df.plot(kind='line',y='Balouchistan',ax=ax,marker='o')
fig = ax.get_figure()
fig.savefig('CoronaVirusGraph.png')
