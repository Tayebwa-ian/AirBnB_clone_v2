#!/usr/bin/python3
"""Review Model-Module(Inherits from the BaseModel)"""
from .base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Review(BaseModel, Base):
    """Holds review attributes and Functions
    Attrs:
        text: review message
        user: the user who made the review
        place: the place where it was made
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
