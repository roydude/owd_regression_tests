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
from tests.mock_data.contacts import MockContacts
import time

class test_19184(GaiaTestCase):
    _Description = "[CONTACTS] Delete a contact from the contact details(all the fields filled)."

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
        # Get details of our test contacts.
        #
        self.Contact_1 = MockContacts().Contact_1
        self.data_layer.insert_contact(self.Contact_1)
        
        #
        # Launch contacts app.
        #
        self.contacts.launch()
        
        #
        # View our contact.
        #
        self.contacts.viewContact(self.Contact_1['name'])
           
        #
        # Edit our contact.
        #
        self.contacts.pressEditContactButton()
         
        #
        # Delete our contact.
        #
        self.contacts.pressDeleteContactButton()
         
        #
        # Cancel deletion.
        #
        x = self.UTILS.getElement(DOM.Contacts.cancel_delete_btn, "Cancel button")        
        self.marionette.tap(x)
         

        
        #
        # Relaunch the app.
        #
        self.contacts.launch()
         
        #
        # Now actually delete our contact.
        #
        self.contacts.deleteContact(self.Contact_1['name'])
 