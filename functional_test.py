from selenium import webdriver
import unittest

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
        self.fail("finish test")
        #enter item box

        #item entered

        #display item

        # ability to enter another item

        # enter second item

        # both items show on page

        # unique url displayed

        # url shows list

        # done

if __name__=="__main__":
    unittest.main(warnings='ignore')
