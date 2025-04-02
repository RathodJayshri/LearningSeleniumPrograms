from selenium import webdriver
import pytest
import allure
import pytest
@allure.title("Verify the title of the webpage sdet.live")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")



# @allure.title("Verify the Title of the webpage app.vwo.com")
# def test_sample():
#     # Selenium 3 - Not much used now
#     driver_path = '/Users/pramod/Downloads/edge/msedgedriver'
#     driver = webdriver.EdgeService(executable_path=driver_path)
#     driver.get("https://app.vwo.com")

