"""
Интерфейс графа, который может быть сгенерирован в HTML код
"""
from abc import abstractmethod

from libs.generatable_ui.abstraction.IGenHtmlElement import IGenHtmlElement


class IGraph(IGenHtmlElement):
    @abstractmethod
    def getHTML(self) -> str:
        pass

    @abstractmethod
    def _build(self) -> str:
        pass
