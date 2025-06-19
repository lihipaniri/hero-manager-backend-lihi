from datetime import datetime

from src.controllers.utils.base_api_model import BaseApiModel


class NewHero(BaseApiModel):
    name: str
    suit_color: str
    has_cape: bool
    last_mission: datetime | None = None
    powers: list[str] | None = []
