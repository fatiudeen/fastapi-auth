# from typing import Optional
# from pydantic import BaseModel

# class User(BaseModel):include_router
#     id: int
#     email: str
#     fullname: str
#     password: str
#     email_verified: bool
#     password_reset_token: Optional[str]


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.utils.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)