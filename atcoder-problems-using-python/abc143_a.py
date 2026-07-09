window, curtain = map(int, input().split())

if 2 * curtain >= window:
    print(0)
else:
    rem = window - (2 * curtain)
    print(rem)