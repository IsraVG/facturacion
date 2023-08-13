from pydantic import BaseModel
from typing import Optional

class CustomHouse( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    status: Optional[int] = 1