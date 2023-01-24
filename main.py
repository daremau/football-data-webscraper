from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

#All matches in website
all_matches_button = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_button.click()

#Selecting different country
dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

#Getting data form matches
matches = driver.find_elements(By.TAG_NAME, 'tr')
#//*[@id="page-wrapper"]/div/div[3]/div[1]/detailed-team/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]
date = []
home_team = []
score = []
away_team = []

for match in matches:
  date.append(match.find_element(By.XPATH, './td[1]').text)
  home_team.append(match.find_element(By.XPATH, './td[2]').text)
  score.append(match.find_element(By.XPATH, './td[3]').text)
  away_team.append(match.find_element(By.XPATH, './td[4]').text)
  print(match.text)

driver.quit()

#Exporting to CSV file
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index=False)
print(df)
