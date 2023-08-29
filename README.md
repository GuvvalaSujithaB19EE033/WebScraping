# WebScraping

This repository contains my assignment on web scraping, where I extracted job listings for the keyword "Python developer" from Indeed.com.

## Folders

The `Assignment` folder is organized into three subfolders:

### 1. Web_Scraping

In the `Web_Scraping` folder, you'll find the code used for scraping job listings from Indeed.com. The main script is `scraping.py`.

#### scraping.py

This Python script uses Selenium and BeautifulSoup to scrape job listings from Indeed.com. It searches for "Python developer" job listings, extracts relevant information, and saves the data to a ans.csv file.

### 2. MongoDb

In the `MongoDb` folder, you'll find the code related to storing the scraped data in a MongoDB database and integrating it with Django Admin.

#### Add_ansFile_to_Cluster.py

This Python script connects to your MongoDB cluster and reads the `ans.csv` file containing the scraped job listings. It then adds this data to the `scraped_db` database.

#### Add_Data_to_Django_Admin.py

This script demonstrates how to integrate the scraped data with the Django Admin panel. It adds the data from the MongoDB collection to the Django models, allowing you to manage and display the job listings using the Django Admin interface.

### 3. Django

In the `Django` folder, you'll find the code related to integrating the scraped data with a Django web application.

#### Project Setup and Integration

1. `myproject`: To work with the MongoDB cluster. Updated the database settings in `settings.py` to connect to the MongoDB cluster.

2. `myapp`: Inside the project, Created an app named `myapp` to handle the integration of the scraped data.

3. `myapp/models.py`: Defined a `Candidates` model to represent the job listings data stored in the MongoDB collection. This model is used to add the scraped data to the Django Admin panel.

4. `myapp/admin.py`: Registered the `Candidates` model with the Django Admin panel so that you can view, edit, and manage the scraped job listings directly from the admin interface.
#### Installations
install asgiref==3.5.0 Django==4.0.3 djongo==1.3.6 dnspython==2.2.1 pykerberos==1.2.4 pymongo==3.12.1 python-snappy==0.6.1 pytz==2022.1 sqlparse==0.2.4

Command to runserver : 'python manage.py runserver' 

Url for admin panel : [127.0.0.1:8000/admin/myapp/candidate](url)

### 4. calculate_average_salary.py

This Python script, located in `myproject/myapp/management/commands`, calculates the average salary for Python developers in city, "Hyderabad." It utilizes the data from the `Candidates` model to perform this calculation.


