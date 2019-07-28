from solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum_operation(self):
        assert sum_solution(1, 2) == 3

    def test_sum_range(self):
        

    #
    #     raise ValueError("Values not in range")
    # elif type(a) is not int or type(b) is not int:
    #     raise ValueError("Input values are not of required type")

