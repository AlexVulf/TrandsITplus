def buscar_capacidade(cidades, origem, destino, passageiros):
    
    fila = [(origem, passageiros)]
    visitadas = set()

    while fila:
        cidade_atual, capacidade_restante = fila.pop(0)
        if cidade_atual == destino:
            return capacidade_restante
        if cidade_atual not in visitadas:
            visitadas.add(cidade_atual)
            for proxima_cidade, capacidade_voo in cidades[cidade_atual]:
                if proxima_cidade not in visitadas and capacidade_voo >= capacidade_restante:
                    fila.append((proxima_cidade, min(capacidade_restante, capacidade_voo)))
    return 0

def processar_instancia():
    m = int(input())
    if m == 0:
        return False
    
    origens = []
    for _ in range(m):
        cidade, passageiros = input().split()
        origens.append((cidade, int(passageiros)))
    
    n, destino = input().split()
    n = int(n)

    cidades = {}
    for _ in range(n):
        cidade1, cidade2, assentos = input().split()
        assentos = int(assentos)
        
        if cidade1 not in cidades:
            cidades[cidade1] = []
        if cidade2 not in cidades:
            cidades[cidade2] = []
        
        cidades[cidade1].append((cidade2, assentos))
        cidades[cidade2].append((cidade1, assentos))

    for cidade_origem, num_passageiros in origens:
        capacidade = buscar_capacidade(cidades, cidade_origem, destino, num_passageiros)
        if capacidade < num_passageiros:
            return True
    
    return False

def main():
    instancias = 1
    while True:
        if not processar_instancia():
            break

        print(f"Instancia {instancias}")
        print("viavel" if not processar_instancia() else "inviavel")
        print()
        
        instancias += 1

if __name__ == "__main__":
    main()
