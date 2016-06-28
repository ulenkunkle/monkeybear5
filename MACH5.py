import quandl
import math
import numpy as np
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import time

style.use('ggplot')

df = pd.read_csv('C:\\Python\\table(11).csv', index_col='Date', parse_dates=True)


df = df[['Open',  'High',  'Low',  'Close', 'Volume','Adj Close']]
df['HL_PCT'] = (df['High'] - df['Low']) / df['Adj Close'] * 100.0

df['PCT_change'] = (df['Adj Close'] - df['Open']) / df['Open'] * 100.0
df = df[['Adj Close', 'HL_PCT', 'PCT_change', 'Volume']]

#print df.head()

forecast_col = 'Adj Close'


df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.2 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.81)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan

last_date =  df.iloc[0].name    #datetime.datetime.now()                                  #df.iloc[-1].name
print '--------------------------'
print last_date
print confidence
last_unix = time.mktime(last_date.timetuple())

one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj Close'].plot()
df['Forecast'].plot()
plt.legend(loc=0)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()