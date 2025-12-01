import os
import psycopg2
from dotenv import load_dotenv

# Load .env locally; in Vercel, env vars are injected automatically
load_dotenv()

def get_conn():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set")
    return psycopg2.connect(db_url)