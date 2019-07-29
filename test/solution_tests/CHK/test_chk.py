from lib.solutions.CHK.checkout_solution import checkout
import pytest


class TestChk:

    @pytest.mark.parametrize(("skus", "total"),
                             [("A B C D", 115),
                              ("3A 2B D", 190),
                              ("2", 15)])
    def test_sum_type(self, skus, total):
        assert checkout(skus) == total





"""
Our price table and offers: 
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+"""