import pandas as pd

# Read the CSV file
csv_file = 'ans.csv'
df = pd.read_csv(csv_file)

# Add an 'id' column with incremental values starting from 1
df.insert(0, 'id', range(1, 1 + len(df)))

# Write the modified data back to the CSV file
df.to_csv('ans_with_id.csv', index=False)

print("id column added to CSV successfully.")