from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from random import randint
from selenium.webdriver.common.by import By

# Assist with creating incremental timing for our scraping to seem more human
from time import sleep

# Initialize Chrome webdriver
driver = webdriver.Chrome()
job_data_list = []
dataframe = pd.DataFrame(columns=['Title','Company' 'Location', 'Salary', 'Description'])

for i in range(0,700,10):
    driver.get('https://in.indeed.com/jobs?q=Python+developer&l=&start='+str(i))
    driver.implicitly_wait(4)
    all_jobs=driver.find_elements(By.CLASS_NAME,'job_seen_beacon')
    job_data = []
    for job in all_jobs:
        result_html=job.get_attribute('innerHTML')
        soup=BeautifulSoup(result_html,'html.parser')
        try:
            title=soup.find("a",class_='jcs-JobTitle css-jspxzf eu4oa1w0').text.replace('\n','')
        except:
            title='None'
        try:
            company=soup.find("span",class_='companyName').text.replace('\n','')
        except:
            company='None'
        #print(title)
        try:
            salary=soup.find("div",class_='salary-snippet-container').text.replace('\n','')
        except:
            salary='None'
        #print(salary)

        try:
            location=soup.find("div",class_='companyLocation').text.replace('\n','')
        except:
            location='None'
        #print(location)
    
        try:
            details=soup.find("div",class_='job-snippet').text.replace('\n','')
        except:
            details='None'
        #print(details)
        job_data_list.append({'Title': title,'Company':company, 'Location': location, 'Salary': salary, 'Description': details})
dataframe = pd.DataFrame(job_data_list)

# Save the DataFrame to a CSV file
dataframe.to_csv('ans.csv', index=False)


   
        

    
