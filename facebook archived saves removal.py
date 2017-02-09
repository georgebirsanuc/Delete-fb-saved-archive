# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class FbPyTestcase2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_fb_py_testcase2(self):
        driver = self.driver
        driver.get(self.base_url + "/saved/?cref=28&collection_token=100001097280457%3A586254444758776%3A102")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_e_01Xz | ]]
        driver.find_element_by_id("email").clear()
        time.sleep(1)
        driver.find_element_by_id("email").send_keys("0755491753")
        time.sleep(1)
        driver.find_element_by_id("pass").clear()
        time.sleep(1)
        driver.find_element_by_id("pass").send_keys("PASSWORD GOES HERE")
        time.sleep(1)
        driver.find_element_by_id("loginbutton").click()
        time.sleep(1)
        driver.get(self.base_url + "/saved/?cref=28&collection_token=100001097280457%3A586254444758776%3A102")
        driver.find_element_by_xpath("//a[contains(text(),'...')]").click()
        driver.find_element_by_xpath("//span[contains(text(),'Unsave')]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
