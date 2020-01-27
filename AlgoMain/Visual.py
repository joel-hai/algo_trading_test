import matplotlib.pyplot as plt

def visu_1(upm):
    upm['Close'].plot(grid=True)
    #x = aapl['Date']
    #y = aapl['Close']
    #plt.plot(x,y)
    return plt.show()