from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://wikipedia.com")

# 1 > ID
el1 = driver.find_element('id', 'searchInput')
el1.send_keys("Hello world!")
el1.click()
sleep(20)
##
# 2 > Xpath
#٫ Absolute
#el2 = driver.find_element('xpath', '/html/body/div[3]/form/fieldset/div/input')
#print(el1)
#print(el2)
#assert el1 == el2
# Relative
#driver.find_element('xpath', "//input[@type='search']")
#driver.find_element('xpath', "//*[text()='Italiano']")


# 3 > Tag
#driver.find_element('tag name', 'select')

# 4 > Link Text
#driver.find_element('link text', 'Download Wikipedia for Android or iOS')

# 5 > Partial Link Text
#driver.find_element('partial link text', 'Download')

# 6 > Class
#driver.find_element('class name', 'svg-search-icon')

# 7 > Css Selector
#driver.find_element('css selector', '#searchInput')
#driver.find_element('css selector', '.svg-search-icon')
