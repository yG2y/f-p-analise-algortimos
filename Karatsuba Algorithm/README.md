# Projeto Karatsuba

O Projeto Karatsuba é uma implementação do algoritmo de multiplicação rápida de Karatsuba, que permite multiplicar números grandes de forma eficiente, reduzindo a complexidade em comparação com o método tradicional. Este projeto inclui uma análise detalhada da complexidade ciclomática e assintótica do algoritmo, além de instruções para execução e testes.

## Descrição do Projeto

O algoritmo de Karatsuba é um método de multiplicação que utiliza a técnica de "dividir para conquistar". Ele divide os números em partes menores, realiza multiplicações nessas partes e combina os resultados de forma inteligente. A implementação segue os seguintes passos:

### 1 Divisão dos números:

Os números são divididos em duas partes: uma parte superior (```a``` ou ```c```) e uma parte inferior (```b``` ou ```d```).

Exemplo: ```x = a ⋅ 10^n/2 + b```

### 2 Multiplicações recursivas:

São calculados três produtos: ac, bd e (a+b) (c+d).

### 3 Combinação dos resultados:

O resultado final é obtido pela fórmula:

```x ⋅ y = ac ⋅ 10^n + ((a+b)(c+d) − ac − bd )⋅ 10^n/2 + bd```

### 4 Caso base:

Se os números têm 1 ou 2 dígitos, a multiplicação é feita diretamente. 

## Como Executar o Projeto

### 1. Pré-requisitos:
  Python 3.13.2 instalado.

### 2. Passos para execução:

#### Clone o repositório:
```bash
git clone https://github.com/yG2y/f-p-analise-algortimos.git
cd '.\f-p-analise-algortimos\'
cd '.\Karatsuba Algorithm\'
```

#### Execute o Script:
```bash
python main.py
```

#### Insira os números:
* O programa solicitará dois números para multiplicação.
* Exemplo: 
```bash
1234
5678
```
#### Resultado Esperado:
* O programa exibirá o resultado da multiplicação e o tempo de execução.
* Exemplo: *(tempo pode variar considerando o Hardware)*
```bash
Resultado: 7006652, Tempo: 0.000047 segundos 
```
## Como Executar o Grafo do Projeto

### 1. Pré-requisitos:
  Instalar a biblioteca Matplotlib.
  ```bash
    python -m pip install -U pip
    python -m pip install -U matplotlib
  ```

### 2. Acesse o caminho do código:
Considerando que está na raiz do proejto *f-p-analise-algortimos* utilize os comandos:
```bash
cd '.\Karatsuba Algorithm\'
```

#### Execute o Script:
```bash
python GraphGenerator.py
```

## Relatório Técnico

### Análise da Complexidade Ciclomática

#### Grafo Karatsuba Figura
![Grafo Karatsuba](/Karatsuba%20Algorithm/imgs/FigureGraph.png)

#### Grafo Karatsuba por PDF
![Grafo Karatsuba PDF](/Karatsuba%20Algorithm/imgs/Grafos%20Karatsuba.png)

#### 1. Nós:
* Verificação do caso base (```if x < 10 or y < 10```).
* Divisão dos números (```split_number```).
* Chamadas recursivas para ```karatsuba```.
* Combinação dos resultados.

#### 2. Arestas:

* Fluxo entre as verificações e chamadas recursivas.

#### 3. Grafo de Fluxo:

* O grafo possui 6 nós e 7 arestas.

#### 4. Cálculo da Complexidade Ciclomática:

* Fórmula: ```M = E − N + 2P```, onde:
  - E = 7 (arestas),
  - N = 6 (nós),
  - P = 1 (componentes conexos). 
- Resultado: ```M = 7 − 6 + 2 × 1 = 3```

## Análise da Complexidade Assintótica

### Complexidade Temporal

* Melhor caso: O(1) (números pequenos).
* Caso médio: O(n^log⁡3) ≈ O(n^1,585)
* Pior caso: O(n^log⁡3).

### Complexidade Espacial

* Melhor caso: O(1).
* Caso médio e pior caso: O(*log^n*) (devido à pilha de chamadas recursivas).

## Explicação do código

### Arquivo: ```main.py```

* Função ```karatsuba```:
  - Implementa o algoritmo de Karatsuba.
  - Divide os números, realiza multiplicações recursivas e combina os resultados.
  - Mede o tempo de execução.
  
* Função ```split_number```:
  - Divide um número em duas partes.

* Função ```multiply_small```:
  - Multiplica números pequenos diretamente.

### Estrutura do Código
#### 1. Entrada:
* Solicita dois números ao usuário.

#### 2. Processamento:
* Executa o algoritmo de Karatsuba.

#### Saída:
* Exibe o resultado e o tempo de execução.

## Dependências
* Python pré-instalado

## Exemplo de Saída
```bash
Digite o primeiro número: 1234
Digite o segundo número: 5678
Resultado: 7006652, Tempo: 0.000123 segundos
```

## Referências
* [Karatsuba Algorithm in Python - GeeksforGeeks](https://www.geeksforgeeks.org/karatsuba-algorithm-in-python/)
* [Algoritmo Karatsuba - Tutorials Point](https://www-tutorialspoint-com.translate.goog/data_structures_algorithms/karatsuba_algorithm.htm?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)

## Licença
Este projeto está licenciado sob a [LICENÇA](../LICENSE) MIT.
