n = int(input())

for _ in range(n):
    frase = input()
    palavras = frase.split()
    palavras_ordenadas = sorted(palavras, key=len, reverse=True)
    print(" ".join(palavras_ordenadas))
