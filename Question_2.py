n = int(input())

for i in range(n):
    c = 0
    n, k = list(map(int, input().split()))
    heights = list(map(int, input().split()))

    for i in heights:
        if i > k:
            c += 1

    print(c)

