def count_diamonds(s):
    stack, diamonds = 0, 0
    for char in s:
        if char == '<':
            stack += 1
        elif char == '>' and stack:
            stack -= 1
            diamonds += 1
    return diamonds

def main():
    for _ in range(int(input().strip())):
        print(count_diamonds(input().strip()))

if __name__ == "__main__":
    main()