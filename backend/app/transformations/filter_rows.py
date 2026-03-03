
import pandas as pd

from app.core.base_node import BaseNode


class FilterRowsNode(BaseNode):

    """
    Nodo que filtra filas de un DataFrame según una condición.

    Requiere exactamente un nodo de entrada.
    """

    def execute(self) -> pd.DataFrame:
        """
        Config esperada:
        {
            "column": "age",
            "operator": ">",
            "value": 30
        }
        """

        # Validación básica de dependencia
        if not self.inputs:
            raise ValueError("FilterRowsNode necesita un nodo de entrada")

        # Obtenemos el DataFrame del nodo padre
        df = self.inputs[0].output

        column = self.config.get("column")
        operator = self.config.get("operator")
        value = self.config.get("value")

        # Aquí estamos aplicando el filtro dinámicamente.
        # En el futuro podríamos:
        # - Permitir múltiples condiciones
        # - Permitir operadores lógicos AND/OR
        # - Usar expresiones más complejas

        if operator == ">":
            return df[df[column] > value]
        elif operator == "<":
            return df[df[column] < value]
        elif operator == "==":
            return df[df[column] == value]
        elif operator == "!=":
            return df[df[column] != value]
        else:
            raise ValueError(f"Operador no soportado: {operator}")
