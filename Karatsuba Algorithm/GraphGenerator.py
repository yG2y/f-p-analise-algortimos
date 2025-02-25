import matplotlib.pyplot as plt
import networkx as nx

# Cria um grafo direcionado
gh_graph = nx.DiGraph()

# Adiciona nós (etapas do algoritmo)
gh_graph.add_node('A', label='Início: Verifica se x ou y são pequenos')
gh_graph.add_node('B', label='Divide x e y em partes menores')
gh_graph.add_node('C', label='Calcula ac = karatsuba(a, c)')
gh_graph.add_node('D', label='Calcula bd = karatsuba(b, d)')
gh_graph.add_node('E', label='Calcula (a+b)(c+d) = karatsuba(a+b, c+d)')
gh_graph.add_node('F', label='Calcula ad_bc = (a+b)(c+d) - ac - bd')
gh_graph.add_node('G', label='Combina resultados: ac * 10^n + ad_bc * 10^(n/2) + bd')
gh_graph.add_node('H', label='Fim: Retorna o resultado')

# Adiciona arestas (fluxo de execução)
gh_graph.add_edge('A', 'B', label='x ou y têm mais de 1 dígito')
gh_graph.add_edge('A', 'H', label='x ou y têm 1 dígito')
gh_graph.add_edge('B', 'C')
gh_graph.add_edge('C', 'D')
gh_graph.add_edge('D', 'E')
gh_graph.add_edge('E', 'F')
gh_graph.add_edge('F', 'G')
gh_graph.add_edge('G', 'H')

# Define o layout do grafo
spring_pos = nx.spring_layout(gh_graph)

# Desenha o grafo
plt.figure(figsize=(8, 8))
nx.draw(gh_graph, pos=spring_pos, with_labels=True, node_color='gray', node_size=2000, font_size=10, font_weight='bold', edge_color='gray', width=2, arrows=True)

# Adiciona rótulos às arestas
edge_labels = nx.get_edge_attributes(gh_graph, 'label')
nx.draw_networkx_edge_labels(gh_graph, pos=spring_pos, edge_labels=edge_labels, font_color='blue')

# Exibe o grafo
plt.title("Fluxo de Controle do Algoritmo de Karatsuba")
plt.show()