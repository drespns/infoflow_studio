from app.core.exceptions import PipelineCycleError


class Pipeline:
    """
    Representa un grafo dirigido acíclico (DAG) de nodos.

    Responsabilidades principales:
    - Almacenar nodos.
    - Conectar dependencias entre nodos.
    - Determinar el orden correcto de ejecución.
    - Ejecutar el pipeline hasta un nodo objetivo.

    Este objeto NO conoce detalles internos de cada transformación.
    Solo gestiona estructura y orden de ejecución.
    """

    def __init__(self):
        # Diccionario que almacena todos los nodos del pipeline.
        # Clave: node_id
        # Valor: instancia del nodo.
        #
        # Esto permite acceso rápido O(1) a cualquier nodo.
        self.nodes = {}

    def add_node(self, node):
        """
        Añade un nodo al pipeline.

        Nota:
        No validamos duplicados aquí todavía.
        En una versión más madura deberíamos impedir IDs repetidos.
        """
        self.nodes[node.node_id] = node

    def connect(self, parent_id: str, child_id: str):
        """
        Crea una dependencia entre nodos.

        parent → child

        Esto significa:
        El nodo 'child' necesita el resultado del nodo 'parent'.

        Internamente:
        - Buscamos ambos nodos en el diccionario.
        - Añadimos el padre como input del hijo.
        """

        parent = self.nodes[parent_id]
        child = self.nodes[child_id]

        # La dependencia se guarda en el nodo hijo.
        child.add_input(parent)

    def execute(self, target_node_id: str):
        """
        Ejecuta el pipeline hasta el nodo indicado.

        Solo se ejecutan:
        - El nodo objetivo
        - Y todos sus ancestros (dependencias)

        Flujo:
        1. Calculamos orden topológico.
        2. Ejecutamos cada nodo en orden.
        3. Devolvemos el resultado final.
        """

        # Determinar orden correcto según dependencias
        ordered_nodes = self._topological_sort(target_node_id)

        # Ejecutamos nodo por nodo
        for node in ordered_nodes:
            node.output = node.execute()

        return self.nodes[target_node_id].output  # TODO TYPE

    def _topological_sort(self, target_node_id):
        """
        Realiza un ordenamiento topológico usando DFS.

        Esto garantiza que:
        - Ningún nodo se ejecuta antes que sus dependencias.
        - Se detectan ciclos en el grafo.

        Usamos:
        - visited: nodos ya procesados.
        - visiting: nodos en la pila actual (para detectar ciclos).
        - stack: resultado final ordenado.
        """

        visited = set()
        visiting = set()  # Detecta ciclos
        stack = []

        def visit(node):

            # Si el nodo está en 'visiting',
            # significa que estamos intentando volver a entrar en él
            # antes de terminar su procesamiento → ciclo.
            if node.node_id in visiting:
                raise PipelineCycleError(
                    f"Ciclo detectado en nodo {node.node_id}"
                )

            # Si ya fue procesado completamente, no hacemos nada.
            if node.node_id in visited:
                return

            # Marcamos como "en proceso"
            visiting.add(node.node_id)

            # Visitamos primero todas sus dependencias
            for parent in node.inputs:
                visit(parent)

            # Quitamos de visiting y marcamos como visitado
            visiting.remove(node.node_id)
            visited.add(node.node_id)

            # Añadimos al orden final
            stack.append(node)

        # Iniciamos desde el nodo objetivo
        visit(self.nodes[target_node_id])

        return stack
