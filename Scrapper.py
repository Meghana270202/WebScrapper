import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
url = 'https://catalog.data.gov/dataset?q=cancer&sort=score+desc%2C+name+asc'

#Step 1: Create a session and load the page
driver = webdriver.Chrome(executable_path='path-to-driver')

#wait for the page to fully load
driver.get(url)

#wait for the page to fully load 
driver.implicitly_wait(5)

#Step 2: Parse HTML code and grab tables with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all('table')

#Step 3: Read tables with Pandas read_html()

dfs=pd.read_html(str(tables))
dfs=pd.DataFrame((dfs[0]))
dfs.to_csv('CSV-path')
print("success")
driver.close()
