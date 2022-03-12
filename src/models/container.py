from typing import Any, Dict, List
from pydantic import BaseModel


class ContainerModel(BaseModel):
    Id: str
    Names: List[str]
    Image: str
    ImageID: str
    Ports: List[Dict[Any, Any]]
    Lables: Dict[str, str]
