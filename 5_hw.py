from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, '#user-name')

password = driver.find_element(By.CSS_SELECTOR, '#password')

submit_button = driver.find_element(By.CSS_SELECTOR, '[type=submit]')


if username and password and submit_button:
    print("Элементы найдены")
else:
    print("Не все элементы найдены")





#CSS_https://flukeout.github.io/

1. plate
2. bento
3. #fancy
4. plate > apple 
5. #fancy > pickle 
6. .small
7. orange.small
8. bento > orange.small
9. plate, bento
10. *
11. plate > * #Child Combinator (>): ul > * selects all direct children of <ul> elements.
12. plate + apple
13. bento ~ pickle
14. plate > apple 



#XPATH_https://topswagcode.com/xpath/
1. plate
2. bento
3. //plate/apple
4. //*
5. //*/apple
6. //*[@id='fancy']
7. //plate/apple
8. //*[@id="fancy"]/pickle
9. //*[contains(@class,'small')]
10. //orange[contains(@class,"small")] 
11. //bento/orange[contains(@class,"small")] 
12. //plate|//bento
13. //plate/*
14. //plate/following-sibling::apple 
