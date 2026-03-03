
from app.core.exceptions import InvalidConfigurationError
from app.core.pipeline import Pipeline
from app.registry import NODE_REGISTRY


def build_pipeline_from_json(pipeline_data):
    """
    Construye un Pipeline real a partir del JSON validado.
    """

    pipeline = Pipeline()

    # Crear nodos
    for node_data in pipeline_data.nodes:
        node_type = node_data.type

        if node_type not in NODE_REGISTRY:
            raise InvalidConfigurationError(
                f"Tipo de nodo no soportado: {node_type}"
            )

        node_class = NODE_REGISTRY[node_type]

        node_instance = node_class(  # NOTE NODE_REGISTRY = { "load_csv": LoadCSVNode,
            node_id=node_data.id,
            config=node_data.config
        )  # (class) BaseNode def __init__(self, node_id: str, config: dict):

        pipeline.add_node(node_instance)

    # Crear conexiones
    for edge in pipeline_data.edges:
        pipeline.connect(edge.source, edge.target)

    return pipeline
