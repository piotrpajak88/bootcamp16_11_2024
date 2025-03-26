import numpy as np

initial_value = 10000
years = 10

annual_return = 0.07
annual_volatility = 0.15
simulations = 1000

np.random.seed(42)

annual_growth_rates = np.random.normal(annual_return, annual_volatility, (years, simulations))
values = initial_value * np.cumprod(1 + annual_growth_rates, axis=0)

print(values)

final_values = values[-1]
print("Średnia wartosc portfela po 10 latach: ", np.mean(final_values))
print("Najlepszy scenariusz: ", np.max(final_values))
print("Najgorszy scenariusz: ", np.min(final_values))
