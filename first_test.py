import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_adding_calc_correct(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_subtraction_calc_correct(self):
        assert self.calc.subtraction(self, 10, 7) == 3

    def test_division_calc_correct(self):
        assert self.calc.division(self, 4, 2) == 2