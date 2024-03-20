

import os
import pandas as pd
import matplotlib.pyplot as plt

# Directory where your CSV files are located
directory = '/Users/krishthakkar/Documents/Spring 24/SA/safe data scrape/safe logs'

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through all CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Read the CSV file into a DataFrame
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)

        # Append the DataFrame to data_frames list
        data_frames.append(df)

# Combine all DataFrames into a single DataFrame
combined_data = pd.concat(data_frames, ignore_index=True)

# Convert 'Amount' column to numeric
combined_data['Amount'] = pd.to_numeric(combined_data['Amount'], errors='coerce')

# Group by 'Account' and sum the 'Amount' for each account
account_summary = combined_data.groupby('Account')['Amount'].sum()

# Create a larger figure size for improved readability
plt.figure(figsize=(18, 10))  # Adjust as needed

# Plot the data with enhanced visualization settings

# # Bar chart for money usage by account
# plt.subplot(1, 2, 1)
# account_summary.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title('Money Usage by Account', fontsize=16)
# plt.xlabel('Account', fontsize=14)
# plt.ylabel('Total Amount', fontsize=14)
# plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate labels for better readability
# plt.tick_params(bottom=False)  # Remove ticks for cleaner look

# # Adjust y-axis limits to avoid overlapping bars
# plt.ylim(0, account_summary.max() * 1.1)  # Adjust based on your data 

# Pie chart for breakdown of total amount
plt.subplot(1, 2, 2)
total_amount = account_summary.sum()
account_percentages = (account_summary / total_amount) * 100

# Adjust autopct for label placement and add textprops for smaller font
plt.pie(account_percentages, labels=account_summary.index, autopct='%1.1f%%', startangle=90,
        pctdistance=0.9, textprops={'fontsize': 10})  

# plt.axis('equal')  
# plt.title('Breakdown of Total Amount', fontsize=16)



# Pie chart plot
filtered_values = [v for v in account_percentages if v >= 2]
filtered_labels = [label for label, v in zip(account_summary.index, account_percentages) if v >= 2]
others_sum = 100 - sum(filtered_values)
filtered_values.append(others_sum)
filtered_labels.append('Other (< 2%)')

accounts_less_than_2_percent = [label for label, v in zip(account_summary.index, account_percentages) if v < 2]

# Print the accounts contributing less than 2%
print("Accounts contributing less than 2%:")
for account in accounts_less_than_2_percent:
    print(account)

# Create the pie chart
plt.figure(figsize=(20, 10))
plt.pie(filtered_values, labels=filtered_labels, autopct="%1.1f%%", startangle=90,
        pctdistance=0.9, textprops={'fontsize': 10})
plt.axis('equal')
plt.title('Breakdown of Total Amount', fontsize=16)





# plt.subplot(1, 2, 2)
# total_amount = account_summary.sum()
# account_percentages = (account_summary / total_amount) * 100
# plt.pie(account_percentages, labels=account_summary.index, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink'])
# plt.axis('equal')  # Equal aspect ratio for a circular pie chart
# plt.title('Breakdown of Total Amount', fontsize=16)




# Set legend options and location to avoid overlapping labels
# legend = plt.legend(prop={'size': 12}, loc='upper left', bbox_to_anchor=(1.02, 1))
# for label in legend.get_texts():
#     label.set_text(label.get_text().split('(')[0])  # Truncate long account names in legend

# Adjust layout to prevent overlapping elements
plt.tight_layout()

plt.show()
