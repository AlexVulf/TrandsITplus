import sys
import math

def count_anagrams(s):
    return math.factorial(len(s))

def main():
    for line in sys.stdin:
        s = line.strip()
        if s == "0":
            break
        print(count_anagrams(s))

if __name__ == "__main__":
    main()
