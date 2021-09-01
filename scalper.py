import time
from selenium import webdriver as wd
import chromedriver_binary

# open broswer window and 
browser = wd.Chrome()

# will wait 10 seconds for window to open
browser.implicitly_wait(10)

# url for best buy rtx 3090
browser.get('https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434')

add_to_cart_button = browser.find_element_by_xpath('//*[@id="fulfillment-add-to-cart-button-71207970"]/div/div/div/button')
add_to_cart_button.click()
