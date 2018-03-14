f = lambda x, y : x + y
result=f(1,1)
print(result)

#r=map(func,seq)
def getSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(getSquare, numbers)
print(result)
numbersSquare = list(result)
print(numbersSquare)

#lambda
numbers = (4,3,2,1)
result = map(lambda x: x*x, numbers)
print(result)
numbersSquare = set(result)
print(numbersSquare)

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))