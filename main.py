# Get the list of people that you follow on instagram but who doesn't follow you back
#                   requirements 
# 1. install selenium with "pip3 install selenium"
# 2. download chromedrive from "https://chromedriver.chromium.org/downloads"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramUnfollowersBot:
    def __init__(self, username, pw):
        # Path to where you saved your chromedriver executable
        self.driver = webdriver.Chrome('./chromedriver')
        self.username = username
        self.driver.get("https://www.instagram.com")
        sleep(2)  
        # find the username field and enter the account username
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        # find the password field and enter the account password
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        # find the path to the login button and click it
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()      
        sleep(6)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(8)
    def get_unfollowers(self):
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(6)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.username)).click()
        following = self.getNames()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers/')]".format(self.username)).click()
        followers = self.getNames()

        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        
    def getNames(self):
        sleep(5)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]") 
        last_ht, ht = 0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text!='']
            #print(names)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names

# fill with your username and password
bot = InstagramUnfollowersBot("","")
bot.get_unfollowers()