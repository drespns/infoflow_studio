import pandas as pd
from app.core.base_node import BaseNode
from app.core.exceptions import (
    InvalidConfigurationError,
    MissingInputError,
    NodeExecutionError
)


class RenameColumnNode(BaseNode):
    """
    Nodo que renombra una columna de un DataFrame.

    Config esperada:
    {
        "old_name": "age",
        "new_name": "edad"
    }

    Requiere exactamente un nodo de entrada.
    """

    def validate_config(self):
        """
        Verifica que la configuración tenga:
        - old_name
        - new_name
        """

        required_keys = ["old_name", "new_name"]

        for key in required_keys:
            if key not in self.config:
                raise InvalidConfigurationError(
                    f"RenameColumnNode ({self.node_id}) requiere '{key}' en config"
                )

        # Validación adicional: evitar nombres vacíos
        if not self.config["old_name"] or not self.config["new_name"]:
            raise InvalidConfigurationError(
                f"RenameColumnNode ({self.node_id}) no permite nombres vacíos"
            )

    def execute(self) -> pd.DataFrame:
        """
        Ejecuta el renombrado de columna.

        Flujo:
        1. Verifica que exista nodo de entrada.
        2. Obtiene DataFrame del padre.
        3. Verifica que la columna original exista.
        4. Verifica que el nuevo nombre no exista ya.
        5. Devuelve nuevo DataFrame con columna renombrada.
        """

        if not self.inputs:
            raise MissingInputError(
                f"RenameColumnNode ({self.node_id}) no tiene nodo de entrada"
            )

        df: pd.DataFrame = self.inputs[0].output

        old_name = self.config["old_name"]
        new_name = self.config["new_name"]

        # Validar que la columna original exista
        if old_name not in df.columns:
            raise NodeExecutionError(
                f"La columna '{old_name}' no existe en el DataFrame"
            )

        # Validar que no sobrescribimos otra columna existente
        if new_name in df.columns:
            raise NodeExecutionError(
                f"La columna '{new_name}' ya existe en el DataFrame"
            )

        try:
            # pandas rename devuelve nuevo DataFrame (no modifica in-place)
            renamed_df = df.rename(columns={old_name: new_name})
            return renamed_df

        except Exception as e:
            raise NodeExecutionError(
                f"Error renombrando columna en nodo {self.node_id}: {str(e)}"
            )
