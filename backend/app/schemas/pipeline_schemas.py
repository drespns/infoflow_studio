from typing import List, Dict, Any

from pydantic import BaseModel, Field


class NodeSchema(BaseModel):
    id: str = Field(..., description="Identificador único del nodo")
    type: str = Field(..., description="Tipo lógico del nodo")
    config: Dict[str, Any] = Field(..., description="Configuración del nodo")


class EdgeSchema(BaseModel):
    source: str
    target: str


class PipelineSchema(BaseModel):
    nodes: List[NodeSchema]
    edges: List[EdgeSchema]
    target: str
