"""
Shipping Logistics Rate Calculator
Starter code to calculate shipping rates based on weight, distance, and service level.

Licensed under the Apache License 2.0.
"""

# Base rates per service level
SERVICE_RATES = {
    "standard": {"base": 5.00, "per_kg": 1.50, "per_km": 0.05},
    "express": {"base": 10.00, "per_kg": 2.50, "per_km": 0.08},
    "overnight": {"base": 20.00, "per_kg": 4.00, "per_km": 0.12},
}


def calculate_shipping_rate(weight_kg, distance_km, service="standard"):
    """Return the shipping cost for a package."""
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than 0.")
    if distance_km <= 0:
        raise ValueError("Distance must be greater than 0.")
    if service not in SERVICE_RATES:
        raise ValueError(f"Unknown service. Choose from: {', '.join(SERVICE_RATES)}")

    rate = SERVICE_RATES[service]
    cost = rate["base"] + (weight_kg * rate["per_kg"]) + (distance_km * rate["per_km"])
    return round(cost, 2)


def main():
    print("=== Shipping Logistics Rate Calculator ===")
    try:
        weight = float(input("Package weight (kg): "))
        distance = float(input("Shipping distance (km): "))
        service = input("Service level (standard/express/overnight): ").strip().lower()

        cost = calculate_shipping_rate(weight, distance, service)
        print(f"\nEstimated shipping cost: ${cost:.2f}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
