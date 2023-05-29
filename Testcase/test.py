import pytest
import os
# from py.xml import html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test:

    def setup(self):
        self.driver = webdriver.Chrome()
        url = r'https://mail.qq.com/'
        self.driver.get(url)

    def teardown(self):
        self.driver.quit()

    #点击酷家乐（按钮）
    # @pytest.mark.run(order=1)
    # def test_001(self):
    #     time.sleep(3)
    #     self.driver.switch_to_frame(self.driver.find_element(By.XPATH, "//*[@id="login_iframe"]"))

    # @pytest.mark.run(order=2)
    # def test_002(self):
    #     top = self.driver.find_element(By.XPATH, "//*[@id="app"]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div[1]/div/button")
    #     self.driver.switch_to_frame(top)


    # 正常输入
    # @pytest.mark.run(order=2)
    # def test_002(self):
    #     self.driver.find_element(By.ID, "kw").send_keys('文字按字音和字形，可分为表形文字、表音文字和意音文字。按语音和语素，可分为音素文字、音节文字和语素文字。 表形文字是人类早期原生文字的象形文字')
    #     self.driver.find_element(By.ID, "su").click()
    #
    #最短输入
    # @pytest.mark.run(order=3)
    # def test_003(self):
    #     self.driver.find_element(By.ID, "kw").send_keys('天空')
        # self.driver.find_element(By.ID, "su").click()
    #
    # #输入空字符串
    # @pytest.mark.run(order=4)
    # def test_004(self):
    #     self.driver.find_element(By.ID, "kw").send_keys(' ')
    #     self.driver.find_element(By.ID, "su").click()
    #
    # #不输入
    # @pytest.mark.run(order=5)
    # def test_005(self):
    #     self.driver.find_element(By.ID, "kw").send_keys('')
    #     self.driver.find_element(By.ID, "su").click()
    #
    # #选择图片
    # @pytest.mark.run(order=6)
    # def test_006(self):
    #     self.driver.find_element(By.CLASS_NAME, "soutu-btn").click()
    #
    # #点击换一换
    # @pytest.mark.run(order=7)
    # def test_007(self):
    #     self.driver.find_element(By.CLASS_NAME, "hot-refresh-text").click()
    #
    #点击我的关注
    @pytest.mark.run(order=7)
    def test_007(self):
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "百度一下").click()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #






