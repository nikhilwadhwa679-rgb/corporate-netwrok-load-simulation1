import numpy as np
import matplotlib.pyplot as plt

# Taking inputs from the user
N = int(input("Enter total population (N): "))
S = int(input("Enter initial susceptible population (S): "))
I = int(input("Enter initial infected population (I): "))
R = int(input("Enter initial recovered population (R): "))

beta = float(input("Enter infection rate (beta): "))
gamma = float(input("Enter recovery rate (gamma): "))
v = float(input("Enter vaccination rate (v): "))

days = int(input("Enter number of days to simulate: "))

# Lists to store results
S_list = []
I_list = []
R_list = []

# Simulation loop
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
