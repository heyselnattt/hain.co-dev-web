from pydantic import BaseModel
from typing import Optional
import datetime as dt

# enum types
from enums.product_type import ProductType
from enums.record_interval import RecordInterval
from enums.transaction_type import TransactionType
from enums.work_position import CanteenPosition, AdminPosition


class Customer(BaseModel):
    customer_first_name: str
    customer_middle_name: Optional[str]
    customer_last_name: str
    customer_username: str
    customer_password: str
    customer_email: str
    customer_contact_number: str
    customer_is_active: bool


class Staff(BaseModel):
    staff_full_name: str
    staff_contact_number: str
    staff_username: str
    staff_password: str
    staff_address: str
    staff_position: CanteenPosition
    staff_is_active: bool


class Admin(BaseModel):
    admin_full_name: str
    admin_username: str
    admin_password: str
    admin_position: AdminPosition
    admin_is_active: bool


class Product(BaseModel):
    product_name: str
    product_price: float
    product_image_link: str
    product_stock: int
    product_description: str
    product_type: ProductType
    product_is_active: bool


class Transaction(BaseModel):
    transaction_agent: str
    transaction_description: str
    transaction_type: TransactionType
    transaction_amount: Optional[float]
    transaction_date: dt.datetime


class Record(BaseModel):
    record_interval: RecordInterval
