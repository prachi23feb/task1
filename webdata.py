from selenium import webdriver
driverpath = "C:\\Users\\HP\\Desktop\\Chrome\\chromedriver.exe"
driver = webdriver.Chrome(driverpath)
driver.get("https://auberginesolutions.com/development")
print(driver.title)
e = []
e.append(driver.find_element_by_xpath("//span[@title='ux design']"))
e.append(driver.find_element_by_xpath("//span[@title='development']"))
e.append(driver.find_element_by_xpath("//span[@title='academy']"))
e.append(driver.find_element_by_xpath("//span[@title='work']"))
e.append(driver.find_element_by_xpath("//span[@title='careers']"))
e.append(driver.find_element_by_xpath("//a[@title='blog']"))
for i in e:
    print(i.get_attribute("innerHTML"))
    #print(i.text)
