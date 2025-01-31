n = int(input())
lista = []
for i in range(n):
    numero = int(input())
    lista.append(numero)

pares = sorted([num for num in lista if num % 2 == 0])
impares = sorted([num for num in lista if num % 2 != 0], reverse=True)

listaOrdenada = pares + impares
print("\n".join(map(str, listaOrdenada)))