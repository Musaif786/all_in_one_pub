from pydantic import BaseModel

class storingData(BaseModel):
    name: str
    num: int
    desc: str