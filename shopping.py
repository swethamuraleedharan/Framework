#----------------1-----------------------------------

# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)
# driver = webdriver.Chrome(options=opts)
# driver.get('https://www.amazon.in/')
# driver.implicitly_wait(30)

# class DemoSearch:
#
#     def search_box(self):
#         driver.find_element('xpath','//input[@placeholder="Search Amazon.in"]').send_keys('shoes')
#         time.sleep(0.5)
#
#     def search_product(self):
#         driver.find_element('xpath','//div[@aria-label="shoes for women"]').click()
#         time.sleep(0.5)
#
#     def product_click(self):
#         driver.find_element('xpath','(//div[@class="a-section aok-relative s-image-tall-aspect"])[3]').click()
#         time.sleep(0.5)
#
#     def product_page(self):
#         handles = driver.window_handles
#         driver.switch_to.window(handles[1])
#         driver.find_element('xpath','//input[@id="add-to-cart-button"]').click()
#         time.sleep(1)
#
#
# search_obj = DemoSearch()
# search_obj.search_box()
# search_obj.search_product()
# search_obj.product_click()
# search_obj.product_page()

#-------------------2---------------------------------
# import time
# class DemoSearch:
#     def __init__(self,driver):
#         self.driver = driver
#     def search_box(self):
#         self.driver.find_element('xpath','//input[@placeholder="Search Amazon.in"]').send_keys('shoes')
#         time.sleep(0.5)
#
#     def search_product(self):
#         self.driver.find_element('xpath','//div[@aria-label="shoes for women"]').click()
#         time.sleep(0.5)
#
#     def product_click(self):
#         self.driver.find_element('xpath','(//div[@class="a-section aok-relative s-image-tall-aspect"])[3]').click()
#         time.sleep(0.5)
#
#     def product_page(self):
#         handles = self.driver.window_handles
#         self.driver.switch_to.window(handles[1])
#         self.driver.find_element('xpath','//input[@id="add-to-cart-button"]').click()
#         time.sleep(1)


## ------------3----------------------
# import time
# from data.reading_excel import search_locators
# locators = search_locators()
#
# class DemoSearch:
#     def __init__(self,driver):
#         self.driver = driver
#     def search_box(self):
#         self.driver.find_element(*locators['search_box']).send_keys('shoes')
#         time.sleep(0.5)
#
#     def search_product(self):
#         self.driver.find_element(*locators['search_product']).click()
#         time.sleep(0.5)
#
#     def product_click(self):
#         self.driver.find_element(*locators['product_click']).click()
#         time.sleep(0.5)
#
#     def product_page(self):
#         handles = self.driver.window_handles
#         self.driver.switch_to.window(handles[1])
#         self.driver.find_element(*locators['product_page']).click()
#         time.sleep(1)

##--------------------4--------------------
import time
from data.reading_excel import search_locators
from library.selenium_wrapper import SeleniumWrapper
locators = search_locators()

class DemoSearch:
    def __init__(self,driver):
        self.driver = driver
        self.wrapper_obj = SeleniumWrapper(driver)
    def search_box(self,ele):
        self.wrapper_obj.enter_data(locators['search_box'],ele)
        time.sleep(0.5)

    def search_product(self):
        self.wrapper_obj.click_element(locators['search_product'])
        time.sleep(0.5)

    def product_click(self):
        self.wrapper_obj.click_element(locators['product_click'])
        time.sleep(0.5)

    def product_page(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.wrapper_obj.click_element(locators['product_page'])
        time.sleep(1)
