import time

def multiply_small(x, y):
    return x * y

def split_number(num, n):
    power = 10 ** (n // 2)
    a = num // power
    b = num % power
    return a, b

def karatsuba(x, y):
    start_time = time.time() # Inicia a contagem de tempo
    
    # Caso base: se x ou y são pequenos, multiplicamos diretamente
    if x < 10 or y < 10:
        result = multiply_small(x, y)
        end_time = time.time() # Finaliza a contagem de tempo
        return result, end_time - start_time

    
    # Determina o número de dígitos
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2
    
    # Divide os números
    a, b = split_number(x, n)
    c, d = split_number(y, n)
    
    # Calcula os produtos
    ac, time_ac = karatsuba(a, c)
    bd, time_bd = karatsuba(b, d)
    ad_bc, time_ad_bc = karatsuba(a + b, c + d)
    ad_bc = ad_bc - ac - bd
    
    # Combina os resultados
    result = ac * 10 ** (2 * n2) + ad_bc * 10 ** n2 + bd
    end_time = time.time() # Finaliza a contagem de tempo
    
    total_time = (end_time - start_time) + time_ac + time_bd + time_ad_bc
    return result, total_time

if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    result, elapsed_time = karatsuba(x, y)
    print(f"Resultado: {result}, Tempo: {elapsed_time:.6f} segundos")