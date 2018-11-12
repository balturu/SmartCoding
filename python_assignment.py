# Adds two numbers together

def add(a, b):
    print('Adding two numbers: '+ str(a) +', '+ str(b))
    added = a + b
    return added

assert add(1,3) == 4
assert add(4,6) == 10

# Data structure

numbers = [1,2,3,5]

def sum(listOfNumbers):
    print('Finding sum of the values in the list')
    sum = 0
    for value in listOfNumbers:
        sum = sum + value
    return sum

assert sum(numbers) == 11
assert sum([100, 200]) == 300
