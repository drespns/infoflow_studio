import pandas as pd
from app.core.base_node import BaseNode
from app.core.exceptions import (
    InvalidConfigurationError,
    MissingInputError,
    NodeExecutionError
)


class GroupByNode(BaseNode):
    """
    Nodo que agrupa un DataFrame por una o varias columnas
    y aplica agregaciones.

    Config esperada:
    {
        "group_by": ["country"],
        "aggregations": {
            "salary": "mean",
            "age": "max"
        }
    }
    """

    def validate_config(self):
        """
        Validamos:
        - group_by debe existir y ser lista no vacía
        - aggregations debe existir y ser dict no vacío
        """

        group_by = self.config.get("group_by")
        aggregations = self.config.get("aggregations")

        if not group_by or not isinstance(group_by, list):
            raise InvalidConfigurationError(
                f"GroupByNode ({self.node_id}) requiere 'group_by' como lista no vacía"
            )

        if not aggregations or not isinstance(aggregations, dict):
            raise InvalidConfigurationError(
                f"GroupByNode ({self.node_id}) requiere 'aggregations' como dict no vacío"
            )

    def execute(self) -> pd.DataFrame:
        """
        Flujo:
        1. Verificar input
        2. Validar que columnas de group_by existan
        3. Validar que columnas de aggregations existan
        4. Ejecutar groupby + agg
        """

        if not self.inputs:
            raise MissingInputError(
                f"GroupByNode ({self.node_id}) no tiene nodo de entrada"
            )

        df = self.inputs[0].output

        group_by = self.config["group_by"]
        aggregations = self.config["aggregations"]

        # Validar columnas de agrupación
        for col in group_by:
            if col not in df.columns:
                raise NodeExecutionError(
                    f"Columna '{col}' no existe para agrupar"
                )

        # Validar columnas de agregación
        for col in aggregations.keys():
            if col not in df.columns:
                raise NodeExecutionError(
                    f"Columna '{col}' no existe para agregación"
                )

        try:
            grouped_df = (
                df
                .groupby(group_by)
                .agg(aggregations)
                .reset_index()
            )

            return grouped_df

        except Exception as e:
            raise NodeExecutionError(
                f"Error ejecutando GroupByNode ({self.node_id}): {str(e)}"
            )
