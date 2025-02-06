from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.1)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(.048692, 0, .018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 200, .018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 200, .018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 200, .018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 1000, .013, 1.65) == approx(-362.778, abs=0.001)
    assert pressure_loss_from_pipe(.048692, 1800.75, .013, 1.65) == approx(-653.272, abs=0.001)

pytest.main(['-v','--tb=line','-rN',__file__])