import statsmodels.api as sm
import numpy as np
import pandas as pd
#from pandas import datetools

def model_1(all_data):
    all_adj_close = all_data['Adj Close']

    all_returns = np.log(all_adj_close/all_adj_close.shift(1))
    aapl_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') =='AAPL']
    aapl_returns.index = aapl_returns.index.droplevel('Ticker')

    msft_returns = all_returns.iloc[all_returns.index.get_level_values('Ticker') =='MSFT']
    msft_returns.index = msft_returns.index.droplevel('Ticker')

    return_data = pd.concat([aapl_returns,msft_returns], axis=1)[1:]
    return_data.columns = ['AAPL', 'MSFT']

    X = sm.add_constant(return_data['AAPL'])
    model = sm.OLS(return_data['MSFT'], X).fit()

    return model.summary()
