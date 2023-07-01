from pydantic import BaseModel


class TgModel(BaseModel):
    user_id: str = None
    bot_token: str
    tg_api: str = None
    tg_proxy: str = None
    forward_from: list[int] = []
    black_id: list[int] = []


class ActivitiesModel(BaseModel):
    black_keywords: list[str] = []
    black_script: list[str] = []


class QlModel(BaseModel):
    file: str = "qlva.sh"
    url: str
    Client_ID: str
    Client_Secret: str
    expiration: int = 0  # 青龙auth过期时间
    Authorization: str = None
    class Config:
        orm_mode = True


class ProjectModel(BaseModel):
    log_level: str = "INFO"
    log_path: str = "logs/"
    Version: float = 0.2
    Identity: str = "内测版本"


class ConfModel(BaseModel):
    tg: TgModel
    activities: ActivitiesModel
    ql: QlModel
    project: ProjectModel

    class Config:
        orm_mode = True
