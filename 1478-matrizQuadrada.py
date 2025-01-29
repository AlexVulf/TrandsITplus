while True:
    x = int(input())
    if x == 0:
        break

    for i in range(x):
        for j in range(x):

            if i < x - i - 1:
                distE = i
            else:
                distE = x - i - 1

            if j < x - j - 1:
                distD = j
            else:
                distD = x - j - 1

            dist = min(distE, distD)

            print(f"{dist + 1:3d}", end="")

            if j != x - 1:
                print(end=" ")

        print()

    print()