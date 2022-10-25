from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import selenium.webdriver

import pickle
import time

def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # opens ticketswap
    browser.get("https://www.ticketswap.nl/event/pip-opening-weekend/regular-tickets/bd69c0b0-3c0b-40c3-9e88-ac86ea76e9eb/2392838") #test

    Tickets = False

    #checks if logged in
    checkLogIn = WebDriverWait(browser, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        "css-n4f2wf"))
    )

    while not Tickets:
        try:
            # refreshes the page looking for ticket
            WebDriverWait(browser, 10).until_not(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                "css-19fqo0n"))
            )
            print("it's not there")
            time.sleep(2)
            browser.refresh()

        except:
            # when ticket available, click on it
            continueClick = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                "css-19fqo0n"))
            )
            print('its there :)')
            continueClick.click()
            time.sleep(3)

            # add to cart
            addCart = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                "e1nefpxg2"))
            )

            addCart.click()
            os.system('Ping.aiff')
            os.system('Ping.aiff')
            os.system('Ping.aiff')

            browser.refresh()
            print('refreshed')
            time.sleep(5)

            # go to cart
            goToCart = WebDriverWait(browser, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                "e17kjwee0")))

            goToCart.click()
            print('at cart')
            time.sleep(1)

            Tickets = True

main()

