from pydantic import BaseModel, SecretStr
from typing import Optional

from enums.work_position import CanteenPosition

"""

"""


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


class CanteenStaff(BaseModel):
    staff_id: int
    staff_full_name: str
    staff_contact_number: str
    staff_username: str
    staff_password: SecretStr
    staff_address: str
    staff_position: CanteenPosition
    staff_is_active: bool

