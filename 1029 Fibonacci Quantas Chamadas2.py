valores_fibonacci = [-1 for _ in range(40)]
contagem_chamadas = [-1 for _ in range(40)]

valores_fibonacci[0] = 0
valores_fibonacci[1] = 1

contagem_chamadas[0] = 1
contagem_chamadas[1] = 1

def calcular_fibonacci(n):
    if valores_fibonacci[n] == -1:
        valor1, chamadas1 = calcular_fibonacci(n - 1)
        valor2, chamadas2 = calcular_fibonacci(n - 2)

        valores_fibonacci[n] = valor1 + valor2
        contagem_chamadas[n] = chamadas1 + chamadas2 + 1

    return (valores_fibonacci[n], contagem_chamadas[n])

num_testes = int(input())

for _ in range(num_testes):
    numero = int(input())
    resultado, num_chamadas = calcular_fibonacci(numero)
    print(f'fib({numero}) = {num_chamadas - 1} calls = {resultado}')