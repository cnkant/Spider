from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
# waitTime=WebDriverWait(browser,10)
def crawl_pages(browser):
    pages_input=browser.find_element_by_class_name('J_Input')
    pages_input.clear()
    pages_input('2')
    sure_button=browser.find_element_by_class_name('J_Submit')
    sure_button.click()
if __name__ == '__main__':
    start_url='https://www.taobao.com/'
    browser=webdriver.Chrome('C:\\Users\\KangLi\\AppData\\Local\\CentBrowser\\Application\\chromedriver.exe')
    browser.get(start_url)
    search_input=browser.find_element_by_id('q')
    search_input.send_keys('ipad2020')
    time.sleep(5)
    search_button=browser.find_element_by_class_name('btn-search')
    search_button.click()
    time.sleep(10)
    crawl_pages(browser)
