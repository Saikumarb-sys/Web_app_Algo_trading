def iron_condor(spot):
    return {
        "SELL_CE": spot + 100,
        "BUY_CE": spot + 200,
        "SELL_PE": spot - 100,
        "BUY_PE": spot - 200
    }
