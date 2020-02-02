from AlgoMain import Import_Data as ID, Visual as VSL
import numpy as np
import pandas as pd
from AlgoMain import modelling as md

upm = ID.data_retrieve_BU()
aapl = ID.data_retrieval()

print(upm)
upm.set_index('Date', inplace = True, drop = False)
print(upm)
#print(VSL.visu_1(upm))
#daily_close = upm[['Date', 'Adj Close']]
daily_close = upm['Adj Close']
#daily_pct_change = daily_close['Adj Close'].pct_change()
daily_pct_change = daily_close.pct_change()
#daily_pct_change = daily_close['Adj Close'].astype('int') / daily_close['Adj Close'].astype('int').shift(1) - 1
daily_pct_change.fillna(0, inplace=True)
#daily_close = daily_close['daily_close_pct'].fillna(0, inplace = True)

#daily_log_returns = np.log(daily_close['Adj Close'].pct_change()+1)
daily_log_returns = np.log(daily_close.pct_change()+1)

#daily_close['Test'] = daily_close['Adj Close'] / daily_close['Adj Close'].shift(1)-1
cum_daily_return = (1 + daily_pct_change).cumprod()

#print(VSL.visu_4(cum_daily_return,daily_pct_change))

cum_daily_return.index = pd.to_datetime(cum_daily_return.index)
cum_monthly_return = cum_daily_return.resample("M").mean()

print(cum_monthly_return)
print(upm['Date'].max(), upm['Date'].min())
all_data = ID.retrive_multi()

#print(VSL.visu_5(all_data))
#print(VSL.visu_6(daily_pct_change))

adj_close_px = aapl['Adj Close']
moving_avg = adj_close_px.rolling(window=40).mean()
aapl['42'] = aapl['Adj Close'].rolling(window=42).mean()
aapl['252'] = aapl['Adj Close'].rolling(window=252).mean()

print(moving_avg[-10:])

#print(VSL.visu_7(aapl))
#print(VSL.visu_8(all_data))

print(md.model_1(all_data))

