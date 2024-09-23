import pandas as pd
import matplotlib.pyplot as plt

# Load the new data
new_data = pd.read_csv('simulation_results3.csv') 

# Set up the plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot E[N] vs Utilization for the new data
ax1.plot(new_data['Utilization'], new_data['E[N]'])
ax1.set_title('E[N] vs Utilization (p) - New Data')
ax1.set_xlabel('Utilization (p)')
ax1.set_ylabel('E[N]')
ax1.grid(True)

# Plot P_IDLE vs Utilization for the new data
ax2.plot(new_data['Utilization'], new_data['P_IDLE'])
ax2.set_title('P_IDLE vs Utilization (p) - New Data')
ax2.set_xlabel('Utilization (p)')
ax2.set_ylabel('P_IDLE (%)')
ax2.grid(True)

# Adjust layout
plt.tight_layout()

# Save the plots as images
fig.savefig('plots.png')  # Saves both plots to an image file
