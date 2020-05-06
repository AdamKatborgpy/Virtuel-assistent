# Forskellige imports
import datetime as datetime
from datetime import date
import matplotlib.pyplot as pyplot
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web
import os
style.use('ggplot')

# Sæt ticker, til den ønskede aktie at følge. Skal stå inden for ''
#ticker = 'TRYG.CO'
ticker = str(input("Skriv aktiesymbolet på den foretrukne aktie: "))

# Ønskede filnavn, som bliver lagt på skrivebordet. Skal slutte på .csv og stå inden for ''
file_name = str(input("Navn paa fil: "))
os.chdir("desktop")
f = open(file_name, "w+")
f.close() 

# Valgte tidsramme fra start til end. Husk at ændre end datoen, hvis du bruger den i fremtiden :)
start = datetime.datetime(2000,1,1)
end = date.today()

# API request fra yahoo
df = web.DataReader(ticker, 'yahoo', start, end)
df.to_csv(file_name)
print(df.head(10))


df = pd.read_csv(file_name, parse_dates=True, index_col=0)

# Denne del er ikke nødvendig. Den visualiserer bare grafen. 
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

ax1 = pyplot.subplot2grid((6,1), (0,0), rowspan=5, colspan=1) 
ax2 = pyplot.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1) 

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

print(df.tail(10))
pyplot.show()