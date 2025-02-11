import sys

def knapsack(n, p, orders):
    dp = [[0] * (p + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        time, pizzas = orders[i - 1]
        for j in range(p + 1):
            if pizzas > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - pizzas] + time)
    
    return dp[n][p]

def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        
        p = int(sys.stdin.readline().strip())
        orders = []
        
        for _ in range(n):
            time, pizzas = map(int, sys.stdin.readline().split())
            orders.append((time, pizzas))
        
        result = knapsack(n, p, orders)
        print(f"{result} min.")

if __name__ == "__main__":
    main()
