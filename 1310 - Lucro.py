import sys

def max_profit(n, cost_per_day, revenues):
    max_profit = 0  # Inicializa o lucro máximo como 0

    # Testa todos os intervalos de dias
    for start in range(n):
        current_sum = 0  # Soma das receitas no intervalo
        for end in range(start, n):
            current_sum += revenues[end]  # Adiciona a receita do dia atual
            days_count = end - start + 1  # Número de dias no intervalo
            profit = current_sum - (days_count * cost_per_day)  # Calcula o lucro
            max_profit = max(max_profit, profit)  # Atualiza o lucro máximo

    return max_profit

try:
    while True:
        line = sys.stdin.readline().strip()
        if not line:  # Se a linha estiver vazia, finaliza a leitura
            break
        
        n = int(line)  # Número de dias
        cost_per_day = int(sys.stdin.readline().strip())  # Custo por dia
        revenues = [int(sys.stdin.readline().strip()) for _ in range(n)]  # Lista de receitas

        print(max_profit(n, cost_per_day, revenues))  # Exibe o resultado
except EOFError:
    pass