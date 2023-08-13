from pydantic import BaseModel
from typing import Optional

class Periodicity( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    status: Optional[int] = 1