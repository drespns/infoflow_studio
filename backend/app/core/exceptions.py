class InfoflowError(Exception):
    """
    Excepción base del sistema Infoflow.
    Todas las demás excepciones heredan de esta.
    """
    pass


class NodeExecutionError(InfoflowError):
    """
    Error durante la ejecución de un nodo.
    """
    pass


class InvalidConfigurationError(InfoflowError):
    """
    Error cuando la configuración de un nodo es inválida.
    """
    pass


class MissingInputError(InfoflowError):
    """
    Error cuando un nodo requiere inputs y no los tiene.
    """
    pass


class PipelineCycleError(InfoflowError):
    """
    Error cuando se detecta un ciclo en el DAG.
    """
    pass