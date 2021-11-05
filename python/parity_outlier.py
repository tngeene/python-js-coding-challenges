def find_outlier(integers):
    ''' 
    You are given an array (which will have a length of at least 3, 
    but could be very large) containing integers. The array is either 
    entirely comprised of odd integers or entirely comprised of even 
    integers except for a single integer N. Write a method that takes 
    the array as an argument and returns this "outlier" N.
    '''
    even_numbers = []
    odd_numbers = []
    outlier = None
    for integer in integers:
        if (integer % 2) == 0:
            even_numbers.append(integer)
        else:
            odd_numbers.append(integer)
    if len(even_numbers) == 1:
        outlier = even_numbers[0]
    elif len(odd_numbers) == 1:
        outlier = odd_numbers[0]
    return outlier

integers = [2, 4, 0, 100, 4, 11, 2602, 36]

find_outlier(integers)


# this solution initiates 2 empty lists, one of even and 
# one with odd  numbers. It then iterates through the list and appends
# to the relevant list. If a list's length is 1, then it's assumed the outlier
# resides in it, hence all we need is access the 0 index of that list and get the 
# first element in it, which is the outlier.
