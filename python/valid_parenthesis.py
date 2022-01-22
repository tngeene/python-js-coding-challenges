"""
Write a function that takes a string of parentheses,
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, 
and false if it's invalid.
"""


def valid_parentheses(string: str) -> bool:
    counter = 0

    for character in string:
        if character == '(': counter += 1    
        if character == ')': counter -= 1
        if counter < 0: return False 
              
    return True if counter == 0 else False

dummy_string = ')test'
dummy_string_2 = 'hi(hi)()'

valid_parentheses(dummy_string)
valid_parentheses(dummy_string_2)
