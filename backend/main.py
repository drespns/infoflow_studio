import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.pipeline import Pipeline
from app.transformations.load_csv import LoadCSVNode
from app.transformations.filter_rows import FilterRowsNode


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

# Añadimos nodos al pipeline
pipeline.add_node(load_node)
pipeline.add_node(filter_node)

# Conectamos nodos (load → filter)
pipeline.connect("load1", "filter1")

# Ejecutamos el pipeline hasta el nodo final
result = pipeline.execute("filter1")

# Mostramos resultado
print(result.head())
