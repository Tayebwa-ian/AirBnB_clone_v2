#!/usr/bin/python3
"""State Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Holds state attributes and Functions
    Attrs:
        name: State's name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("cities", backref="state",
                          cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
