from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://music.163.com/')

driver.switch_to_frame('contentFrame')

htmllist = driver.find_elements_by_xpath('//p[@class="dec"]//a')

songlist_list = []
songlist_list_name = []

for item in htmllist:
    songlist_list.insert(0, item.get_attribute('href'))  # 用get_attribute获取标签属性
    songlist_list_name.insert(0, item.get_attribute('textContent').strip())
