import pandas as pd
import numpy as np
from AlgoMain import Import_Data as ID, Visual as VSL

aapl = aapl = ID.data_retrieval()
shorttime = 90

longtime= 250

signals = pd.DataFrame(index= aapl.index, columns=['signal'])
signals['signal'].fillna(0.0, inplace = True)
signals['Short_Moving'] = aapl['Adj Close'].rolling(window=shorttime, min_periods=1
                                                    ,center=False).mean()
signals['Long_Moving'] = aapl['Adj Close'].rolling(window=longtime, min_periods=1
                                                    ,center=False).mean()

#if [shorttime:] wasn't defined it would end up in false transactions as the value cannot be calculated
signals['signal'][shorttime:] = np.where(
    signals['Short_Moving'][shorttime:]
    >
    signals['Long_Moving'][shorttime:], 1.0, 0.0
)

#calculates the difference between the row and previous to it and if signal cahnges from 0 to 1 then positions
# column indicates a transaction 1 = buy, -1 sell
signals['positions'] = signals['signal'].diff()

print(signals.iloc[shorttime:])
#print(VSL.visu_9(aapl,signals))

initial_capital=10000

positions = pd.DataFrame(index=signals.index, columns=['AAPL']).fillna(0.0)
positions['AAPL'] = 100*signals['signal']

portfolio = positions.multiply(aapl['Adj Close'], axis= 0)
pos_diff= positions.diff()
print(portfolio.iloc[shorttime:])
print(pos_diff.iloc[shorttime:])
portfolio['holdings'] = (positions.multiply(aapl['Adj Close'], axis=0)).sum(axis=1)
portfolio['cash'] = initial_capital - (pos_diff.multiply(aapl['Adj Close'], axis=0)).sum(axis=1).cumsum()

portfolio['total'] = portfolio['cash'] + portfolio['holdings']
portfolio['returns'] = portfolio['total'].pct_change()

print(pos_diff['AAPL'].unique())
print(portfolio.iloc[shorttime:])