t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    dicionario = {}
    
    for _ in range(m):
        palavra_japones = input()
        traducao = input()
        dicionario[palavra_japones] = traducao
    
    for _ in range(n):
        linha = input()
        palavras = linha.split()
        nova_linha = []
        
        for palavra in palavras:
            if palavra in dicionario:
                nova_linha.append(dicionario[palavra])
            else:
                nova_linha.append(palavra)
        
        print(" ".join(nova_linha))
    
    print()
