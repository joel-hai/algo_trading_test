import matplotlib.pyplot as plt

def visu_1(upm):
    upm['Close'].plot(grid=True)
    #x = aapl['Date']
    #y = aapl['Close']
    #plt.plot(x,y)
    return plt.show()

def visu_2(daily_pct_change):

    daily_pct_change.hist(bins=50)
    return plt.show()
