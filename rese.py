import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['Advanced Checker', 'Basic Checker']
accuracy = [92, 72]
std_dev = [2.0, 8.08]  # Standard deviations from your t-test results

# Create x-axis values
x = np.arange(len(groups))

# Create figure
plt.figure(figsize=(8, 6))

# Plot line graph with markers
plt.plot(x, accuracy, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8, label='Accuracy')

# Add error bars
plt.errorbar(x, accuracy, yerr=std_dev, fmt='o', color='red', capsize=5, label='Standard Deviation')

# Customize the plot
plt.title('Password Checker Performance Comparison', fontsize=14, pad=20)
plt.xlabel('Password Checker Type', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.xticks(x, groups)
plt.ylim(60, 100)  # Set y-axis limits
plt.grid(True, linestyle='--', alpha=0.7)

# Add value labels above points
for i, acc in enumerate(accuracy):
    plt.text(x[i], acc + 2, f'{acc}%', ha='center', va='bottom', fontsize=11)

# Add legend
plt.legend(loc='lower right')

# Adjust layout
plt.tight_layout()

# Save and show
plt.savefig('password_checker_comparison.png', dpi=300)
plt.show()