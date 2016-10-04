import os
import unittest
from appium import webdriver
from time import sleep


class Ios(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    "Class to run tests against the Chess Free app"

    def User_setup_Desirecapabolities(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['deviceName'] = 'iPad 2'
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath('/Users/wasey/Desktop/UICatalog.app')
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)


    def User_shutdown_Ios(self):
        "Tear down the test"
        self.driver.quit()


    def test_001_element_button(self):
        "Test the Button element"
        button = self.driver.find_element_by_xpath("//UIAApplication[1]")
        button.click()
        Button=button.text
        print(Button)


    def test_002_element_control(self):
        control = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]")
        control.click()
        Cntrl=control.text
        print(Cntrl)

    def test_003_element_textfield(self):
        TextField = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]")
        TextField.click()
        Text=TextField.text
        print(Text)

    def test_004_element_searchField(self):
        SearchField = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]")
        SearchField.click()
        search=SearchField.text
        print(search)

    def test_005_element_TextView(self):
        TextView = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]")
        TextView.click()
        text=TextView.text
        print(text)

    def test_006_element_Picker(self):
        Picker = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]")
        Picker.click()
        picker=Picker.text
        print(picker)

    def test_007_element_Image(self):
        Image = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]")
        Image.click()
        image=Image.text
        print(image)

    def test_008_element_Web(self):
        Web = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[8]")
        Web.click()
        web=Web.text
        print(web)

    def test_009_element_Segmant(self):
        Segmant = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[9]")
        Segmant.click()
        segmant=Segmant.text
        print(segmant)

    def test_010_element_Toolber(self):
        Toolber = self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[10]")
        Toolber.click()
        toolber=Toolber.text
        print(toolber)

        # back = self.driver.find_element_by_name("//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]")
        # back.click()




# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Ios)
    unittest.TextTestRunner(verbosity=2).run(suite)
