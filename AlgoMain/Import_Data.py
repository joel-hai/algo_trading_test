import pandas_datareader as pdr
import datetime

def data_retrieval():
    aapl = pdr.get_data_yahoo('AAPL',
                              start=datetime.datetime(2014,1,1),
                              end=datetime.date.today())
    aapl['Date'] = aapl.index
    aapl.reset_index(drop=True, inplace=True)

    aapl = aapl[['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]
    #print(aapl.columns.to_list())

    aapl['Diff'] = aapl['Open'] - aapl['Close']
    aapl.drop(['Diff'], axis=1, inplace=True)

    #del aapl['Diff']

    return aapl

