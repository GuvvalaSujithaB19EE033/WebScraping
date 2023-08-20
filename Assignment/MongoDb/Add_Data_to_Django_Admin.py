import pandas as pd
from pymongo import MongoClient
csv_file = 'ans_with_id.csv'
df = pd.read_csv(csv_file)



connection_string = f"mongodb+srv://sujitha1:itbOXQ9KwrqoPY1j@cluster0.ntlnzav.mongodb.net/"

client = MongoClient(connection_string)
db = client['scraped_db']  # Replace 'scraped_db' with your desired database name
collection = db['myapp_candidate']  # Replace 'candidates' with your desired collection name

for index, row in df.iterrows():
    candidate_data = {
        'id': row['id'],
        'Title': row['Title'],
        'Company': row['Company'],
        'Location': row['Location'],
        'Salary': row['Salary'],
        'Description': row['Description']
    }
    collection.insert_one(candidate_data)
client.close()