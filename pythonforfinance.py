import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import bs4
import sklearn


style.use('ggplot')

start = dt.datetime.now() - dt.timedelta(days=5*365)
end = dt.datetime.now()

df = pd.read_csv('TSLA.csv',parse_dates=True, index_col=0)
df.plot()
plt.show()
