
#3.  Write a Python function to check whether a string is pangram or not.

def is_pangram(text):
    # Create a set of unique letters in the text
    letters = set(char.lower() for char in text if char.isalpha())
    
    # Check if the set of letters contains all 26 letters of the alphabet
    return len(letters) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Pack my box with five dozen liquor jugs"))  
print(is_pangram("Hello, world!")) 