from fastapi import APIRouter
from backend.utils import get_conn


router = APIRouter(tags=['employees'])


#========================================================
# 1 GET ALL EMPLOYEES:
@router.get('/employees')
def get_employees():
    conn= get_conn()
    cur = conn.cursor()
    script = 'SELECT * FROM  employees;'
    # vaule = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#-----------------------------------------------------------
# 2 GET EMPLOYEES BY ID:
@router.get('/employees/{employee_id}')
def get_employee(employee_id):
    conn= get_conn()
    cur = conn.cursor()
    script = 'SELECT * FROM  employees;'
    # vaule = 
    cur.execute(script)
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#============================================================================
# 3 CREATE AN  EMPLOYEE:
@router.post('/create_employee')
def create_employee(employee_id,name,position,region):
    conn= get_conn()
    cur = conn.cursor()
    script = 'INSERT INTO employees (%s,%s,%s,%s) RETURNING employee_id,name,position,region;'
    value = (employee_id,name,position,region)
    cur.execute(script,value)
    conn.commit()
    update = cur.fetchall()
    cur.close()
    conn.close()
    return update
#============================================================================
