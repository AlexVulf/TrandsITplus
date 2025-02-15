from collections import deque

def can_reach_destination(origem, passageiros, destino, voos):
    fila = deque([(origem, passageiros)])
    visitadas = set()
    
    while fila:
        cidade_atual, pass_restantes = fila.popleft()
        
        if cidade_atual == destino:
            return True
            
        if cidade_atual not in visitadas:
            visitadas.add(cidade_atual)
            if cidade_atual in voos:
                for proxima_cidade, capacidade in voos[cidade_atual]:
                    if capacidade >= pass_restantes and proxima_cidade not in visitadas:
                        fila.append((proxima_cidade, pass_restantes))
    
    return False

def main():
    instancia = 1
    
    while True:
        m = int(input())
        if m == 0:
            break
        
        origens = []
        for _ in range(m):
            cidade, passageiros = input().split()
            origens.append((cidade, int(passageiros)))
        
        n, destino = input().split()
        n = int(n)
        
        voos = {}
        for _ in range(n):
            cidade1, cidade2, assentos = input().split()
            assentos = int(assentos)
            
            if cidade1 not in voos:
                voos[cidade1] = []
            if cidade2 not in voos:
                voos[cidade2] = []
            
            voos[cidade1].append((cidade2, assentos))
            voos[cidade2].append((cidade1, assentos))
        
        viavel = True
        for cidade_origem, num_passageiros in origens:
            if not can_reach_destination(cidade_origem, num_passageiros, destino, voos):
                viavel = False
                break
        
        print(f"Instancia {instancia}")
        print("viavel" if viavel else "inviavel")
        print()
        
        instancia += 1

if __name__ == "__main__":
    main()