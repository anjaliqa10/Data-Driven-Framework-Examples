import XLUtils
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")     # provide any URL you want to automate
driver.maximize_window()
driver.implicitly_wait(10)

path = "test-data-path"     # Create test-data.xlsx file and provide the path e.g c://Users/testdata.xlsx

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):  # normally 'rows' value will be total no. of rows-1, so if u want to iterate over all the rows, always mention rows+1
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()
    time.sleep(10)

    if driver.title == "Find a Flight: Mercury Tours:":
        print('test is passed')
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")

    else:
        print('test failed')
        XLUtils.writeData(path, "Sheet1", r, 3, "Test failed")

    driver.find_element_by_link_text("Home").click()
    print('Navigated to Home-Page')
