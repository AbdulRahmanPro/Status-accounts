from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import os
import time
import re

class AmzoneBot:
    def __init__(self, pathprofile, option):
        self.chrome_options = uc.ChromeOptions()
        self.chrome_options.add_argument(f"--user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\{pathprofile}")
        self.chrome_options.add_argument("--incognito")
        if option == "--headless":
            self.chrome_options.add_argument("--headless")
        else:
            self.chrome_options.add_argument("NONE")
        self.driver = uc.Chrome(options=self.chrome_options)


    def element_present(self, by, value):
        try:
            WebDriverWait(self.driver, 0).until(EC.presence_of_element_located((by, value)))
            return True
        except:
            return False

    def Accounts_Status(self, xmain):
        self.driver.get("https://gaming.amazon.com/home")
        cookie = {
            "name": "x-main",
            "value": f"{xmain['x_main']}"
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(2)
        if self.element_present(By.XPATH, "//*[contains(text(),'Try Prime')]"):
            print('Try Prime')
            with open('./Functions/Config/Prime.txt', "a") as file:
                line = xmain["email"] + xmain["x_main"] + "\n"
                file.write(line)

        if self.element_present(By.XPATH, "//*[contains(text(),'Activate Prime Gaming')]"):
            with open('./Functions/Config/Activate_prime.txt', "a") as file:
                line = xmain["email"] + xmain["x_main"] + "\n"
                file.write(line)

        if not (self.element_present(By.XPATH, "//*[contains(text(), 'Activate Prime Gaming')]") or self.element_present(By.XPATH, "//*[contains(text(), 'Try Prime')]")):
            with open('./Functions/Config/Successful_account.txt', "a") as file:
                line = xmain["email"] + xmain["x_main"] + "\n"
                file.write(line)

    def start(self):
        email_list = []
        file_path = os.path.abspath("./Functions/Config/Accounts.txt")
        with open(file_path, "r") as file:
            for line in file:
                full_text = line.strip()
                split_text = full_text.split('_:_')
                desired_text = {
                    'email': split_text[0],
                    'x_main': split_text[1]
                }
                email_list.append(desired_text)
                print(split_text)
        for email in email_list:
            self.Accounts_Status(email)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    pathprofile = "profile_path_here"
    option = "--headless"
    bot = AmzoneBot(pathprofile, option)
    bot.start()
    bot.close()
