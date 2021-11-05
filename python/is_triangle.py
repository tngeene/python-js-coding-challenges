def is_triangle(a, b, c):
    """
    Implement a function that accepts 3 integer values a, b, c. 
    The function should return true if a triangle can be built 
    with the sides of given length and false in any other case.
    (In this case, all triangles must have surface greater than 0 to be accepted).  
    """
    # use the triangle inequality theorem

    if ((a + b > c) and (b + c > a) and (a + c > b)):
        return True
    return False