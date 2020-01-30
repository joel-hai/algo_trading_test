from AlgoMain import Import_Data as ID, Visual as VSL
import numpy as np

upm = ID.data_retrieve_BU()
#aapl = ID.data_retrieval()
print(upm)
#print(VSL.visu_1(upm))
daily_close = upm[['Date', 'Adj Close']]
daily_close['daily_close_pct'] = daily_close['Adj Close'].pct_change()
daily_close['daily_close_pct'].fillna(0, inplace = True)

print(daily_close)

daily_close['daily_log_rtr'] = np.log(daily_close['Adj Close'].pct_change() +1)

print(daily_close)