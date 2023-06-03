from Base.driver import *
from Pages.login import *
from HTMLTestRunner import HTMLTestRunner
import unittest
class Test:
    @classmethod
    def setUpCalss(self):
        print('执行开始')
    @classmethod
    def tearDownClass(self):
        print('执行结束')

    data_list1 = [('admin', 'admin123'), ('dev', 'dev123'), ('test', 'test123')]
    @pytest.mark.parametrize('username, pwd', data_list1)
    def test_01(self,username,pwd):
        self.Login = InitLogin()
        self.Login.login(username, pwd)
        assert self.Login.driver.driver.find_element(By.CSS_SELECTOR, ".model-link > .hidden-xs").text == username
        self.Login.driver.driver.quit()

if __name__=='__main__':
    pytest.main(['-s','-v','--html=F:\file2\Automation_Project\report/test_Test.html','test_tt.py::Test_py'])



