def fibonacci(n, call_count):
    if n == 0:
        return 0, call_count + 1
    elif n == 1:
        return 1, call_count + 1
    else:

        result1, call_count = fibonacci(n-1, call_count)
        result2, call_count = fibonacci(n-2, call_count)
        return result1 + result2, call_count

def solve():
    N = int(input())
    for _ in range(N):
        X = int(input())

        result, calls = fibonacci(X, 0)
        print(f"fib({X}) = {calls} calls = {result}")

solve()