from pydantic import BaseModel


class ExportModel(BaseModel):
    name: str
    alias: str
    value: str = None  # export .....
    delays: int
    js_level: int

    class Config:
        from_attributes = True
