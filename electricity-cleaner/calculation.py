# MY OWN SHOW ME topic: Is U.S. Electricity Actually Getting Cleaner?
# Comparable source: U.S. EPA eGRID summary tables for 2010 and 2023.
#
# eGRID 2010 U.S. CO2 total output emission rate: 1232.35 lb/MWh
# eGRID 2023 U.S. CO2 total output emission rate: 767.2 lb/MWh

rate_2010 = 1232.35
rate_2023 = 767.2

decline = (1 - rate_2023 / rate_2010) * 100
print(f"CO2 output emission rate decline: {decline:.1f}%")

coal_2010 = 44.7748
coal_2023 = 16.1
gas_2010 = 23.9686
gas_2023 = 43.2
wind_solar_2010 = 2.3154
wind_solar_2023 = 13.9

print(f"Coal share: {coal_2010:.1f}% -> {coal_2023:.1f}%")
print(f"Natural gas share: {gas_2010:.1f}% -> {gas_2023:.1f}%")
print(f"Wind + solar share: {wind_solar_2010:.1f}% -> {wind_solar_2023:.1f}%")
