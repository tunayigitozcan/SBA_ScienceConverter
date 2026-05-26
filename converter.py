"""ScienceConverter - unit conversion tool."""

KM_PER_MILE = 1.609344


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km / KM_PER_MILE


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * KM_PER_MILE


if __name__ == "__main__":
    print(f"5 km    = {km_to_miles(5):.4f} miles")
    print(f"3 miles = {miles_to_km(3):.4f} km")
