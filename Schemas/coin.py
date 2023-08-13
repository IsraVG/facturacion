from pydantic import BaseModel
from typing import Optional

class Coin( BaseModel ):
    id: Optional[int]
    code: str
    description: str
    decimals: int
    status: Optional[int] = 1