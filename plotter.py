import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("document.csv")

df.loc[-1] = [0,0,0,0,0]  # adding a row
df.index = df.index + 1  # shifting index
df = df.sort_index()  # sorting by index

print(df)
ax = plt.gca()
plt.title("Cases in Pakistan")
plt.xlabel("Days")
plt.ylabel("Cases")
df.plot(kind='line',y='Total',ax=ax,marker='o')
df.plot(kind='line',y='Sindh',ax=ax,marker='o')
df.plot(kind='line',y='Punjab',ax=ax,marker='o')
df.plot(kind='line',y='NWFP',ax=ax,marker='o')
df.plot(kind='line',y='Balouchistan',ax=ax,marker='o')
plt.show()
fig = ax.get_figure()
fig.savefig('CoronaVirusGraph.png')
