

def sum(a, b):
    """In order to complete the round you need to implement the following method:
         sum(Integer, Integer) -> Integer

    Where:
     - param[0] = a positive integer between 0-100
     - param[1] = a positive integer between 0-100
     - @return = an Integer representing the sum of the two numbers"""
    if a not in range(0, 100) or b not in range(0, 100) or type(a) is not int or type(b) is not int:
        raise ValueError("Values not in range or of required type")

    return a+b