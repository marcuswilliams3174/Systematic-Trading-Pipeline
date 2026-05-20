import numpy as np

def generate_signal(df):
    signal = df["signal"].fillna(0)
    return signal
