import operator
def Maximum(digits, operators):

    return 0

def parenthesisPlacement(digits, operators):
    digitlength = len(digits)
    maximum = [[0 for i in range(digitlength)] for j in range(digitlength)]
    minimum = [[0 for i in range(digitlength)] for j in range(digitlength)]
    for i in range(len(digits)):
        maximum[i][i] = digits[i]
        minimum[i][i] = digits[i]
    for s in range(1, len(digitlength)):
        for i in range(1, n-s):
            j = i + s
            minimum[i][j] = Minimum()
    print(maximum)
    print(minimum)
    return 0

operators = list()
numbers = list()
digits = list()
s = list(str(input()))
for i in range(len(s)):
    if  i % 2 == 0:
        numbers.append(s[i])
    else:
        operators.append(s[i])
for i in numbers:
    digits.append(int(i))
parenthesisPlacement(digits, operators)
# ops = { "+": operator.add, "-": operator.sub, "*": operator.mul }
# print(ops["+"](1,1))


