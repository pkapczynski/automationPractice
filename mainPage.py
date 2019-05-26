newProject = '//a[contains (@href, "/create-a-design")]'
newCv = '//a[contains (@href, "https://www.canva.com/design?create&type=TACQ-j4WGew&category=tACZCki4tbY&schema=web-2")]'
class MainPage:
    def __init__(self, driver):
        self.driver = driver


    def newProject(self):
        self.driver.find_element_by_xpath(newProject).click()
    def newCv(self):
        self.driver.find_element_by_xpath(newCv).click()