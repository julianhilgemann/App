import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Define the slider
slider = st.slider("Number of samples", 0, 10000, 100)

# Generate a random sample from a standard normal distribution
samples = np.random.normal(0, 1, slider)

plt.style.use('dark_background')  # Set the style to dark mode

fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Plot the KDE plot
sns.kdeplot(samples, color="white", ax=ax[1])  # KDE with white color

# Plot the theoretical distribution
x = np.linspace(-5, 5, 1000)
ax[1].plot(x, norm.pdf(x, 0, 1), color='red', linestyle='dashed')  # plot the PDF of the standard normal distribution with dashed line
ax[1].grid(True, color='white', linestyle='-', linewidth=0.5)  # Grid with white lines

# Label the second plot
ax[1].set_title('Kernel Density Estimation and Theoretical Normal Distribution', color='white')

# Get the limits of the second plot's axes
xlim = ax[1].get_xlim()
ylim = ax[1].get_ylim()

# Plot the histogram
ax[0].hist(samples, bins=100, density=True, color='white', range=xlim)  # density=True to normalize and range is set to match the second plot
ax[0].grid(True, color='white', linestyle='-', linewidth=0.5)  # Grid with white lines

# Set the limits of the first plot's axes to match the second plot
ax[0].set_xlim(xlim)
ax[0].set_ylim(ylim)

# Label the first plot
ax[0].set_title('Histogram', color='white')

# Display the plot in Streamlit
st.pyplot(fig)
