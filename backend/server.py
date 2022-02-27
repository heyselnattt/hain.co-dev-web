from fastapi import FastAPI

from data_models import Product, CanteenStaff, Customer

app = FastAPI()


# === TESTING ===
@app.get('/')
def root():
    return {'message': 'Hello World'}


"""
Helpers
    get next id

Product
    get all - to display as cards
    get 1 - for record 
    post 1 - add record
    put 1 - update record
    
Canteen Staff
    get all - to display as cards
    get 1 - for record
    post 1 - add record
    put 1 - update record
    
Customer
    get all - for table
    get 1 - for record
    post 1 - add record
    put 1 - update record
    
Admin
    get all - to display as cards
    get 1 - for record
    post 1 - add record
    put 1 - update record
    
Transaction
    get all - for table
    get 1 - for record
    post 1 - add record
    put 1 - update record
    
Record
    get all - for table
    get 1 - for record
    post 1 - add record
    put 1 - update record
"""


# === HELPER FUNCTIONS ===
def get_max_id(table_name: str) -> int:
    pass


# === PRODUCT ===

@app.get('/product')
def get_all_product() -> list[Product]:
    pass


@app.get('/product/{id}')
def get_product_by_id(id: int) -> Product:
    pass


@app.post('/product/{id}')
def add_product(id: int, product: Product) -> Product:
    pass


@app.put('/product/{id}')
def update_product(id: int, updated_product: Product) -> Product:
    pass


# === CANTEEN STAFF ===

@app.get('/staff')
def get_all_canteen_staff() -> list[CanteenStaff]:
    pass


@app.get('staff/{id}')
def get_staff_by_id(id: int) -> CanteenStaff:
    pass


@app.post('staff/{id}')
def add_staff(id: int, staff: CanteenStaff) -> CanteenStaff:
    pass


@app.put('staff/{id}')
def update_staff(id: int, updated_staff: CanteenStaff) -> CanteenStaff:
    pass


# === CUSTOMER ===

@app.get('/customer')
def get_all_customer() -> list[Customer]:
    pass


@app.get('customer/{id}')
def get_customer_by_id(id: int) -> Customer:
    pass


@app.post('customer/{id}')
def add_customer(id: int, customer: Customer) -> Customer:
    pass


@app.put('customer/{id}')
def update_customer(id: int, updated_customer: Customer) -> Customer:
    pass
