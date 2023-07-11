import json

from flask import Flask, render_template, request

from libs.database.JSONFile import JSONFile
from libs.factories.CityPointFactory import CityPointFactory
from libs.generatable_ui.InteractiveGraph2D import InteractiveGraph2D

app = Flask(__name__)

"""Здесь могла быть ваша база))"""
# main_db: DBPool = PostgreSqlDBPool()
# main_db.set_connection_params("settings.json", "main")
# main_db.connect()
#
# if main_db is DBPool:
#     atexit.register(main_db.closeAllConnection())


"""
    Проект простенький, поэтому не вижу особого смысла выносить роуты в отдельный класс
    или делать ORM. Короче всё максимально просто
"""

@app.route('/')
def index():
    data = JSONFile.read_file("nodes.json")
    points, conns = CityPointFactory(data.get("nodes"), data.get("connections")).getObjects()
    graph = InteractiveGraph2D(data=points, connections=conns, dot_size=20)
    html = graph.getHTML()
    return render_template("index.html", interactiveGraphLink=html)


@app.route('/node/<id>', methods=["DELETE"])
def node_api(id):
    status = 404
    file_name = "nodes.json"
    if request.method == 'DELETE':
        data = JSONFile.read_file(file_name)
        status = 204
        for node in data.get("nodes"):
            if node.get("id") == int(id):
                data.get("nodes").remove(node)
                status = 200
                break
        for connection in data.get("connections"):
            if connection.get("from") == int(id) or connection.get("to") == int(id):
                data.get("connections").remove(connection)
        print(str(json))
        JSONFile.write_file(file_name, data)

    response = app.response_class(
        status=status
    )
    return response


if __name__ == "__main__":
    app.run(port=3100, debug=True)
