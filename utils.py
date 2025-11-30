import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    db_url = os.getenv('database_link')
    conn = psycopg2.connect(db_url,cursor_factory=RealDictCursor)
    return conn