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

class Test:
    @classmethod
    def setUpCalss(self):
        print('执行开始')

    @classmethod
    def tearDownClass(self):
        print('执行结束')

    @pytest.mark.run(order = 1)
    def test_01(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = ChromeService(executable_path='CHROMEDRIVER_PATH')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        url = r'http://121.196.201.7:8080/login?from=%2F'
        self.driver.get(url)
        self.driver.set_window_size(1742, 1126)
        self.driver.find_element(By.ID, 'j_username').click()
        self.driver.find_element(By.ID, "j_username").send_keys("admin")
        self.driver.find_element(By.NAME, "j_password").click()
        self.driver.find_element(By.NAME, "j_password").send_keys("admin123")
        self.driver.find_element(By.NAME, "Submit").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "admin"
        self.driver.quit()

    @pytest.mark.run(order = 2)
    def test_02(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = ChromeService(executable_path='CHROMEDRIVER_PATH')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        url = r'http://121.196.201.7:8080/login?from=%2F'
        self.driver.get(url)
        self.driver.set_window_size(1742, 1126)
        self.driver.find_element(By.ID, 'j_username').click()
        self.driver.find_element(By.ID, "j_username").send_keys("dev")
        self.driver.find_element(By.NAME, "j_password").click()
        self.driver.find_element(By.NAME, "j_password").send_keys("dev123")
        self.driver.find_element(By.NAME, "Submit").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "dev"
        self.driver.quit()

    @pytest.mark.run(order = 5)
    def test_03(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.service = ChromeService(executable_path='CHROMEDRIVER_PATH')
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        url = r'http://121.196.201.7:8080/login?from=%2F'
        self.driver.get(url)
        self.driver.set_window_size(1742, 1126)
        self.driver.find_element(By.ID, 'j_username').click()
        self.driver.find_element(By.ID, "j_username").send_keys("test")
        self.driver.find_element(By.NAME, "j_password").click()
        self.driver.find_element(By.NAME, "j_password").send_keys("test123")
        self.driver.find_element(By.NAME, "Submit").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "test"
        self.driver.quit()


if __name__=='__main__':
    pytest.main(['-s','-v','--html=F:\file2\Automation_Project\report/test_Test.html','test_tt.py::Test_py'])
