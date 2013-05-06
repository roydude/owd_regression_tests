#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#

class test_19186(GaiaTestCase):
    _Description = '[CONTACTS] Delete all characters to the name and surname fields.'
    
    _testName    = "Obi"
    _testSurname = "Wan"

    def setUp(self):
        pass
    
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

        #
        # Launch contacts app.
        #
        self.contacts.launch()

        #
        # Click create new contact.
        #
        self.contacts.startCreateNewContact()
        
        
        #####################################
        #
        # Given name ...
        #
        
        #
        # Add some info. to the field.
        #
        self.UTILS.typeThis(DOM.Contacts.given_name_field, "Given name field", self._testName)
        
        #
        # Press the 'x'.
        #
        x = self.UTILS.getElement(DOM.Contacts.given_name_reset_icon, "Given name reset icon")
        self.marionette.tap(x)

        #
        # Click the header, then verify that the field contains nothing.
        #
        self.marionette.tap(self.marionette.find_element("tag name", "h1"))
        x = self.UTILS.getElement(DOM.Contacts.given_name_field, "Given name field")
        self.UTILS.TEST(x.text == "", "Given name field is empty after being cleared.")
        
                
        #####################################
        #
        # Surname ...
        #
        
        #
        # Add some info. to the field.
        #
        self.UTILS.typeThis(DOM.Contacts.family_name_field, "Surname field", self._testSurname)
        
        #
        # Press the 'x'.
        #
        x = self.UTILS.getElement(DOM.Contacts.family_name_reset_icon, "Surname reset icon")
        self.marionette.tap(x)

        #
        # Click the header, then verify that the field contains nothing.
        #
        self.marionette.tap(self.marionette.find_element("tag name", "h1"))
        x = self.UTILS.getElement(DOM.Contacts.family_name_field, "Surname field")
        self.UTILS.TEST(x.text == "", "Surname field is empty after being cleared.")
                
