import pandas as pd

def compute_pivot_table(chunk):
    pivot = pd.pivot_table(chunk, index='artistname', columns='user', values='artist-value', aggfunc='sum', fill_value=0)
    return pivot
