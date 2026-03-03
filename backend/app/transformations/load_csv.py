
import pandas as pd

from app.core.base_node import BaseNode


class LoadCSVNode(BaseNode):

    """
    Nodo encargado de cargar un archivo CSV desde disco.

    Este nodo suele ser un nodo raíz (no tiene inputs).
    """

    def execute(self) -> pd.DataFrame:
        """
        Lee el archivo CSV indicado en la configuración.

        Config esperada:
        {
            "path": "ruta/al/archivo.csv"
        }
        """

        path = self.config.get("path")

        # Podríamos añadir aquí:
        # - Validación de existencia
        # - Manejo de encoding
        # - Parámetros opcionales (delimiter, header, etc.)

        df = pd.read_csv(path)

        return df
