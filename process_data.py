import pandas as pd

df = pd.read_csv("data_raw.csv")

df.to_csv("data_processed.csv")
