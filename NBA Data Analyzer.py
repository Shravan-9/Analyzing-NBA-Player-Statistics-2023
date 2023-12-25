# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nba_data = pd.read_csv(r'YOUR DATA FILE PATH')


# Drop Players with missing Values
nba_data = nba_data.dropna()

# Create a new coloumn for points 'PPG' (Points Per Game)
nba_data['PPG'] = nba_data['PTS'] / nba_data['GP']
nba_data['RPG'] = nba_data['REB'] / nba_data['GP']
nba_data['APG'] = nba_data['AST'] / nba_data['GP']


# Create a new column 'New_POS' with updated positions
nba_data['New_POS'] = np.where(nba_data['POS'].isin(['F']), np.random.choice(['SF', 'PF'], size=len(nba_data)), nba_data['POS'])
nba_data['New_POS'] = np.where(nba_data['POS'].isin(['G']), np.random.choice(['SG', 'PG'], size=len(nba_data)), nba_data['New_POS'])

# Create a figure with two rows and two columns
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Plotting the histogram for Points
nba_data['PPG'].plot.hist(ax=axes[0, 0], color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribution of Points in 2023')
axes[0, 0].set_xlabel('Points per Game')
axes[0, 0].set_ylabel('Frequency')

# Plotting the bar chart for Updated Positions (New_POS)
nba_data['New_POS'].value_counts().plot(kind='bar', ax=axes[0, 1], color='lightcoral', edgecolor='black')
axes[0, 1].set_title('Distribution of Positions in 2023')
axes[0, 1].set_xlabel('Positions')
axes[0, 1].set_ylabel('Frequency')

# Plotting the histogram for Assists
nba_data['APG'].plot.hist(ax=axes[1, 0], color='deepskyblue', edgecolor='black')
axes[1, 0].set_title('Distribution of Assists in 2023')
axes[1, 0].set_xlabel('Assists Per Game')
axes[1, 0].set_ylabel('Frequency')

# Plotting the histogram for Rebounds
nba_data['RPG'].plot.hist(ax=axes[1, 1], color='coral', edgecolor='black')
axes[1, 1].set_title('Distribution of Rebounds in 2023')
axes[1, 1].set_xlabel('Rebound Per Game')
axes[1, 1].set_ylabel('Frequency')

# Calculate average PPG, RPG, APG
average_ppg = nba_data['PPG'].sum() / len(nba_data)
average_rpg = nba_data['RPG'].sum() / len(nba_data)
average_apg = nba_data['APG'].sum() / len(nba_data)
average_gp = nba_data['GP'].sum() / len(nba_data)


# Display the results
print(f"The Average NBA Player Averages:")
print(f"Average Points Per Game (PPG): {average_ppg:.1f}")
print(f"Average Rebounds Per Game (RPG): {average_rpg:.1f}")
print(f"Average Assists Per Game (APG): {average_apg:.1f}")
print(f"Average Games Played Per Game (AGP): {average_gp:.1f}")


# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()




