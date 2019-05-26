from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time
from homePage import HomePage
from productPage import ProductPage
class CartTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome('/Users/piotrkapczynski/PycharmProjects/teraz to bedzie dzialac/chromedriver')

    def test_addToCartByHover(self):

        driver = self.driver
        time.sleep(3)
        Hp = HomePage(driver)
        Hp.hoverFirstElement()
        Hp.addToCartAfterHover()

        ProductPrice = driver.find_element_by_xpath('//span[contains (@id, "layer_cart_product_price")]').text
        Hp.checkoutAfterHover()
        time.sleep(3)
        PriceInCart= driver.find_element_by_xpath('//span[contains (@class, "price")]/span').text
        assert ProductPrice in PriceInCart



    def test_addToCartByProductCard(self):
        self.driver.get('http://automationpractice.com/')

        time.sleep(3)
        driver = self.driver
        Hp = HomePage(driver)
        Hp.homePage()
        time.sleep(4)
        Pp = ProductPage(driver)
        Pp.addToCart()

    def tearDownClass(cls):
        cls.driver.close()





