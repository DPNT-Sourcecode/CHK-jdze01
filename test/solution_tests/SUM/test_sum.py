from lib.solutions.SUM_R1 import sum
import pytest


class TestSum:
    def test_sum_operation(self):
        assert sum(1, 0) == 1

    def test_sum_range(self):
        with pytest.raises(ValueError) as exceptInfo:
            sum(102, 2)
        assert "Values not in range or of required type" in str(exceptInfo.value)

    def test_sum_range(self):
        with pytest.raises(ValueError) as exceptInfo:
            sum(-1, 2)
        assert "Values not in range or of required type" in str(exceptInfo.value)

    @pytest.mark.parametrize(("a", "b"),
                             [(1, 2.5),
                              ('2', 5),
                              (5, 3+2j)])
    def test_sum_type(self, a, b):
        with pytest.raises(ValueError) as exceptInfo:
            sum(a, b)
        assert "Values not in range or of required type" in str(exceptInfo.value)