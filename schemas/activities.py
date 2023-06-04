from pydantic import BaseModel


class ExportModel(BaseModel):
    name: str
    alias: str
    value: str = None  # export .....
    delays: int

    class Config:
        orm_mode = True
