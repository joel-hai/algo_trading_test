import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def visu_1(upm):
    upm['Close'].plot(grid=True)
    #x = aapl['Date']
    #y = aapl['Close']
    #plt.plot(x,y)
    return plt.show()

def visu_2(daily_pct_change):

    daily_pct_change.hist(bins=150)
    return plt.show()

def visu_3(data, dailyclose):
    data.plot(figsize=(12, 8))
    dailyclose.plot()
    return plt.show()

def visu_4(data, dailyclose):
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time')
    ax1.set_ylabel('cum_return')
    ax1.plot(data, color = color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('pct_change')
    ax2.plot(dailyclose, color=color, linewidth=0.1)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    return plt.show()

def visu_5(all_data):
    def data(all_data):
        daily_close_px = all_data['Adj Close'].\
            reset_index().pivot('Date', 'Ticker', 'Adj Close')

        daily_pct_change=daily_close_px.pct_change()
        return daily_pct_change

    daily_pct_change = data(all_data)
    daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

    return plt.show()

def visu_6(daily_pct_change):
    pd.plotting.scatter_matrix(daily_pct_change, diagonal='kde', alpha = 0.1, figsize=(12,12))

    return plt.show()

def visu_7(aapl):
    aapl[['Adj Close', '42', '252']].plot()

    return plt.show()

def visu_8(all_data):
    daily_close_px = all_data['Adj Close']. \
        reset_index().pivot('Date', 'Ticker', 'Adj Close')

    daily_pct_change = daily_close_px.pct_change()

    min_periods = 75
    vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

    vol.plot(figsize=(10, 8))

    return plt.show()

def visu_9(aapl, signals):

    fig = plt.figure()

    ax1 = fig.add_subplot(111, ylabel ='price in dollars')
    aapl['Adj Close'].plot(ax=ax1, color = 'r', lw=2.)

    signals[['Short_Moving', 'Long_Moving']].plot(ax=ax1,lw=2.)

    ax1.plot(signals.loc[signals.positions == 1.0].index,
             signals.Short_Moving[signals.positions == 1.0],
             '^', markersize=10, color='m')

    ax1.plot(signals.loc[signals.positions == -1.0].index,
             signals.Short_Moving[signals.positions == -1.0],
             'v', markersize=10, color='k')
    return plt.show()

def visu_10(portfolio,signals):
    fig= plt.figure()
    ax1 = fig.add_subplot(111, ylabel='Portfolio value in Dollas')

    portfolio['total'].plot(ax=ax1, lw=2)
    ax1.plot(portfolio.loc[signals.positions == 1.0]
             .index,
             portfolio.total[signals.positions == 1.0],
             '^', markersize=10, color='m')
    ax1.plot(portfolio.loc[signals.positions == -1.0].index,
             portfolio.total[signals.positions == -1.0],
             'v', markersize=10, color='k')
    return plt.show()