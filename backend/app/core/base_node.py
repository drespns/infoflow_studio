from abc import ABC, abstractmethod

import pandas as pd


class BaseNode(ABC):

    """
    Clase base abstracta para todos los nodos del pipeline.

    Cada nodo representa una transformación dentro del DAG.
    Puede tener nodos padre (inputs) y produce un DataFrame como salida.

    Esta clase define la interfaz común que todos los nodos deben implementar.
    """

    def __init__(self, node_id: str, config: dict):
        """
        :param node_id: Identificador único del nodo dentro del pipeline.
        :param config: Diccionario con la configuración específica de la transformación.
        """
        self.node_id = node_id

        # Configuración específica del nodo (por ejemplo:
        # columna, operador, ruta del archivo, etc.)
        self.config = config

        # Lista de nodos de los que depende este nodo.
        # En un DAG, estos serían los nodos "padre".
        self.inputs = []

        # Cache del resultado del nodo tras ejecutar.
        # Evita recomputar si se reutiliza más adelante.
        self.output = None

    def add_input(self, node: "BaseNode"):
        """
        Conecta un nodo padre a este nodo.

        :param node: Nodo del cual depende este nodo.
        """
        self.inputs.append(node)

    @abstractmethod
    def execute(self) -> pd.DataFrame:
        """
        Método que cada nodo debe implementar.

        Debe ejecutar la transformación correspondiente y devolver
        un DataFrame como resultado.
        """
        pass
