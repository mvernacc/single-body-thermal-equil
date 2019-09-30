"""Unit tests for equilibrium_temperature."""
import pytest
from pytest import approx
from single_body_thermal_equil import Conductive, Radiative, equilibrium_temperature, demo


def test_single_conductive():
    """Test a single conductive boundary."""
    ### Setup ###
    T_1 = 300
    cond = Conductive(T_1, 1.)

    ### Action ###
    T_eq = equilibrium_temperature((cond,))

    ### Verification ###
    assert T_1 == approx(T_eq)


def test_single_radiative():
    """Test a single radiative boundary."""
    ### Setup ###
    T_1 = 300
    cond = Radiative(T_1, 1.)

    ### Action ###
    T_eq = equilibrium_temperature((cond,))

    ### Verification ###
    assert T_1 == approx(T_eq)


def test_two_conductive():
    """Test two conductive boundaries."""
    ### Setup ###
    T_1 = 300.
    T_2 = 600.
    cond_1 = Conductive(T_1, 1.)
    cond_2 = Conductive(T_2, 1.)

    ### Action ###
    T_eq = equilibrium_temperature((cond_1, cond_2))

    ### Verification ###
    T_correct = (T_1 + T_2) / 2
    assert T_eq == approx(T_correct)


def test_value_error():
    """Should raise a value error for bogus input."""
    with pytest.raises(ValueError):
        equilibrium_temperature(('foo', 'bar'))


def test_demo():
    """Demo should run without errors."""
    T_ingot = demo()
    assert T_ingot == approx(1268., rel=1e-3)

