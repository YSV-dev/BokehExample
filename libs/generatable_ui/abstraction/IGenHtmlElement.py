"""
Интерфейс элемента, который может генерировать HTML код, например графики, схемы или формы
"""
from abc import abstractmethod, ABC


class IGenHtmlElement(ABC):
    @abstractmethod
    def getHTML(self) -> str:
        pass
