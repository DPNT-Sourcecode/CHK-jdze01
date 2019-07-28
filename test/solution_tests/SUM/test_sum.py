from solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum_operation(self):
        assert sum_solution(1, 2) == 3

    def test_sum_range(self):
        with pytest.raises(ValueError) as exceptInfo:
            sum_solution(102, 2)
        assert "Values not in range" in str(exceptInfo.value)

    @pytest.mark.parametrize(("a", "b"),
                             [(1, 2.5),
                              ('2', 5),
                              (5, 3+2j)])
    def test_sum_type(self, a, b):
        with pytest.raises(ValueError) as exceptInfo:
            sum_solution('102', 2.5)
        assert "Input values are not of required type" in str(exceptInfo.value)

