import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish)  
    result = np.full(numbers.shape, '', dtype=object) 
    
    result[numbers % 3 == 0] = 'fizz'
    result[numbers % 5 == 0] = 'buzz'
    result[numbers % 15 == 0] = 'fizzBuzz'

    mask = result == ''
    result[mask] = numbers[mask].astype(str)

    return result

start = 91
finish = 106  
print("\n".join(FizzBuzz(start, finish)))

myEmptyList = []
for i in range(91, 105):
    myEmptyList.append(i)
    
print(myEmptyList)  
