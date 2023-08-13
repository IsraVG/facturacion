from pydantic import BaseModel
from typing import Optional

class TaxRegime( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    physical_person: int
    moral_person: int
    status: Optional[int] = 1