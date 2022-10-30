#!/usr/bin/python3
"""Defines a user class."""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class for user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
