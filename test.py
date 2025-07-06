from dotenv import load_dotenv
import os

load_dotenv()  # This must come BEFORE you use os.getenv!

db_host = os.getenv("POSTGRES_HOST", "localhost")  # fallback to 'localhost'
print(f"DB Host: {db_host}")  # for debugging, you can remove this later
