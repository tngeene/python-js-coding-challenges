from string import punctuation

def pig_it(text):
    """
    Move the first letter of each word to the end of it, 
    then add "ay" to the end of the word. Leave punctuation 
    marks untouched.
    
    """  
    return ' '.join(word[1:] + word[0] + 'ay' if word not in punctuation else word for word in text.split(' '))


    
