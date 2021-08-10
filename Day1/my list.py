#!/usr/bin/env python3
import pandas as pd
f = open("trade2.txt", "w+")

df1 = pd.DataFrame({
    "date": [8092021, 8102021, 8112021],
    "price": [7.12, 8.52, 2.35]
    })
df2 = pd.DataFrame({
    "date": [8122021, 8132021, 8142021],
    "price": [2.3, 11.25, 5.11]
    })

df3 = pd.DataFrame({
    "date": [8132021, 8142021, 8152021],
    "price": [1.22, 6.25, 10.57]
    })
df1.to_csv(f, mode='a', sep='\t')
f.close
trade = [df1, df2, df3]
length = len(trade)

f = open("trade2.txt", "a")
for i in range(length):
    if i > 0: trade[i].to_csv(f, header=None, mode='a', sep='\t')


