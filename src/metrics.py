import numpy as np

def equity_curve(returns):
    return (1 + returns).cumprod()

def drawdown(equity):
    return equity / equity.cummax() - 1
