class Graph:
    def __init__(self, vertices, directed=False):
        """
        Inicializa o grafo
        :param vertices: número de vértices
        :param directed: se o grafo é orientado (default=False)
        """
        self.vertices = vertices
        self.directed = directed
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
        self.adj_list = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        """
        Adiciona uma aresta entre os vértices u e v
        :param u: vértice de origem
        :param v: vértice de destino
        """
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_matrix[u][v] = 1
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_matrix[v][u] = 1
                self.adj_list[v].append(u)
    
    def hamiltonian_path(self):
        """
        Encontra um caminho hamiltoniano no grafo
        :return: lista com a ordem dos vértices no caminho ou None se não existir
        """
        path = []
        
        # Função auxiliar para verificar se o vértice pode ser adicionado ao caminho
        def is_safe(v, pos, path):
            # Verifica se o vértice está conectado ao vértice anterior no caminho
            if self.adj_matrix[path[pos-1]][v] == 0:
                return False
            
            # Verifica se o vértice já não está no caminho
            if v in path:
                return False
                
            return True
        
        # Função recursiva para encontrar o caminho
        def hamiltonian_path_util(path):
            # Caso base: todos os vértices estão no caminho
            if len(path) == self.vertices:
                return True
                
            # Tenta adicionar cada vértice ao caminho
            for v in range(self.vertices):
                if is_safe(v, len(path), path):
                    path.append(v)
                    
                    if hamiltonian_path_util(path):
                        return True
                        
                    # Backtracking
                    path.pop()
            
            return False
        
        # Tenta iniciar o caminho de cada vértice
        for start_vertex in range(self.vertices):
            path = [start_vertex]
            
            if hamiltonian_path_util(path):
                return path
                
        return None
    
    def print_hamiltonian_path(self):
        """
        Imprime um caminho hamiltoniano se existir
        """
        path = self.hamiltonian_path()
        
        if path:
            print("Caminho Hamiltoniano encontrado:")
            print(" -> ".join(map(str, path)))
        else:
            print("Nenhum Caminho Hamiltoniano encontrado no grafo.")


# Função para criar grafo a partir da entrada do usuário
def create_graph_from_input():
    print("Criando um grafo:")
    directed = input("O grafo é orientado? (s/n): ").lower() == 's'
    vertices = int(input("Número de vértices: "))
    
    graph = Graph(vertices, directed)
    
    print("Digite as arestas (formato: origem destino)")
    print("Digite 'fim' para terminar)")
    
    while True:
        edge = input("Aresta: ").strip()
        if edge.lower() == 'fim':
            break
        
        try:
            u, v = map(int, edge.split())
            graph.add_edge(u, v)
        except ValueError:
            print("Formato inválido. Use: origem destino (Ex: 0 1)")
    
    return graph


# Menu interativo
def main_menu():
    print("\nMenu:")
    print("1. Criar grafo manualmente")
    print("2. Usar grafo de exemplo (não orientado)")
    print("3. Usar grafo de exemplo (orientado)")
    print("4. Sair")
    
    choice = input("Escolha uma opção: ")
    return choice


# Exemplos de grafos
def example_undirected_graph():
    """Grafo não orientado com caminho hamiltoniano"""
    g = Graph(5, directed=False)
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    return g

def example_directed_graph():
    """Grafo orientado com caminho hamiltoniano"""
    g = Graph(5, directed=True)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 4)
    g.add_edge(1, 3)
    return g


# Programa principal
if __name__ == "__main__":
    print("Implementação do Algoritmo para Caminho Hamiltoniano")
    
    graph = None
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            graph = create_graph_from_input()
            graph.print_hamiltonian_path()
        elif choice == '2':
            graph = example_undirected_graph()
            print("\nGrafo de exemplo não orientado criado:")
            graph.print_hamiltonian_path()
        elif choice == '3':
            graph = example_directed_graph()
            print("\nGrafo de exemplo orientado criado:")
            graph.print_hamiltonian_path()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")