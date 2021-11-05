import string
from fractions import Fraction
def printer_errors(s):
    allowed_string_characters = string.ascii_lowercase

    # if len(s) >= 1
    print(allowed_string_characters)
    allowed_color_characters = ('a', 'b', 'c', 'd', 'e', 'f',
                          'g', 'h', 'i', 'j', 'k', 'l', 'm', )
    numerator = 0
    denominator = 0

    for i, letter in enumerate(s):
        processed_letter = letter.lower()
        if processed_letter not in allowed_color_characters:
            numerator += 1
    denominator = len(s)
    rational = numerator / denominator
    print(Fraction(3048590516989259, 18014398509481984), rational)
    return Fraction(rational)

# change to anything set of characters
string_to_evaluate = "aaaahhyy"
printer_errors(string_to_evaluate)