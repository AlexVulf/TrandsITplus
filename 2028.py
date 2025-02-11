import sys

def generate_sequence(n):
    sequence = [0]
    for i in range(1, n + 1):
        sequence.extend([i] * i)
    return sequence

def main():
    case_number = 1
    for line in sys.stdin:
        n = int(line.strip())
        sequence = generate_sequence(n)
        print(f"Caso {case_number}: {len(sequence)} {'numero' if len(sequence) == 1 else 'numeros'}")
        print(" ".join(map(str, sequence)))
        print()
        case_number += 1

if __name__ == "__main__":
    main()
