from DietPlanner import calculate_metabolic_rate, calculate_calories, calculate_protein, calculate_macros
import pytest

def test_calculate_metabolic_rate():
    assert calculate_metabolic_rate('male', 23, 160, 70) == 1727.0
    assert calculate_metabolic_rate('female', 21, 110, 62) == 1217.0

def test_calculate_calories():
    assert calculate_calories(1727, 'sedentary') == 2072.0
    assert calculate_calories(1217, 'lightly active') == 1673.0

def test_calculate_protein():
    assert calculate_protein(160, 'lose') == 160.0
    assert calculate_protein(110, 'maintain') == 99.0

def test_calculate_macros():
    assert calculate_macros(2072, 160) == (160.0, 58.0, 228.0)
    assert calculate_macros(1673, 99) == (99.0, 46.0, 215.0)

pytest.main(["-v", "--tb=line", "test_dietplanner.py"])