#2. Write a Python function that checks whether a word or phrase is palindrome or not.  
def is_palindrome(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text.lower() if char.isalnum())
    
    # Check if the cleaned text is the same as its reverse
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("nurses run"))  
print(is_palindrome("hello"))  