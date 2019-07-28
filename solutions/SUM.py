

def sum_solution(a, b):
    """In order to complete the round you need to implement the following method:
         sum(Integer, Integer) -> Integer

    Where:
     - param[0] = a positive integer between 0-100
     - param[1] = a positive integer between 0-100
     - @return = an Integer representing the sum of the two numbers"""
    if a not in range(100) or b not in range(100):
        raise ValueError("Values not in range")
    elif type(a) is not int or type(b) is not int:
        raise ValueError("Input values are not of required type")

    return a+b