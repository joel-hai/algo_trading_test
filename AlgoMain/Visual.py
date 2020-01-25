import matplotlib.pyplot as plt

def visu_1(aapl):
    aapl['Close'].plot(grid=True)
    x = aapl['Date']

    return plt.show()