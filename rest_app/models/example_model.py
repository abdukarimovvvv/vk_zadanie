from typing import Any

from pydantic import BaseModel


class ExampleModel(BaseModel):
    kind: Any = None
    name: str = None
    description: str = None
    version: str = None
    configuration: object = None
