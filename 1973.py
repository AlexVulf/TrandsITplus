def jornada_nas_estrelas(N, carneiros):
    visitados = set()
    i = 0
    
    while 0 <= i < N:
        visitados.add(i)
        
        if carneiros[i] == 0:
            break
        
        carneiros[i] -= 1 
        
        if carneiros[i] % 2 == 0:
            i -= 1
        else:
            i += 1

    estrelas_atacadas = len(visitados)
    carneiros_restantes = sum(carneiros)

    return estrelas_atacadas, carneiros_restantes

N = int(input())
carneiros = list(map(int, input().split()))

resultado = jornada_nas_estrelas(N, carneiros)
print(resultado[0], resultado[1])
