def main():
    num = [0] * 2001
    qtd = int(input())
    
    for _ in range(qtd):
        ent = int(input())
        num[ent] += 1
    
    for cont in range(2001):
        if num[cont] > 0:
            print(f"{cont} aparece {num[cont]} vez(es)")

if __name__ == "__main__":
    main()