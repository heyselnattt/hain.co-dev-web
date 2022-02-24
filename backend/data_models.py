from pydantic import BaseModel, SecretStr
from typing import Optional

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
