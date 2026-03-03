import os
import pandas as pd
from app.core.base_node import BaseNode
from app.core.exceptions import InvalidConfigurationError, NodeExecutionError


class LoadCSVNode(BaseNode):
    """
    Nodo responsable de cargar un archivo CSV.

    Normalmente es un nodo raíz (no depende de otros nodos).
    Produce un DataFrame a partir de un archivo en disco.
    """

    def validate_config(self):
        """
        Validamos que la configuración contenga la clave 'path'.

        Esta validación ocurre en el constructor del nodo,
        antes de que se ejecute cualquier pipeline.
        """

        path = self.config.get("path")

        if not path:
            raise InvalidConfigurationError(
                f"LoadCSVNode ({self.node_id}) requiere 'path' en config"
            )

    def execute(self) -> pd.DataFrame:
        """
        Ejecuta la lectura del CSV.

        Flujo:
        1. Verifica que el archivo existe.
        2. Intenta leerlo con pandas.
        3. Si falla, lanza error controlado.
        """

        path = self.config.get("path")

        # Validamos que el archivo realmente exista en disco
        if not os.path.exists(path):
            raise NodeExecutionError(
                f"Archivo no encontrado: {path}"
            )

        try:
            # Pandas se encarga de parsear el CSV.
            # Más adelante podremos añadir:
            # - encoding configurable
            # - delimiter configurable
            # - lectura en chunks
            df = pd.read_csv(path)
            return df

        except Exception as e:
            # Encapsulamos cualquier error en uno propio
            raise NodeExecutionError(
                f"Error leyendo CSV en nodo {self.node_id}: {str(e)}"
            )
