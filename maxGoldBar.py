def maxGoldBars(goldWeight, capacity):
    bars = len(goldWeight)
    rows, cols = (bars, capacity)
    sol = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(bars):
        for c in range(capacity):
            sol[i][c] = sol[i-1][c]
            if goldWeight[i] <= c:
                weight = sol[i-1][c-goldWeight[i]] + goldWeight[i]
                if weight > sol[i][c]:
                    sol[i][c] = weight
    return sol[i][c]

capacity, n = map(int, input().split())
goldWeight = list(map(int, input().split()))
# print(capacity, n)
print(maxGoldBars(goldWeight, capacity+1))