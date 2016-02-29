'''
Created on Feb 15, 2015

@author: egao
'''

# -*- coding: utf-8 -*-

import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import unittest

class TestCase(unittest.TestCase):

    def setUp(self):
        profile = FirefoxProfile()
        # Ignore certification
        profile.set_preference("webdriver_assume_untrusted_issuer", False)
        profile.set_preference("webdriver_accept_untrusted_certs", True)
        profile.accept_untrusted_certs = True
        
        # Set user agent
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4")
        profile.update_preferences()
        self.driver = webdriver.Firefox(profile)

        self.base_url = "http://m.finance.yahoo.co.jp/"
        self.driver.implicitly_wait(30)
        self.accept_next_alert = True

    def ssAssertEquals(self, left, right):
        try:
            # assertionError-->screenshot
            self.assertEqual(left, right)
        except AssertionError, e:
            now = datetime.datetime.now()
            self.driver.save_screenshot("/var/log" + self.__class__.__name__ + "_" + now.strftime("%Y%m%d%H%M%S") + ".png")
            raise e

    def test_sitetop(self):
        self.driver.get(self.base_url)
        self.ssAssertEquals(u"Y!", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
