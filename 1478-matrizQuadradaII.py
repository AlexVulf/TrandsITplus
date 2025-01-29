def generate_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(abs(i - j) + 1)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:3}" for num in row))

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        matrix = generate_matrix(n)
        print_matrix(matrix)
        print()

if __name__ == "__main__":
    main()