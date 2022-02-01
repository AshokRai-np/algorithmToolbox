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

capacity = 7
itemWeight = [3, 2, 5, 4]
itemValue = [30, 20, 10, 55]
print(knapsack(itemValue, itemWeight, capacity))