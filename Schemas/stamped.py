from pydantic import BaseModel
from typing import Optional

class Stamped( BaseModel ):
    Total: float
    TipoComprobante: str
    description: str
    decimals: int
    status: Optional[int] = 1