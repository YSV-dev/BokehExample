import uuid

from bokeh import events
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Button, LabelSet, ColumnDataSource, TapTool
from bokeh.plotting import figure
from bokeh.embed import components

from libs.generatable_ui.abstraction.IGraph import IGraph
from libs.models.ui.CityConnection import CityConnection
from libs.models.ui.abstraction.IGraphPoint import IGraphPoint


class InteractiveGraph2D(IGraph):
    def __init__(self, data: list[IGraphPoint], connections: list[CityConnection], title: str = "",
                 dot_size: float = 5):
        self.title = title
        self.data = data
        self.connections = connections
        self.dot_size = dot_size
        self.uuid: str = str(uuid.uuid4()).replace("-", "_")
        self._build()

    def _build(self):
        graph = figure(title=self.title, toolbar_location="above", tools="pan,wheel_zoom,box_zoom,reset")
        x = []
        y = []
        name = []
        id = []
        description = []

        for point in self.data:
            x.append(point.getX())
            y.append(point.getY())
            name.append(point.getName())
            id.append(point.getID())
            description.append(point.getDescription())

        for connection in self.connections:
            x0 = connection.x0
            x1 = connection.x1
            y0 = connection.y0
            y1 = connection.y1
            weight = connection.weight
            graph.line([x0, x1], [y0, y1], line_width=2)

        source = ColumnDataSource(data=dict(
            id=id,
            x=x,
            y=y,
            name=name,
            description=description
        ))

        cr = graph.circle(x, y, size=self.dot_size)
        print(cr.js_event_callbacks)

        labels = LabelSet(x='x', y='y', text='name', text_font_size='9pt',
                          x_offset=5, y_offset=5, source=source,
                          text_baseline="middle", text_align="center")
        graph.add_layout(labels)

        callback = CustomJS(args={'circle': source, 'geom': cr}, code=
        f"""
                                const selected_node_id = cb_data.source.selected.indices[0];
                                
                                const selected_node =
                                    {{
                                        id: circle.data.id[selected_node_id],
                                        name: circle.data.name[selected_node_id],
                                        description: circle.data.description[selected_node_id]
                                    }} 
                                
                                current_value_{self.uuid} = selected_node;
                            """
                            )
        tap_tool = TapTool(mode='replace', callback=callback, renderers=[cr])
        graph.add_tools(tap_tool)

        card_btn = Button(button_type='default', label="Карточка", margin=5)
        card_btn.js_on_event(events.ButtonClick, CustomJS(code=
                                                          f"show_card_{self.uuid}(current_value_{self.uuid})"))
        delete_btn = Button(button_type='danger', label="Удалить", margin=5)
        delete_btn.js_on_event(events.ButtonClick, CustomJS(code=
                                                            f"delete_{self.uuid}(current_value_{self.uuid})"))

        layout = column(graph, row(delete_btn, card_btn))

        script, div = components(layout)

        custom_js = f"""
            <script>
                var current_value_{self.uuid} = undefined;
            
                function show_card_{self.uuid} () {{
                    if(current_value_{self.uuid}){{
                        let description_modal = new bootstrap.Modal(document.getElementById('description_modal'))
                        let modal_content = document.getElementById('description_modal_content');
                        let title = document.getElementById('description_modal_label');
                        title.innerHTML = `${{current_value_{self.uuid}.name}}`;
                        modal_content.innerHTML = `<p>${{current_value_{self.uuid}.description}}</p>`;
                        description_modal.show();
                    }}
                }}
                
                function delete_{self.uuid} (selected_node) {{
                    if(current_value_{self.uuid}){{
                        let id = current_value_{self.uuid}.id
                        const response = fetch('/node/' + id, 
                            {{ method: 'DELETE' }})
                            .then(response => {{
                                if (response.status === 200) {{
                                    location. reload();
                                }}
                            }}) 
                    }}
                }}
            </script>"""

        self._html = custom_js + script + div

    def getHTML(self) -> str:
        return self._html
