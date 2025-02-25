import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)  
    result = numbers.astype(object)  

    result[numbers % 5 == 0] = "buzz"      
    result[numbers % 3 == 0] = "fizz"      
    result[numbers % 15 == 0] = "fizzbuzz"  

    return result.tolist()  

x = FizzBuzz(40, 45)
print("FizzBuzz output:", x)  

assert x[0] == "buzz", f"Expected 'buzz', got {x[0]}"
assert x[1] == 41, f"Expected 41, got {x[1]}"
assert x[5] == "fizzbuzz", f"Expected 'fizzbuzz', got {x[5]}"

print("All tests passed.")
