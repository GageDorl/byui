from compound_interest import final_value 
import pytest
def test_final_value():
    fv = final_value(100,.08,9,12)
    assert fv == pytest.approx(204.95,abs=0.005)

pytest.main(["-v", "--tb=line", "-rN", __file__])
