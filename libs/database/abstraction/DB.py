import traceback
from abc import ABC, abstractmethod
import json


class DB(ABC):
    def __init__(self, connection_params: dict = None):
        self.host: str = ""
        self.port: int = -1
        self.user: str = ""
        self.password: str = ""
        self.db_name: str = ""

        if connection_params is None:
            self.connection_params = {}
        else:
            self.connection_params = connection_params

    def set_connection_params(self, settings_file_path: str = "settings.json", connection_name: str = None):
        if connection_name is None:
            raise "Connection name must be declared!"

        with open(settings_file_path) as settings_file:
            try:
                json_object = dict(json.loads(settings_file.read()))
                self.connection_params = json_object.get("db").get(connection_name)
            except json.JSONDecodeError:
                traceback.print_exc()
                raise "Settings are incorrect. JSON parse error!"
            except KeyError:
                traceback.print_exc()
                raise "Connection with this name doesn't exist!"
        self._parseParams()

    @abstractmethod
    def _parseParams(self):
        try:
            self.host = self.connection_params.get("host")
            self.port = self.connection_params.get("port")
            self.user = self.connection_params.get("db_user")
            self.password = self.connection_params.get("db_password")
            self.db_name = self.connection_params.get("db_name")
        except KeyError:
            traceback.print_exc()
            raise "Error with parsing value"

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, sql: str) -> list:
        pass

    @abstractmethod
    def execute_file(self, sql_file_path: str) -> list:
        pass
