import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.pipeline import Pipeline
from app.transformations.filter_rows import FilterRowsNode
from app.transformations.groupby import GroupByNode
from app.transformations.load_csv import LoadCSVNode
from app.transformations.rename_column import RenameColumnNode


# Creamos una instancia del pipeline
pipeline = Pipeline()

# Nodo raíz: carga de datos
load_node = LoadCSVNode(
    node_id="load1",
    config={"path": "sample.csv"}
)

# Nodo de transformación: filtrado
filter_node = FilterRowsNode(
    node_id="filter1",
    config={
        "column": "age",
        "operator": ">",
        "value": 30
    }
)

rename_node = RenameColumnNode(
    node_id="rename1",
    config={
        "old_name": "age",
        "new_name": "edad"
    }
)

group_node = GroupByNode(
    node_id="group1",
    config={
        "group_by": ["edad"],
        "aggregations": {
            "salary": "mean"
        }
    }
)

# Añadimos nodos al pipeline
pipeline.add_node(load_node)
pipeline.add_node(rename_node)
pipeline.add_node(filter_node)
pipeline.add_node(group_node)


# Conectamos nodos (load → filter)
pipeline.connect("load1", "filter1")
pipeline.connect("filter1", "rename1")  # (filter → rename)
pipeline.connect("rename1", "group1")  # (rename → group)

# Ejecutamos el pipeline hasta el nodo final
# result = pipeline.execute("filter1")
# result = pipeline.execute("rename1")
result = pipeline.execute("group1")

# Mostramos resultado
print(result.head())
