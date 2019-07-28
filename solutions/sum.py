
def sum_integers(a: int, b: int):
    """In order to complete the round you need to implement the following method:
         sum(Integer, Integer) -> Integer

    Where:
     - param[0] = a positive integer between 0-100
     - param[1] = a positive integer between 0-100
     - @return = an Integer representing the sum of the two numbers"""
    if a not in range(100) or b not in range(100):
        return None

    return a+b


