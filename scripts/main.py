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









# import pandas as pd

# #loading data
# df = pd.read_csv("sales_data_sample.csv")

# #cleaning data: dropping duplicates, handling nulls
# df.drop_duplicates(inplace = True)
# df.drop_duplicates(inplace=True)
# df.fillna({'Sales': 0, 'Quantity': 1}, inplace=True)  # Example fill

# # Standardize date format
# df['Date'] = pd.to_datetime(df['Date'])

# # Optional: standardize categories, strip spaces
# df['Category'] = df['Category'].str.strip().str.title()

# # Save cleaned data
# df.to_csv("sales_data_clean.csv", index=False)
