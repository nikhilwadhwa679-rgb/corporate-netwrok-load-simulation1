import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from scipy.integrate import odeint

st.title("🦠 Community Flu Outbreak Simulation (SIR Model)")

# --- User Inputs ---
population = st.number_input("Total Population", value=1000)
initial_infected = st.number_input("Initial Infected", value=10)
initial_recovered = st.number_input("Initial Recovered", value=0)

beta = st.slider("Infection Rate (β)", 0.0, 1.0, 0.3)
gamma = st.slider("Recovery Rate (γ)", 0.0, 1.0, 0.1)

vaccination_rate = st.slider("Vaccination Rate", 0.0, 0.5, 0.05)
closure_effect = st.slider("Closure Effect (reduces infection)", 0.0, 1.0, 0.3)

days = st.slider("Simulation Days", 10, 200, 100)

# Adjust infection rate due to closures
effective_beta = beta * (1 - closure_effect)

# Initial values
S0 = population - initial_infected - initial_recovered
I0 = initial_infected
R0 = initial_recovered

# Time grid
t = np.linspace(0, days, days)

# SIR model with vaccination
def sir_model(y, t, beta, gamma, vaccination_rate):
    S, I, R = y
    dSdt = -beta * S * I / population - vaccination_rate * S
    dIdt = beta * S * I / population - gamma * I
    dRdt = gamma * I + vaccination_rate * S
    return [dSdt, dIdt, dRdt]

# Solve ODE
solution = odeint(sir_model, [S0, I0, R0], t, args=(effective_beta, gamma, vaccination_rate))
S, I, R = solution.T

# --- Plot ---
fig, ax = plt.subplots()
ax.plot(t, S, label="Susceptible")
ax.plot(t, I, label="Infected")
ax.plot(t, R, label="Recovered")
ax.set_xlabel("Days")
ax.set_ylabel("Population")
ax.legend()

st.pyplot(fig)