from selenium import webdriver # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium. webdriver.support import expected_conditions as EC # type: ignore
from selenium. webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

driver = webdriver. Chrome('/Users/simransetia/Downloads/chromedriver-2')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
target='"Ravikiran"'#Enter your friend's name
string="Message sent using Python !! "#The message you need to
x_arg='//span[contains(@title, '+ target +')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = driver. find_element_by_class_name('_1Plpp')
for i in range(50) :
    input_box.send_keys(string+Keys. ENTER)