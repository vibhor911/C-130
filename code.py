import pandas as pd
import csv

df = pd.read_csv("data.csv")

del df["Luminosity"]
del df["star"]
del df["Unnamed: 6"]
del df["Mass.1"]
del df["Radius.1"]
del df["Distance.1"]

df.to_csv('clean.csv') 