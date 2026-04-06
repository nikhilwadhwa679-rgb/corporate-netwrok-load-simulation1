import numpy as np
import matplotlib.pyplot as plt

# Total population
N = 1000

# Initial values
S = 990
I = 10
R = 0

# Parameters
beta = 0.3      # infection rate
gamma = 0.1     # recovery rate
v = 0.05        # vaccination rate

days = 100

S_list = []
I_list = []
R_list = []

for day in range(days):
    new_infected = beta * S * I / N
    new_recovered = gamma * I
    new_vaccinated = v * S

    S = S - new_infected - new_vaccinated
    I = I + new_infected - new_recovered
    R = R + new_recovered + new_vaccinated

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plotting the results
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel("Days")
plt.ylabel("Population")
plt.title("SIR Model with Vaccination")
plt.legend()
plt.show()