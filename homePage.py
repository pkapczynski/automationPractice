from selenium.webdriver import ActionChains

import time


class HomePage:


    def __init__(self, driver):
        self.driver = driver
    def homePage(self):
        self.driver.find_element_by_id('header_logo').click()
    def openFirstProduct(self):
        self.driver.find_element_by_xpath('//a[contains (@href, "http://automationpractice.com/index.php?id_product=1&controller=product")]')
    def hoverFirstElement(self):
        firstproduct= self.driver.find_element_by_xpath('//a[contains (@href, "http://automationpractice.com/index.php?id_product=1&controller=product")]')
        action = ActionChains(self.driver)
        action.move_to_element(firstproduct).perform()
    def addToCartAfterHover(self):
        self.driver.find_element_by_xpath('//span[contains (text(), "Add to cart")]').click()
        time.sleep(3)
    def checkoutAfterHover(self):
        self.driver.find_element_by_xpath('//a[contains(@title, "Proceed to checkout")]').click()
    def getTitle(self):
        title = self.driver.find_element_by_xpath('//span[contains (@id, "layer_cart_product_title")]').text

