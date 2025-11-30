from fastapi import APIRouter
from utils import get_conn

router = APIRouter(tags=['Products'])

#================================================================================================
@router.get('/products')
def get_products():
    conn = get_conn()
    cur = conn.cursor()
    script = 'SELECT * FROM products;' 
    # value = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#================================================================================================