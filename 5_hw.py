from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CLASS_NAME, "btn_action")


    if username_field and password_field and submit_button:
        print("Элементы найдены")
except NoSuchElementException:
    print("Элементы не найдены")

finally:
    driver.quit()



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
