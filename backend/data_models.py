from pydantic import BaseModel, SecretStr, AnyUrl
from typing import Optional, Union
import datetime as dt

# enum types
from enums.product_type import ProductType
from enums.record_interval import RecordInterval
from enums.transaction_type import TransactionType
from enums.work_position import CanteenPosition, AdminPosition

# done
class Customer(BaseModel):
    customer_id: int
    customer_first_name: str
    customer_middle_name: Optional[str]
    customer_last_name: str
    customer_contact_number: str
    customer_username: str
    customer_password: SecretStr
    customer_email: str
    customer_is_active: bool

# done
class CanteenStaff(BaseModel):
    staff_id: int
    staff_full_name: str
    staff_contact_number: str
    staff_username: str
    staff_password: SecretStr
    staff_address: str
    staff_position: CanteenPosition  # done table
    staff_is_active: bool

# done
class Admin(BaseModel):
    admin_id: int
    admin_full_name: str
    admin_username: str
    admin_password: SecretStr
    admin_position: AdminPosition  # done table


class Product(BaseModel):
    product_id: int
    product_name: str
    product_price: float
    product_image_link: AnyUrl
    product_stock: int
    product_type: ProductType
    product_allergic_ingredients: list[str]
    product_is_active: bool


class Transaction(BaseModel):
    transaction_id: int
    transaction_agent: str
    transaction_description: str
    transaction_type: TransactionType  # done table
    transaction_amount: Optional[float]
    transaction_date: dt.datetime


class Record(BaseModel):
    record_id: int
    record_interval: RecordInterval
