from collections import deque


class Pipeline:
    
    """
    Representa un conjunto de nodos conectados en forma de DAG.

    Se encarga de:
    - Almacenar nodos
    - Conectarlos
    - Determinar el orden correcto de ejecución
    - Ejecutar el flujo hasta un nodo objetivo
    """

    def __init__(self):
        # Diccionario de nodos indexados por node_id
        # Permite acceso rápido y único
        self.nodes = {}

    def add_node(self, node):
        """
        Añade un nodo al pipeline.

        :param node: Instancia de BaseNode o subclase.
        """
        self.nodes[node.node_id] = node

    def connect(self, parent_id: str, child_id: str):
        """
        Conecta dos nodos estableciendo dependencia.

        parent → child

        :param parent_id: ID del nodo padre.
        :param child_id: ID del nodo hijo.
        """
        parent = self.nodes[parent_id]
        child = self.nodes[child_id]

        # Añadimos el padre como input del hijo
        child.add_input(parent)

    def execute(self, target_node_id: str):
        """
        Ejecuta el pipeline hasta el nodo objetivo.

        Solo se ejecutan los nodos necesarios para producir
        el resultado final solicitado.

        :param target_node_id: Nodo final que queremos calcular.
        :return: DataFrame resultado del nodo objetivo.
        """

        # Ordenamos los nodos respetando dependencias
        ordered_nodes = self._topological_sort(target_node_id)

        # Ejecutamos en orden
        for node in ordered_nodes:
            node.output = node.execute()

        return self.nodes[target_node_id].output

    def _topological_sort(self, target_node_id):
        """
        Realiza un ordenamiento topológico recursivo.

        Garantiza que:
        - Los nodos padre se ejecutan antes que los hijos.
        - No se rompe la lógica del DAG.
        """

        visited = set()
        stack = []

        def visit(node):
            # Si ya fue visitado, no repetimos
            if node.node_id in visited:
                return

            visited.add(node.node_id)

            # Primero visitamos los nodos de los que depende
            for parent in node.inputs:
                visit(parent)

            # Luego añadimos el nodo actual
            stack.append(node)

        visit(self.nodes[target_node_id])

        return stack