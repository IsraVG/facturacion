from turtle import st
from unicodedata import decimal
from pydantic import BaseModel
from typing import Optional

class CfdiUse( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    phisical_person: int
    moral_person: int
    tax_regime_code: str
    status: Optional[int] = 1