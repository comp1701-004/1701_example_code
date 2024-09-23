import math

number = 100

counter = 1
result = math.sqrt(12)

while counter < number:
    term = math.sqrt(12) / ((-3)**counter * (2*counter+1))
    result = result + term
    counter = counter + 1

print(result)