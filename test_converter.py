"""Pytest suite for the ScienceConverter unit conversions."""
import math

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    miles_to_km,
)


def test_km_to_miles_one_mile_round_trip():
    # 1.609344 km should be exactly 1 mile
    assert math.isclose(km_to_miles(1.609344), 1.0, rel_tol=1e-9)


def test_miles_to_km_one_mile():
    assert math.isclose(miles_to_km(1), 1.609344, rel_tol=1e-9)


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius_freezing():
    assert fahrenheit_to_celsius(32) == 0


def test_fahrenheit_to_celsius_boiling():
    assert fahrenheit_to_celsius(212) == 100
