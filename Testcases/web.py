from Common.driver import *
class Test:
    @classmethod
    def setUpCalss(self):
        print('执行开始')
    @classmethod
    def tearDownClass(self):
        print('执行结束')
    @pytest.mark.run(order = 1)
    def test_01(self):
        self.method = InitDriver()
        self.method.driver.get(r'http://121.196.201.7:8080/login?from=%2F')
        self.method.driver.find_element(By.ID, 'j_username').click()
        self.method.driver.find_element(By.ID, "j_username").send_keys("admin")
        self.method.driver.find_element(By.NAME, "j_password").click()
        self.method.driver.find_element(By.NAME, "j_password").send_keys("admin123")
        self.method.driver.find_element(By.NAME, "Submit").click()
        assert self.method.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "admin"
        self.method.driver.quit()

    @pytest.mark.run(order = 2)
    def test_02(self):
        self.method = InitDriver()
        self.method.driver.get(r'http://121.196.201.7:8080/login?from=%2F')
        self.method.driver.find_element(By.ID, 'j_username').click()
        self.method.driver.find_element(By.ID, "j_username").send_keys("dev")
        self.method.driver.find_element(By.NAME, "j_password").click()
        self.method.driver.find_element(By.NAME, "j_password").send_keys("dev123")
        self.method.driver.find_element(By.NAME, "Submit").click()
        assert self.method.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "dev"
        self.method.driver.quit()

    @pytest.mark.run(order = 3)
    def test_03(self):
        self.method = InitDriver()
        self.method.driver.get(r'http://121.196.201.7:8080/login?from=%2F')
        self.method.driver.find_element(By.ID, 'j_username').click()
        self.method.driver.find_element(By.ID, "j_username").send_keys("test")
        self.method.driver.find_element(By.NAME, "j_password").click()
        self.method.driver.find_element(By.NAME, "j_password").send_keys("test123")
        self.method.driver.find_element(By.NAME, "Submit").click()
        assert self.method.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == "test"
        self.method.driver.quit()

if __name__=='__main__':
    pytest.main(['-s','-v','--html=F:\file2\Automation_Project\report/test_Test.html','test_tt.py::Test_py'])
