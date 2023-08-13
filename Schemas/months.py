from turtle import st
from unicodedata import decimal
from pydantic import BaseModel
from typing import Optional

class Months( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    status: Optional[int] = 1