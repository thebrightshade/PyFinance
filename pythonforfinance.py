import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import bs4
import sklearn


style.use('ggplot')

start = dt.datetime.now() - dt.timedelta(days=5*365)
end = dt.datetime.now()

# df = web.DataReader('TSLA', 'iex', start, end)
# df = web.DataReader('TSLA', 'morningstar', start, end)

df = pd.read_csv('TSLA.csv', parse_dates=True, index_col=0)
# df['100ma'] = df['close'].rolling(window=100, min_periods=0).mean()

df_ohlc = df['close'].resample('10D').ohlc()
df_volume = df['volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['date'] = df_ohlc['date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()

ax1.plot(df.index, df['close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['volume'])

plt.show()

df
