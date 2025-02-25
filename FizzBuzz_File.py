import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)  
    result = np.full(numbers.shape, '', dtype=object) 
    
    result[numbers % 15 == 0] = 'fizzbuzz'  
    result[numbers % 3 == 0] = 'fizz'
    result[numbers % 5 == 0] = 'buzz'

    mask = result == ''
    result[mask] = numbers[mask]  

    return result.tolist()  

start = 40
finish = 45
print(FizzBuzz(start, finish))  
