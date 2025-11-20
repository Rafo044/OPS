"""CoreService validasiya modulu"""

from pydantic import BaseModel, EmailStr


class UserValidator(BaseModel):
    name: str
    email: EmailStr


class OrderValidator(BaseModel):
    order_name: str
    order_price: float
