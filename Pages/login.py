from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Base.driver import *

class InitLogin:
    def login(self,username,password):
        self.driver = InitDriver()
        self.driver.driver.get(r'http://121.196.201.7:8080/login?from=%2F')
        self.driver.driver.maximize_window()
        self.driver.driver.find_element(By.ID, 'j_username').click()
        self.driver.driver.find_element(By.ID, "j_username").send_keys(username)
        self.driver.driver.find_element(By.NAME, "j_password").click()
        self.driver.driver.find_element(By.NAME, "j_password").send_keys(password)
        self.driver.driver.find_element(By.NAME, "Submit").click()




