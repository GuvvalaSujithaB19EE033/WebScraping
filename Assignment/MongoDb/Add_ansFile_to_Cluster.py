import pandas as pd
from pymongo import MongoClient
csv_file = 'ans.csv'
df = pd.read_csv(csv_file)

username = 'sujitha1'
password = 'itbOXQ9KwrqoPY1j'
cluster_url = 'cluster0'

connection_string = f"mongodb+srv://sujitha1:itbOXQ9KwrqoPY1j@cluster0.ntlnzav.mongodb.net/"

client = MongoClient(connection_string)
db = client['scraped_db']  # Replace 'scraped_db' with your desired database name
collection = db['candidates']  # Replace 'candidates' with your desired collection name

for index, row in df.iterrows():
    candidate_data = {
        'Title': row['Title'],
        'Company': row['Company'],
        'Location': row['Location'],
        'Salary': row['Salary'],
        'Description': row['Description']
    }
    collection.insert_one(candidate_data)
client.close()