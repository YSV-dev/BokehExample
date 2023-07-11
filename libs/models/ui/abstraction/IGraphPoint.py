from abc import abstractmethod, ABC


class IGraphPoint(ABC):
    @abstractmethod
    def __init__(self, id: int = -1, x: float = 0, y: float = 0, name: str = "", description: str = ""):
        self._id = id
        self._x = x
        self._y = y
        self._name = name
        self._description = description

    def getID(self):
        return self._id

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description
