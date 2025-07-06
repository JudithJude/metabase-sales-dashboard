import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_port = os.getenv("POSTGRES_PORT", "5433")
db_name = os.getenv("POSTGRES_DB")

print(f"Connecting to postgresql://{db_user}:****@{db_host}:{db_port}/{db_name}")

df = pd.read_csv("data/sales_data_clean.csv")

engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
)

df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Sales data uploaded successfully!")

















# import pandas as pd
# from sqlalchemy import create_engine
# from dotenv import load_dotenv
# import os


# #loading env variables from .env file
# load_dotenv()

# db_user = os.getenv("POSTGRES_USER")
# db_pass = os.getenv("POSTGRES_PASSWORD")
# db_host = os.getenv("POSTGRES_HOST", "localhost")
# db_port = 5432
# db_name = os.getenv("POSTGRES_DB")

# #reading the cleaned CSV
# df = pd.read_csv("data/sales_data_clean.csv")

# #creating SQLAlchemy engine
# engine = create_engine(
#     f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# )

# #uploading DataFrame to PostgreSQL (Creates or replaces "sales_data" table)
# df.to_sql("sales_data", engine, if_exists = "replace", index = False)

# print("Sales data uploaded successfully!")


# # Create SQLAlchemy engine
# engine = create_engine(
#     f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# )

# # Upload DataFrame to PostgreSQL (creates or replaces 'sales_data' table)
# df.to_sql('sales_data', engine, if_exists='replace', index=False)

# print("Data uploaded successfully! Your table is named 'sales_data'.")