"""ScienceConverter - unit conversion tool."""

KM_PER_MILE = 1.609344  # Defined by the international yard agreement (1959)
LB_PER_KG = 2.20462


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km / KM_PER_MILE


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * KM_PER_MILE


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def kg_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg * LB_PER_KG


def pounds_to_kg(lb):
    """Convert pounds to kilograms."""
    return lb / LB_PER_KG


if __name__ == "__main__":
    print(f"5 km          = {km_to_miles(5):.4f} miles")
    print(f"3 miles       = {miles_to_km(3):.4f} km")
    print(f"100 Celsius   = {celsius_to_fahrenheit(100):.2f} Fahrenheit")
    print(f"32 Fahrenheit = {fahrenheit_to_celsius(32):.2f} Celsius")
    print(f"10 kg         = {kg_to_pounds(10):.4f} pounds")
    print(f"22 pounds     = {pounds_to_kg(22):.4f} kg")
