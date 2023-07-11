from libs.models.ui.CityConnection import CityConnection
from libs.models.ui.CityPoint import CityPoint


class CityPointFactory:
    def __init__(self, nodes: list, conns: list):
        self._node_coords: dict = {}
        self.nodes: list[CityPoint] = self.createObject(nodes)
        self.conns: list[CityConnection] = self.createConnectionObject(conns)

    def createObject(self, data) -> list[CityPoint]:
        result_list = []
        for row in data:
            id = row.get("id")
            x = row.get("x")
            y = row.get("y")
            name = row.get("name")
            description = row.get("description")
            self._node_coords[id] = [x, y]
            result_list.append(CityPoint(id, x, y, name, description))
        return result_list

    def createConnectionObject(self, data) -> list[CityConnection]:
        result_list = []
        for row in data:
            node_from = row.get("from")
            node_to = row.get("to")
            weight = row.get("weight")
            try:
                x0, y0 = self._node_coords[node_from]
                x1, y1 = self._node_coords[node_to]
                result_list.append(CityConnection(-1, node_from, node_to, x0, y0, x1, y1, weight))
            except Exception as e:
                print(e)
        return result_list

    def getObjects(self):
        return self.nodes, self.conns
