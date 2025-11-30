from fastapi import FastAPI
from backend.employees import router as employee_router
from backend.products import router as product_router
from backend.sales import router as sales_router

app = FastAPI()
#=========================================================
@app.get('/')
def root():
    return {'Msg':'Hello From Root'}
#=========================================================


app.include_router(employee_router)
app.include_router(product_router)
app.include_router(sales_router)

