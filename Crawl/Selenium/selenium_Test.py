from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\\KangLi\\AppData\\Local\\CentBrowser\\Application\\chromedriver.exe')
browser.get("http://www.baidu.com")
input_text=browser.find_element_by_id('kw') # 通过id定位元素，除此之外还有多种方式定位元素
input_text.send_keys('python')  # 文本框输入事件
click_button=browser.find_element_by_id('su')
click_button.click()    # 按钮点击事件
