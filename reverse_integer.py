#4. Write a program that takes an integer as input and returns an integer with reversed digit ordering. 

def reverse_digits(num):
    # Convert the number to a string, reverse it, and convert it back to an integer
    return int(str(abs(num))[::-1]) * (-1 if num < 0 else 1)

print(reverse_digits(500))  
print(reverse_digits(-56)) 
print(reverse_digits(-90)) 
print(reverse_digits(91))  
