#Sum of three integers. However if two values are equal sum will be zero

a,b,c = map(int, input('Enter three number: ').split())

def sum(a,b,c):
    sum = a + b + c
    if a == b or a == c or b ==c:
        return 0
    else:
        return sum

print(sum(a,b,c))