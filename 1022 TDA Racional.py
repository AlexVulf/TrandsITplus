from math import gcd

def simplify(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

def operate(n1, d1, op, n2, d2):
    if op == '+':
        num = n1 * d2 + n2 * d1
        den = d1 * d2
    elif op == '-':
        num = n1 * d2 - n2 * d1
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = n2 * d1
    return num, den

def main():
    qtd = int(input())
    
    for _ in range(qtd):
        n1, _, d1, op, n2, _, d2 = input().split()
        n1, d1, n2, d2 = map(int, [n1, d1, n2, d2])
        
        num, den = operate(n1, d1, op, n2, d2)
        simp_num, simp_den = simplify(num, den)
        
        print(f"{num}/{den} = {simp_num}/{simp_den}")

if __name__ == "__main__":
    main()