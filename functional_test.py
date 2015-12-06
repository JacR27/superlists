from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_post_and_get_to_do_items(self):
        
        # go to home page
        self.browser.get('http://localhost:8000')

        # title and header had to-do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #enter item box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )
        #item entered
        inputbox.send_keys('hello')
        inputbox.send_keys(Keys.ENTER)
        #display item
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: hello' for row in rows),
            "New to-do item did not appear in table"
        )
        
        # ability to enter another item

        # enter second item

        # both items show on page

        # unique url displayed

        # url shows list

        # done
        self.fail("finish test")
if __name__=="__main__":
    unittest.main(warnings='ignore')
