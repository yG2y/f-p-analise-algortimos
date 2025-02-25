from graphviz import Digraph
import os

# Especifique o caminho do executável dot
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

# Cria o grafo
dot = Digraph(comment='Fluxo de Controle do Algoritmo de Karatsuba')

# Adiciona nós e arestas
dot.node('A', 'Início: Verifica se x ou y são pequenos')
dot.node('B', 'Divide x e y em partes menores')
dot.node('C', 'Calcula ac = karatsuba(a, c)')
dot.node('D', 'Calcula bd = karatsuba(b, d)')
dot.node('E', 'Calcula (a+b)(c+d) = karatsuba(a+b, c+d)')
dot.node('F', 'Calcula ad_bc = (a+b)(c+d) - ac - bd')
dot.node('G', 'Combina resultados: ac * 10^n + ad_bc * 10^(n/2) + bd')
dot.node('H', 'Fim: Retorna o resultado')

dot.edge('A', 'B', label='x ou y têm mais de 1 dígito')
dot.edge('A', 'H', label='x ou y têm 1 dígito')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('E', 'F')
dot.edge('F', 'G')
dot.edge('G', 'H')

# Renderiza o grafo
dot.render('karatsuba_flow', format='pdf', cleanup=True)

print("Grafo gerado com sucesso! Verifique o arquivo 'karatsuba_flow.pdf'.")