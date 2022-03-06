from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data_models import (
    Product,
    CanteenStaff,
    Customer,
    Admin, Transaction, Record
)

app = FastAPI()


# === TRUSTED HOSTS/REQUEST ORIGINS ===

origins = [
  'http://localhost:8080',
  'http://localhost:3000'
]


# === ADD MIDDLEWARE TO APPLICATION ===

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# === TESTING ===

@app.get('/')
def root():
    return {'message': 'Hello World'}


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


@app.get('/staff/{id}')
def get_staff_by_id(id: int) -> CanteenStaff:
    pass


@app.post('/staff/{id}')
def add_staff(id: int, staff: CanteenStaff) -> CanteenStaff:
    pass


@app.put('/staff/{id}')
def update_staff(id: int, updated_staff: CanteenStaff) -> CanteenStaff:
    pass


# === CUSTOMER ===

@app.get('/customer')
def get_all_customer() -> list[Customer]:
    pass


@app.get('/customer/{id}')
def get_customer_by_id(id: int) -> Customer:
    pass


@app.post('/customer/{id}')
def add_customer(id: int, customer: Customer) -> Customer:
    pass


@app.put('/customer/{id}')
def update_customer(id: int, updated_customer: Customer) -> Customer:
    pass


# === ADMIN ===

@app.get('/admin')
def get_all_admin() -> list[Admin]:
    pass


@app.get('/admin/{id}')
def get_admin_by_id(id: int) -> Admin:
    pass


@app.post('/admin/{id}')
def add_admin(id: int, admin: Customer) -> Admin:
    pass


@app.put('/admin/{id}')
def update_admin(id: int, updated_admin: Customer) -> Admin:
    pass


# === TRANSACTION ===

@app.get('/transaction')
def get_all_transaction() -> list[Transaction]:
    pass


@app.get('transaction/{id}')
def get_transaction_by_id(id: int) -> Transaction:
    pass


@app.post('transaction/{id}')
def add_transaction(id: int, transaction: Transaction) -> Transaction:
    pass


# === RECORD ===

@app.get('/record')
def get_all_record() -> list[Record]:
    pass


@app.get('record/{id}')
def get_record_by_id(id: int) -> Record:
    pass


@app.post('record/{id}')
def add_record(id: int, updated_record: Record) -> Record:
    pass
