from libs.models.ui.abstraction.IGraphConnection import IGraphConnection


class CityConnection(IGraphConnection):
    def __init__(self,
                 id: int = -1,
                 node_from: int = -1,
                 node_to: int = -1,
                 x0: float = 0,
                 y0: float = 0,
                 x1: float = 0,
                 y1: float = 0,
                 weight: float = 0):
        super().__init__(id, node_from, node_to, x0, y0, x1, y1, weight)
