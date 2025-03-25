import time

def max_min_select(arr, left, right):
    """
    Função recursiva que encontra o maior e menor elemento de um array usando divisão e conquista
    """
    if left == right:
        return (arr[left], arr[right])
    
    if right == left + 1:
        if arr[left] < arr[right]:
            return (arr[left], arr[right])
        else:
            return (arr[right], arr[left])
    
    mid = (left + right) // 2
    left_min, left_max = max_min_select(arr, left, mid)
    right_min, right_max = max_min_select(arr, mid + 1, right)
    
    global_min = left_min if left_min < right_min else right_min
    global_max = left_max if left_max > right_max else right_max
    
    return (global_min, global_max)

def find_max_min(arr):
    """Função wrapper para inicializar a chamada recursiva"""
    if not arr:
        return (None, None)
    return max_min_select(arr, 0, len(arr) - 1)

def input_list():
    """Função para receber a lista de números do usuário via terminal"""
    print("Digite os números separados por espaços (ex: 10 5 8 3 22):")
    input_str = input().strip()
    
    try:
        return list(map(float, input_str.split()))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números separados por espaços.")
        return None

if __name__ == "__main__":
    numbers = None
    while numbers is None:
        numbers = input_list()
    
    # Medição do tempo de execução
    start_time = time.time()
    min_val, max_val = find_max_min(numbers)
    end_time = time.time()
    
    # Convertendo para milissegundos
    execution_time = (end_time - start_time) * 1000
    
    print("\nResultado:")
    print(f"Lista inserida: {numbers}")
    print(f"Tamanho da lista: {len(numbers)} elementos")
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
    print(f"\nTempo de execução do algoritmo MaxMin: {execution_time:.6f} milissegundos")
    
    # Comparação com funções nativas
    start_native = time.time()
    native_min = min(numbers)
    native_max = max(numbers)
    end_native = time.time()
    native_time = (end_native - start_native) * 1000
    
    print("\nComparação com funções nativas:")
    print(f"Tempo das funções min/max do Python: {native_time:.6f} milissegundos")
    print(f"Diferença: {abs(execution_time - native_time):.6f} ms")