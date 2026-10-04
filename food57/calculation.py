# FOOD-57 reproducibility script
# Data source: UK Department for Energy Security and Net Zero (DESNZ),
# Greenhouse gas reporting: conversion factors 2026, "Freighting goods" table.
# https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026
#
# Boundary: TTW (transport-operation emissions). Air freight value includes radiative forcing (RF).

factors = {
    "Small truck (diesel van <=3.5 t)": 0.63511,
    "Semi truck (articulated HGV)": 0.07926,
    "Rail freight": 0.02583,
    "Container ship (average)": 0.01612,
    "Air freight (long-haul, incl. RF)": 0.89939,
}

weight_tonnes = 1
distance_km = 1000

print("1 tonne of food moved 1,000 km:")
for mode, factor in factors.items():
    kg = weight_tonnes * distance_km * factor
    print(f"{mode}: {kg:.2f} kg CO2e")

air_budget = factors["Air freight (long-haul, incl. RF)"] * 100
print("\nDistance each mode can travel for the emissions of 100 km by air:")
for mode, factor in factors.items():
    km = air_budget / factor
    print(f"{mode}: {km:.1f} km")
