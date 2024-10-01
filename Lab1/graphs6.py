import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('simulation_results6.csv')

# Unique buffer sizes
buffer_sizes = data['Buffer Size'].unique()

# Create subplots for P_IDLE and P_LOSS
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Plot P_IDLE
for buffer_size in buffer_sizes:
    subset = data[data['Buffer Size'] == buffer_size]
    axs[0].plot(subset['Utilization'], subset['P_IDLE'], label=f'Buffer Size {buffer_size}')
axs[0].set_title('P_IDLE vs Utilization')
axs[0].set_xlabel('Utilization')
axs[0].set_ylabel('P_IDLE')
axs[0].legend()
axs[0].grid()

# Plot P_LOSS
for buffer_size in buffer_sizes:
    subset = data[data['Buffer Size'] == buffer_size]
    axs[1].plot(subset['Utilization'], subset['P_LOSS'], label=f'Buffer Size {buffer_size}')
axs[1].set_title('P_LOSS vs Utilization')
axs[1].set_xlabel('Utilization')
axs[1].set_ylabel('P_LOSS')
axs[1].legend()
axs[1].grid()

# Save the figure as an image
plt.tight_layout()
plt.savefig('simulation_results_plot.png')
plt.show()
