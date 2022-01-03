from selenium import webdriver # 驱动Chrome浏览器
from selenium.common.exceptions import TimeoutException # 超时错误检测
from selenium.webdriver.common.by import By # 用于自定义查找元素的方法
from selenium.webdriver.support import expected_conditions as EC    # 用EC指代expected_conditions
from selenium.webdriver.support.ui import WebDriverWait # 定义等待时间
from urllib.parse import quote  # 将汉字转码为页面指定编码
from pyquery import PyQuery # 解析页面
import time

KEYWORD = 'ipad2020'
browser = webdriver.Chrome('C:\\Users\\KangLi\\AppData\\Local\\CentBrowser\\Application\\chromedriver.exe')
wait_time = WebDriverWait(browser, 10)  # 等待时间为10s
def crawl_page(page,i):
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        time.sleep(10)

        if page>1:
            input_pages=wait_time.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,'input .J_Input')))
            input_pages.clear() # 清除输入框原本内容
            input_pages.send_keys(page) # 输入想要爬取第几页
            submit_button=wait_time.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,'span.J_Submit')))
            submit_button.click()   # 点击确定按钮
        # 10s内定位item，如果定位不到则会报错,located后面两层括号
        wait_time.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except: # 出现错误重新爬取该页
        i+=1
        print(">>>出错，将开始第%d次尝试"%i)
        crawl_page(page,i)

def get_products():
    html=browser.page_source    # 获取源代码
    doc=PyQuery(html)   # 解析源代码，类似于BeautifulSoup
    items=doc('#mainsrp-itemlist .items .item').items()
    # print(items)
    for item in items:
        products={
            'title':item.find('.J_ClickStat').text().replace('\n',''),
            'image':item.find('.J_ItemPic').attr('data-src'),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(products)
        # file.write(products)
if __name__ == '__main__':
    # for i in range(2):
    #     # 爬取前两页
    #     t=1
    #     crawl_page(i+1,t)
    crawl_page(2,1)