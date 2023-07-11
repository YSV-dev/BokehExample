from abc import ABC, abstractmethod


class IGraphConnection(ABC):
    @abstractmethod
    def __init__(self,
                 id: int = -1,
                 node_from: int = -1,
                 node_to: int = -1,
                 x0: float = 0,
                 y0: float = 0,
                 x1: float = 0,
                 y1: float = 0,
                 weight: float = 0):
        self.id: int = id
        self.node_from = node_from
        self.node_to = node_to
        self.x0: float = x0
        self.y0: float = y0
        self.x1: float = x1
        self.y1: float = y1
        self.weight: float = weight

    def getID(self):
        return self.id

    def getX0(self):
        return self.x0

    def getX1(self):
        return self.x1

    def getY0(self):
        return self.y0

    def getY1(self):
        return self.y1

    def getWeight(self):
        return self.weight

    def getFrom(self):
        return self.node_from

    def getTo(self):
        return self.node_to
