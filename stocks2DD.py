import random
import pprint
import sqlite3
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dateutil.parser import *
import numpy as np
from scipy.interpolate import spline
# from matplotlib import style

# style.use('fivethirtyeight')
global  IDS

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
conn = sqlite3.connect("C:\\New folder\\stock_1cczzzzzzzzzaa.db")
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unit INTEGER,  balance REAL, stockP REAL, stockO REAL)")

initialMoneyOwned = 1000.0
initialStocksOwned = 0.1
initialStockPrice = 10000.0
tradingDays = 10
tp = 5.0 # buy/sell percentage threshold of the investor
maxVolatilityPercent = 5.0 # of the stock
numTrials = 10


hold = 0
IDS = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

initialInvestment = initialMoneyOwned + initialStocksOwned * initialStockPrice

def SimulateTrading(moneyOwned, stocksOwned, stockPrice, days):
    stockBuySellPrice = stockPrice
    
    for day in range(days):
        volatility = random.random() * stockPrice * maxVolatilityPercent / 100.0 
        stockPrice += (random.random() * 2.0 - 1.0) * volatility
        
        # trading
        if stocksOwned > 0.0:
            if stockPrice >= stockBuySellPrice * (100.0 + tp) / 100.0:
                # sell
                moneyOwned += stocksOwned * stockPrice
                stocksOwned = 0.0
                stockBuySellPrice = stockPrice

        if moneyOwned > 0.0:
            if stockPrice <= stockBuySellPrice * (100.0 - tp) / 100.0:
                # buy
                stocksOwned += moneyOwned / stockPrice
                moneyOwned = 0.0
                stockBuySellPrice = stockPrice
    #print stocksOwned
    return (moneyOwned, stocksOwned, stockPrice)
    
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,
    
    

def animate(i):
    #print('---------') + str(numTrials)
    numTrials = 20
    numWins = 0
    numLosses = 1
    totalWins = 0.0
    totalLosses = 0.0
    # holds = c.execute('SELECT rowid FROM stuffToPlot')
    #IDS +=1
    #print IDS
    # c.execute('SELECT rowid FROM stuffToPlot ORDER BY rowid DESC LIMIT 1')
    # s9 = c.fetchone()
    # IDS = s9[0]
    for i in range(numTrials):
        #hold +=1
        #print str(numTrials)
        (moneyOwned, stocksOwned, stockPrice) = \
        SimulateTrading(initialMoneyOwned, initialStocksOwned, initialStockPrice, tradingDays)

        finalReturn = moneyOwned + stocksOwned * stockPrice - initialInvestment
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        #print stocksOwned
        #if moneyOwned > 0:
            #i = hold + i
        SO = stocksOwned *10000
            #print SO
            # print ('++++++++++++++')
        if finalReturn > 0.0:
            numWins += 1
            totalWins += finalReturn
        elif finalReturn < 0.0:
            numLosses += 1
            totalLosses += finalReturn			
			
        c.execute("INSERT INTO stuffToPlot (unit, balance,stockP,stockO) VALUES (?,?,?,?)", (totalLosses*10 ,moneyOwned,stockPrice, SO))
        conn.commit()
        

        
        # print "Stocks = " + str(stocksOwned) 
        # print "balance = " + str(moneyOwned)
        # print "Trading Days       = " + str(tradingDays) 
        # print "Number of Trials   = " + str(numTrials)
        # print "Number of Wins     = " + str(numWins)
        # #print "Average Win Amt    = " + str(totalWins / numWins)
        # print "Number of Losses   = " + str(numLosses)
        # print "Average Loss Amt   = " + str(abs(totalLosses / numLosses+1))
        # print "Stock Price  =  " + str(stockPrice)
        # print "Final Count  =  " + str(abs(finalReturn))
        # print i
        
    c.execute('SELECT unit, balance,stockP,stockO FROM stuffToPlot')
   
    #print d0[0]
    data = c.fetchall()
    # c.execute('SELECT rowid FROM stuffToPlot ORDER BY rowid DESC LIMIT 1')
    # s9 = c.fetchone()
    # IDS = s9[0]
    
    dates = []
    values = []
    stockp=[]
    stocko = []
    
    d = np.array([])
    v = np.array([])
    for row in data:
        dates.append(row[0])
        values.append(row[1])
        stockp.append(row[2])
        stocko.append(row[3])
        #print dates
        #d = np.append(d,row[0])
        
        #v =np.append(v,row[1])
    #plt.plot_date(dates,values)
    #s_dates = np.linspace (d.min() , d.max(), 300)
    #s_values = spline(d,v, s_dates)
#ax1.clear()
    ax1.clear()
    im = ax1.plot(dates,values,marker = 'o', linestyle = ':')
    im = ax1.plot(stockp, marker = 'o', linestyle = 'None', color = 'r')
    im = ax1.plot(stocko, marker = 'o', linestyle = 'None', color = 'y')

   #ax1.plot(s_dates,s_values)
    return im

# numWins = 0   
# numLosses = 1
s = 99
#ani = animation.FuncAnimation(fig,  animate,  interval = 1000, init_func = init, blit = True)    
ani = animation.FuncAnimation(fig,  animate,  interval = 100,)
#animate(1000)
plt.show()

c.close()
conn.close()
