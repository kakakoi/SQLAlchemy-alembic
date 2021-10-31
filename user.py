from sqlalchemy import Column, String, Integer
from sqlalchemy.engine import base
from setting import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    