# Knapsack problem with DP repeating items with fractioning not allowed

def knapsack(itemValue, itemWeight, capacity):
    value = list()
    for w in range(capacity):
        value.append(0)
        for i in range(len(itemWeight)):
            if itemWeight[i] <= w:
                val = value[w - itemWeight[i]] + itemValue[i]
                if val > value[w]:
                   value[w] = val
    return value[w]

# capacity = 7
# itemWeight = [3, 2, 5, 4]
# itemValue = [30, 20, 10, 55]
# print(knapsack(itemValue, itemWeight, capacity))
# ---------------------------------------------------------------------------------

#Knapsack problem using DP, repetition of items not allowed with fractioning not allowed
def knapsackNoRepetition(itemValue, itemWeight, capacity):
    rows, cols = (len(itemWeight), capacity)
    value = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(len(itemValue)):
        for w in range(capacity):
            value[i][w] = value[i -1][w]
            if itemWeight[i] <= w:
                val = value[i-1][w - itemWeight[i]] + itemValue[i]
                if val > value[i][w]:
                    value[i][w] = val
    return value[i][w]
# ---------------------------------------------------------------------------------------


capacity = 7
itemWeight = [3, 2, 5, 4]
itemValue = [30, 20, 10, 55]
print(knapsackNoRepetition(itemValue, itemWeight, capacity))
