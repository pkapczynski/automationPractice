class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.driver.find_elements_by_class_name('product-image-container')[1].click()