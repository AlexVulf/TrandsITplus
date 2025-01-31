def process_cartas(n):
    cartas = list(range(1, n + 1))
    descartadas = []
    
    while len(cartas) > 1:
        descartadas.append(cartas.pop(0))  
        cartas.append(cartas.pop(0))  
    
    return descartadas, cartas[0]

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        descartadas, restante = process_cartas(n)
        
        print(f"Discarded cards: {', '.join(map(str, descartadas)) if descartadas else ''}")
        print(f"Remaining card: {restante}")

if __name__ == "__main__":
    main()
