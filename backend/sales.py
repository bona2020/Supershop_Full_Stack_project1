from fastapi import APIRouter
from utils import get_conn

router = APIRouter(tags= ['Sales'])

#=====================================================
#1. GET ALL SALES:
@router.get('/get_sales')
def get_sales():
    conn = get_conn()
    cur = conn.cursor()
    script = 'SELECT * FROM sales;'
    # value = ''
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#=====================================================
