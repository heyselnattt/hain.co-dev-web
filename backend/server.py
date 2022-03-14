import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor, NamedTupleCursor
from starlette import status
from starlette.exceptions import HTTPException

from database.database_operation import DatabaseOperator

from data_models import (
    Product,
    Staff,
    Customer,
    Admin, Transaction, Record
)

app = FastAPI(
    title='Hain.co Web API',
    version='0.0.1',
    contact={
        'name': 'Clarence Rhey Salaveria',
        'email': 'clarencerhey.edu@gmail.com'
    }
)


# === TRUSTED HOSTS/REQUEST ORIGINS ===

origins = [
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


# === PRODUCT ===

@app.get('/product')
def get_all_product() -> list[Product]:
    try:
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute("""SELECT 
                            product_id,
                            product_name,
                            product_price,
                            product_image_link,
                            product_stock,
                            product_type,
                            product_is_active
                            FROM hainco_product""")
        all_product = cursor.fetchall()
        if not all_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No products exist'
            )
        return all_product
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


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
def get_all_canteen_staff() -> list[Staff]:
    try:
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute("""SELECT 
                            staff_id,
                            staff_full_name,
                            staff_contact_number,
                            staff_username,
                            staff_address,
                            staff_position,
                            staff_is_active
                            FROM hainco_staff""")
        all_staff = cursor.fetchall()
        if not all_staff:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No staff records exist'
            )
        return all_staff
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.get('/staff/{id}')
def get_staff_by_id(id: int) -> Staff:
    pass


@app.post('/staff/{id}')
def add_staff(id: int, staff: Staff) -> Staff:
    pass


@app.put('/staff/{id}')
def update_staff(id: int, updated_staff: Staff) -> Staff:
    pass


# === CUSTOMER ===

@app.get('/customer')
def get_all_customer() -> list[Customer]:
    try:
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute("""SELECT 
                            customer_id,
                            customer_first_name,
                            customer_middle_name,
                            customer_last_name,
                            customer_username,
                            customer_email,
                            customer_contact_number,
                            customer_is_active
                            FROM hainco_customer""")
        all_customer = cursor.fetchall()
        if not all_customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No customer records exist'
            )
        return all_customer
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


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
def get_all_admin():
    try:
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute("""SELECT 
                        admin_id,
                        admin_full_name,
                        admin_username,
                        admin_position,
                        admin_is_active
                        FROM hainco_admin""")
        all_admin = cursor.fetchall()
        if not all_admin:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No admin records found'
            )
        return all_admin
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.get('/admin/{username}')
def get_admin_by_username(username: str):
    pass


@app.post('/admin/new_admin')
def add_admin(admin: Admin):
    pass


@app.put('/admin/update_admin')
def update_admin(username: str, updated_admin: Admin) -> Admin:
    pass


# === TRANSACTION ===

@app.get('/transaction')
def get_all_transaction() -> list[Transaction]:
    try:
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute("""SELECT 
                        transaction_id,
                        transaction_agent,
                        transaction_description,
                        transaction_type,
                        transaction_amount,
                        transaction_date
                        FROM hainco_transaction""")
        all_transaction = cursor.fetchall()
        if not all_transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='No transactions found'
            )
        return all_transaction
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


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
