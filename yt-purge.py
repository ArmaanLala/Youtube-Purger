from selenium import webdriver
from time import sleep
from creditentials import email, password


class PurgerBot:

    # This method opens up the browser and logs the user in
    def __init__(self, email, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://youtube.com")
        self.driver.maximize_window()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span").click()

        # The line below is for two-factor authentication and you will need to do this part on your own
        sleep(20)

        # If you only have one youtube account tied to this email, comment the next line out
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div/form/div[2]/button/span").click()
        sleep(5)
        
    # Prints all your subscriptions in a txt file
    def listSubscriptions(self):
        subs = open("subscription.txt", "w")
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-collapsible-entry-renderer/ytd-guide-entry-renderer/a/paper-item").click()
        subscriptions = self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div")
        channels = subscriptions.find_elements_by_id("endpoint")
        for item in channels:
            name = item.get_attribute("title")
            subs.write(name + "\n")

    # Finished the massive unsubscribe function
    def massUnsubscribe(self, x):
        for i in range(x):
            subscriptions = self.driver.find_element_by_xpath(
                "/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div")
            sleep(3)
            subscriptions.find_element_by_id("endpoint").click()
            sleep(3)
            self.driver.find_element_by_xpath(
                "/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/ytd-subscribe-button-renderer/paper-button").click()
            sleep(3)
            self.driver.find_element_by_xpath(
                "/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/paper-button").click()
            sleep(3)
            self.driver.execute_script("window.history.go(-1)")
            sleep(10)
            self.driver.refresh()

    # clears the users search history
    def history(self):
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[1]/a/paper-item").click()
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[2]/ytd-browse-feed-actions-renderer/div/ytd-button-renderer[1]/a/paper-button").click()
        sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/paper-button").click()


myBot = PurgerBot(email, password)
myBot.listSubscriptions()
# Input the number of channels you are subscribed to
myBot.massUnsubscribe()
myBot.history()
myBot.driver.close()
