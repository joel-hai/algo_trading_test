from AlgoMain import Import_Data as ID, Visual as VSL
import numpy as np

upm = ID.data_retrieve_BU()
print(upm)
upm.set_index('Date', inplace = True, drop = False)
print(upm)
#print(VSL.visu_1(upm))
daily_close = upm[['Date', 'Adj Close']]
daily_pct_change = daily_close['Adj Close'].pct_change()
#daily_pct_change = daily_close['Adj Close'].astype('int') / daily_close['Adj Close'].astype('int').shift(1) - 1
daily_pct_change.fillna(0, inplace=True)
#daily_close = daily_close['daily_close_pct'].fillna(0, inplace = True)
print(daily_close)
daily_log_returns = np.log(daily_close['Adj Close'].pct_change()+1)

print(daily_close)
print(daily_pct_change)
#daily_close['Test'] = daily_close['Adj Close'] / daily_close['Adj Close'].shift(1)-1
print(VSL.visu_2(daily_pct_change))
cum_daily_return = (1 + daily_pct_change).cumprod()
print(cum_daily_return)
#print(daily_close)


