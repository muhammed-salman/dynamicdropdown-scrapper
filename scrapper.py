from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import requests

url = "https://panchayatelection.maharashtra.gov.in/MasterSearch.aspx"

page= requests.get(url)

# create a new Firefox session
# use brew install geckodriver
# which geckodriver --> OUTPUTS THE PATH OF geckodriver if installed put this in below statement
driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
driver.implicitly_wait(30)
driver.get(url)
wait = WebDriverWait(driver, 10)

select_ids = ['ContentPlaceHolder1_SearchControl1_DDLLocalBody','ContentPlaceHolder1_SearchControl1_DDLDivision','ContentPlaceHolder1_SearchControl1_DDLDistrict','ContentPlaceHolder1_SearchControl1_DDLMunicipalcorporation','ContentPlaceHolder1_SearchControl1_ddlEP','ContentPlaceHolder1_SearchControl1_DDLWARDGP']

el = driver.find_element_by_id(select_ids[0])
local_body_select = Select(el) 
local_body_options = el.find_elements_by_tag_name('option')

local_body_option_value  = []
local_body_option_text = []

division_option_value  = []
division_option_text = []
division_local_body = []

district_option_value  = []
district_option_text = []
district_division = []

muncipal_option_value  = []
muncipal_option_text = []
muncipal_district = []

election_option_value = []
election_option_text = []
election_muncipal = []

ward_option_value  = []
ward_option_text = []
ward_election = []    
            

for option in local_body_options:
    local_body_option_value.append(option.get_attribute("value"))
    local_body_option_text.append(option.text)

local_body_data = pd.DataFrame({'value':local_body_option_value, 'text':local_body_option_text })

print(local_body_data.shape[0])

for i in range(1,local_body_data.shape[0]):
    wait.until(driver.find_element_by_id(select_ids[0]))
    local_body_select.select_by_value(local_body_option_value[i])
    
    cur = 1
    
    el = driver.find_element_by_id(select_ids[cur])
    division_select = Select(el) 
    division_options = el.find_elements_by_tag_name('option')
    
    if len(division_options)>1:
        for option in division_options:
            division_option_value.append(option.get_attribute("value"))
            division_option_text.append(option.text)
            division_local_body.append(local_body_option_text[i])
            


#print(python_select)

#parse html
soup = BeautifulSoup(driver.page_source,'html.parser')

# print(soup.prettify())    
'''
#finding the LocalBody select box options
local_body = soup.find(id = 'ContentPlaceHolder1_SearchControl1_DDLLocalBody').findAll('option')


#printing all the values in option tag
for i in range(1,len(local_body)):
    print(local_body[i]['value'],local_body[i].text)

params = {'ctl00$ContentPlaceHolder1$SearchControl1$DDLLocalBody': '2', 'ctl00$ContentPlaceHolder1$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$SearchControl1$DDLLocalBody', }

#page = requests.post(url, data = params)

#soup = BeautifulSoup(page.content,'html.parser')

#print(soup.prettify())    
'''