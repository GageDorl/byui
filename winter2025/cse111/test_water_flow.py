from pytest import approx
import pytest

from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, kPa_to_psi

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

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-.306, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(.048692, 0) == approx(0, abs=1)
    assert reynolds_number(.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(.28687, 1.65) == approx(471729, abs=1)
    assert reynolds_number(.28687, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(.28687, 0, 1, .048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(.28687, 1.65, 471729, .048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(.28687, 1.75, 500318, .048692) == approx(-184.182, abs=0.001)

def test_kPa_to_psi():
    assert kPa_to_psi(0) == approx(0, abs=0.1)
    assert kPa_to_psi(100) == approx(14.5, abs=0.1)
    assert kPa_to_psi(200) == approx(29.0, abs=0.1)
    assert kPa_to_psi(300) == approx(43.5, abs=0.1)
    assert kPa_to_psi(400) == approx(58.0, abs=0.1)

pytest.main(['-v','--tb=line','-rN',__file__])