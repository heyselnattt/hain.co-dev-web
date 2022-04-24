from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import OperationalError
from psycopg2.extras import RealDictCursor
from starlette import status
from starlette.exceptions import HTTPException

from data_models import (
    Product,
    Staff,
    Customer,
    Admin, Transaction, Record
)

from database.database_operation import DatabaseOperator
import database.database_operation as DB_STATIC
import database.create as db_controller

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

@app.get('/product',
         status_code=status.HTTP_200_OK)
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
                            product_description,
                            product_type,
                            product_is_active,
                            product_code
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


@app.get('/product/{product_code}')
def get_product_by_product_code(product_code: str):
    try:
        existing = False
        # check product if existing
        all_products = get_all_product()
        for record in all_products:
            # convert to a dictionary
            db_product = dict(record)
            if product_code == db_product['product_code']:
                existing = True
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Product does not exist.'
            )
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute(f"""SELECT 
                            product_id,
                            product_name,
                            product_price,
                            product_image_link,
                            product_stock,
                            product_description,
                            product_type,
                            product_is_active,
                            product_code
                            FROM hainco_product
                            WHERE product_code = '{product_code}'
                            """)
        product_record = cursor.fetchone()
        return product_record
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.post('/product/new_product')
def add_product(product: Product):
    try:
        code = product.product_code
        # check username if taken
        all_product = get_all_product()
        for record in all_product:
            # convert to a dictionary
            db_product = dict(record)
            if code == db_product['product_code']:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Username is already taken'
                )

        return {
            "data": db_controller.add_product_to_database(product),
            "detail": "Product added to database"
        }
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Invalid data format received'
        )


@app.put('/product/{id}')
def update_product(id: int, updated_product: Product) -> Product:
    pass


# === CANTEEN STAFF ===

@app.get('/staff',
         status_code=status.HTTP_200_OK)
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


@app.get('/staff/{username}',
         status_code=status.HTTP_200_OK)
def get_staff_by_username(username: str):
    try:
        existing = False
        # check username if existing
        all_staff = get_all_canteen_staff()
        for record in all_staff:
            # convert to a dictionary
            db_staff = dict(record)
            if username == db_staff['staff_username']:
                existing = True
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Username does not exist.'
            )
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute(f"""SELECT 
                            staff_id,
                            staff_full_name,
                            staff_contact_number,
                            staff_username,
                            staff_address,
                            staff_position,
                            staff_is_active
                            FROM hainco_staff
                            WHERE staff_username = '{username}'
                            """)
        staff_record = cursor.fetchone()
        return staff_record
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.post('/staff/{id}',
          status_code=status.HTTP_201_CREATED)
def add_staff(staff: Staff):
    try:
        username = staff.staff_username
        # check username if taken
        all_staff = get_all_canteen_staff()
        for record in all_staff:
            # convert to a dictionary
            db_staff = dict(record)
            if username == db_staff['staff_username']:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Username is already taken'
                )

        return {
            "data": db_controller.add_staff_to_database(staff),
            "detail": "Staff added to database"
        }
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Invalid data format received'
        )


@app.put('/staff/{id}',
         status_code=status.HTTP_200_OK)
def update_staff(id: int, updated_staff: Staff) -> Staff:
    pass


# === CUSTOMER ===

@app.get('/customer',
         status_code=status.HTTP_200_OK)
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


@app.get('/customer/{username}',
         status_code=status.HTTP_200_OK)
def get_customer_by_username(username: str):
    try:
        existing = False
        # check username if existing
        all_customers = get_all_customer()
        for record in all_customers:
            # convert to a dictionary
            db_customer = dict(record)
            if username == db_customer['customer_username']:
                existing = True
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Username does not exist.'
            )
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute(f"""SELECT 
                            customer_id,
                            customer_first_name,
                            customer_middle_name,
                            customer_last_name,
                            customer_username,
                            customer_email,
                            customer_contact_number,
                            customer_is_active
                            FROM hainco_customer
                            WHERE customer_username = '{username}'
                            """)
        customer_record = cursor.fetchone()
        return customer_record
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.post('/customer/new_customer',
          status_code=status.HTTP_201_CREATED)
def add_customer(customer: Customer):
    try:
        username = customer.customer_username
        # check username if taken
        all_customers = get_all_customer()
        for record in all_customers:
            # convert to a dictionary
            db_customer = dict(record)
            if username == db_customer['customer_username']:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Username is already taken'
                )

        return {
            "data": db_controller.add_customer_to_database(customer),
            "detail": "Customer added to database"
        }
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Invalid data format received'
        )


@app.put('/customer/{id}',
         status_code=status.HTTP_200_OK)
def update_customer(id: int, updated_customer: Customer) -> Customer:
    pass


# === ADMIN ===

@app.get('/admin',
         status_code=status.HTTP_200_OK)
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


@app.get('/admin/{username}',
         status_code=status.HTTP_200_OK)
def get_admin_by_username(username: str):
    try:
        # check username if existing
        all_admin = get_all_admin()
        for record in all_admin:
            # convert to a dictionary
            db_admin = dict(record)
            if username != db_admin['admin_username']:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Username does not exist.'
                )
        db = DatabaseOperator(cursor_factory=RealDictCursor)
        cursor = db.get_cursor()
        cursor.execute(f"""SELECT 
                        admin_id,
                        admin_full_name,
                        admin_username,
                        admin_position,
                        admin_is_active
                        FROM hainco_admin
                        WHERE admin_username = '{username}'
                        """)
        admin_record = cursor.fetchone()
        return admin_record
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


@app.post('/admin/new_admin',
          status_code=status.HTTP_201_CREATED)
def add_admin(admin: Admin):
    try:
        username = admin.admin_username
        # check username if taken
        all_admin = get_all_admin()
        for record in all_admin:
            # convert to a dictionary
            db_admin = dict(record)
            if username == db_admin['admin_username']:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Username is already taken'
                )

        return {
            "data": db_controller.add_admin_to_database(admin),
            "detail": "Admin added to database"
        }
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Invalid data format received'
        )


@app.put('/admin/update_admin',
         status_code=status.HTTP_200_OK)
def update_admin(username: str, updated_admin: Admin):
    pass


# === TRANSACTION ===

@app.get('/transaction',
         status_code=status.HTTP_200_OK)
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


@app.get('/transaction/{id}',
         status_code=status.HTTP_200_OK)
def get_transaction_by_id(id: int) -> Transaction:
    pass


@app.post('/transaction/{id}',
          status_code=status.HTTP_201_CREATED)
def add_transaction(id: int, transaction: Transaction) -> Transaction:
    pass


# === RECORD ===

@app.get('/record',
         status_code=status.HTTP_200_OK)
def get_all_record() -> list[Record]:
    pass


@app.get('/record/{id}')
def get_record_by_id(id: int) -> Record:
    pass


# TODO change the id variable to properly match the database rows
@app.post('/record/{id}')
def add_record(id: int, updated_record: Record) -> Record:
    pass


# === META ===

@app.get('/meta/row_count')
def get_row_count():
    try:
        return DB_STATIC.count_rows()
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Failed to connect to database'
        )


if __name__ == '__main__':
    print(get_admin_by_username('eluxify'))