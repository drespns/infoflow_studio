import pandas as pd
from app.core.base_node import BaseNode
from app.core.exceptions import (
    InvalidConfigurationError,
    MissingInputError,
    NodeExecutionError
)


class FilterRowsNode(BaseNode):
    """
    Nodo que filtra filas según una condición simple.

    Actualmente:
    - Solo admite una condición
    - Solo admite operadores básicos
    """

    def validate_config(self):
        """
        Verifica que la configuración tenga:
        - column
        - operator
        - value
        """

        required_keys = ["column", "operator", "value"]

        for key in required_keys:
            if key not in self.config:
                raise InvalidConfigurationError(
                    f"FilterRowsNode ({self.node_id}) requiere '{key}' en config"
                )

    def execute(self) -> pd.DataFrame:
        """
        Ejecuta el filtrado sobre el DataFrame del nodo padre.

        Flujo:
        1. Verifica que exista input.
        2. Obtiene DataFrame del padre.
        3. Verifica que la columna exista.
        4. Aplica operador.
        """

        # Este nodo requiere exactamente un input.
        if not self.inputs:
            raise MissingInputError(
                f"FilterRowsNode ({self.node_id}) no tiene nodo de entrada"
            )

        # Obtenemos resultado del nodo padre
        df = self.inputs[0].output

        column = self.config["column"]
        operator = self.config["operator"]
        value = self.config["value"]

        # Validación de existencia de columna
        if column not in df.columns:
            raise NodeExecutionError(
                f"Columna '{column}' no existe en el DataFrame"
            )

        try:
            # Aplicamos operador dinámicamente
            if operator == ">":
                return df[df[column] > value]

            elif operator == "<":
                return df[df[column] < value]

            elif operator == "==":
                return df[df[column] == value]

            elif operator == "!=":
                return df[df[column] != value]

            else:
                raise InvalidConfigurationError(
                    f"Operador no soportado: {operator}"
                )

        except Exception as e:
            # Capturamos errores inesperados
            raise NodeExecutionError(
                f"Error ejecutando filtro en nodo {self.node_id}: {str(e)}"
            )
