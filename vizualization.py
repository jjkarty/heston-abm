import matplotlib.pyplot as plt

def plot_price(price_history):
    plt.figure()
    plt.plot(price_history)
    plt.title("Price Evolution")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.grid()
    plt.show()

def plot_volatility(vol_history):
    plt.figure()
    plt.plot(vol_history)
    plt.title("Stochastic Volatility")
    plt.xlabel("Time")
    plt.ylabel("Variance")
    plt.grid()
    plt.show()

def plot_smile(strikes, option_prices, label=""):
    plt.figure()
    plt.plot(strikes, option_prices, marker="o", label=label)
    plt.title("Volatility Smile (Option Prices vs Strike)")
    plt.xlabel("Strike")
    plt.ylabel("Option Price")
    if label:
        plt.legend()
    plt.grid()
    plt.show()