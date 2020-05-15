from selenium import webdriver
from time import sleep
from creditentials import email, password


class PurgerBot:

    #This method opens up the browser and logs the user in
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://youtube.com")
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()

        # The line below is for two-factor authentication and you will need to do this part on your own
        sleep(60)

        # If you only have one youtube account tied to this email, comment the next line out
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/form/div[2]/button/span").click()

myBot = PurgerBot(email,password)

