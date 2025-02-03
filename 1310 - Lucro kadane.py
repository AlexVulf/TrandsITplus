import sys

def max_profit(n, cost_per_day, revenues):
    max_ending_here = 0
    max_so_far = 0
    
    for revenue in revenues:
        profit = revenue - cost_per_day  # Lucro do dia após o custo
        max_ending_here = max(profit, max_ending_here + profit)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        
        n = int(line)  # Número de dias
        cost_per_day = int(sys.stdin.readline().strip())  # Custo por dia
        revenues = [int(sys.stdin.readline().strip()) for _ in range(n)]  # Lista de receitas

        print(max_profit(n, cost_per_day, revenues))  # Exibe o resultado
except EOFError:
    pass
