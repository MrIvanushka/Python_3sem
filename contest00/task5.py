def ScoreSum(value):
    sum = 0
    while value > 0:
        sum += value % 10
        value //= 10
    return sum

Value = int(input())

while Value > 9:
    Value = ScoreSum(Value)

print(Value)