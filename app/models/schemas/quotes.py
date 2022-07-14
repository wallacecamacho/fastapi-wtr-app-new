from typing import List

from pydantic import BaseModel


class Quotes(BaseModel):
    tickersName: List[str]
