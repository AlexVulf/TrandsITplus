def ordenar_por_tamanho(frases):
    for frase in frases:
        palavras = frase.split()
        palavras.sort(key=len, reverse=True)
        print(" ".join(palavras))

if __name__ == "__main__":
    n = int(input().strip())
    frases = [input().strip() for _ in range(n)]
    ordenar_por_tamanho(frases)
