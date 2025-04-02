# Create a Selenium Script to verify the title for
#
# Open the Page - https://katalon-demo-cura.herokuapp.com/
#
# Verify the current URL, current title
#
# In the page source add a assertion that “CURA Healthcare Service” exist in the page. driver.pageSource() - String




# from numba.cuda.cudadrv.driver import driver
from selenium import webdriver

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data=driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()