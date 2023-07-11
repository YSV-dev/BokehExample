from abc import ABC, abstractmethod

from libs.database.abstraction.DB import DB


class DBPool(DB, ABC):
    def __init__(self, connection_params: dict = None):
        super().__init__(connection_params)
        self.min_con: int = 1
        self.max_con: int = 20
        self.pool: object = None


    @abstractmethod
    def getConnection(self):
        pass

    def _parseParams(self):
        super()._parseParams()
        self.min_con = self.connection_params.get("min_connections", 1)
        self.max_con = self.connection_params.get("max_connections", 20)

    @abstractmethod
    def closeAllConnection(self):
        pass
