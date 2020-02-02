import pandas_datareader as pdr
import datetime
import pandas as pd
import os
def data_retrieval():
    aapl = pdr.get_data_yahoo('AAPL',
                              start=datetime.datetime(2017,1,10),
                              end=datetime.datetime(2020,1,10))
    aapl['Date'] = aapl.index
    aapl.reset_index(drop=True, inplace=True)

    aapl = aapl[['Date', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]
    #print(aapl.columns.to_list())

    aapl['Diff'] = aapl['Open'] - aapl['Close']
    aapl.drop(['Diff'], axis=1, inplace=True)

    #del aapl['Diff']

    return aapl

def data_retrieve_BU():
    #print(os.getcwd())
    os.chdir('/Users/joelhaiko/Desktop/STOCKCSV/')
    dftest = pd.read_csv('allstocktest.csv')
    dftest = dftest[dftest['Ticker'] == 'UPM.HE']

    dftest['Diff'] = dftest.apply(lambda x: x['Open']
                                  / x['Close'], axis=1)

    return dftest


    #print(dftest['Ticker'].unique())

def retrive_multi():
    def get(tickers, startdate, enddate):
        def data(ticker):
            return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))

        datas = map(data, tickers)
        return (pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

    tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
    all_data = get(tickers, datetime.datetime(2006, 10, 1), datetime.datetime(2012, 1, 1))
    return all_data
