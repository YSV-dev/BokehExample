from libs.models.ui.abstraction.IGraphPoint import IGraphPoint


class CityPoint(IGraphPoint):
    def __init__(self,
                 id: int = -1,
                 x: float = 0,
                 y: float = 0,
                 name: str = "unnamed",
                 description: str = ""):
        super().__init__(id, x, y, name, description)

