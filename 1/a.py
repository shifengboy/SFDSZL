from selenium import webdriver


class TestWorkWeixin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
