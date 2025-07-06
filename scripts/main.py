import pandas as pd

#loading csv
df = pd.read_csv("data/sales_data_sample.csv", encoding='latin1')

#cleaning by standardising date formart, handle missing sales as 0, and dropping duplicates
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors = "coerce")
df["SALES"] = df["SALES"].fillna(0)
df = df.drop_duplicates()
#filling missimg product lines with unknown
df["PRODUCTLINE"] = df["PRODUCTLINE"].fillna("Unknown")

#saving cleaned_data
df.to_csv("data/sales_data_clean.csv", index = False)

