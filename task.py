import pandas as pd
import matplotlib.pyplot as plt

# Read the data from "Spurs.csv" into a DataFrame
data = pd.read_csv("Spurs.csv")

# Calculate the average goals scored (GF) and goals against (GA)
avg_GF = data['GF'].mean()
avg_GA = data['GA'].mean()

# Sort the days of the week in the correct order
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data['Day'] = pd.Categorical(data['Day'], categories=weekdays, ordered=True)

# Create a figure with subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the goals scored (GF) and goals against (GA) together
data.plot(x='Round', y=['GF', 'GA'], kind='bar', ax=axes[0])
axes[0].set_xlabel('Round')
axes[0].set_ylabel('Goals')
axes[0].set_title('Goals Scored (GF) and Goals Against (GA)')
axes[0].legend(['Goals Scored (GF)', 'Goals Against (GA)'])

# Add text with average GF and GA inside the first subplot
axes[0].text(0.05, 0.95, f"Average GF: {avg_GF:.2f}", transform=axes[0].transAxes, fontsize=10)
axes[0].text(0.05, 0.85, f"Average GA: {avg_GA:.2f}", transform=axes[0].transAxes, fontsize=10)

# Plot a bar chart of the number of matches played on each day (sorted correctly)
data['Day'].value_counts().loc[weekdays].plot(kind='bar', ax=axes[1])
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Count')
axes[1].set_title('Number of Matches Played on Each Day')

# Adjust the spacing between subplots
plt.tight_layout()

plt.show()
