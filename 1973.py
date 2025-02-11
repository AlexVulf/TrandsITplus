import sys

def jornada_nas_estrelas(N, carneiros):
    visitados = [False] * N
    i = 0
    
    while 0 <= i < N:
        visitados[i] = True
        
        if carneiros[i] == 0:
            break

        direcao = 1 if carneiros[i] % 2 == 1 else -1

        carneiros[i] -= 1

        i += direcao

    estrelas_atacadas = sum(visitados)
    carneiros_restantes = sum(carneiros)

    return estrelas_atacadas, carneiros_restantes

N = int(sys.stdin.readline().strip())  
carneiros = list(map(int, sys.stdin.readline().strip().split()))  

resultado = jornada_nas_estrelas(N, carneiros)
print(resultado[0], resultado[1])
