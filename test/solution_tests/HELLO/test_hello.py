from lib.solutions.HLO.hello_solution import hello
import pytest


class TestHello:

    def test_hello_input_type(self):
        with pytest.raises(TypeError) as exceptInfo:
            hello(2)
        assert "Input parameter is not of string type" in str(exceptInfo.value)

    def test_hello_output_type(self):
        with pytest.raises(TypeError) as exceptInfo:
           message = hello("name")
        assert "Output message is not of string type" in str(exceptInfo.value)


    # @pytest.mark.parametrize(("a", "b"),
    #                          [(1, 2.5),
    #                           ('2', 5),
    #                           (5, 3+2j)])
    # def test_sum_type(self, a, b):
    #     with pytest.raises(ValueError) as exceptInfo:
    #         sum(a, b)
    #     assert "Values not in range or of required type" in str(exceptInfo.value)