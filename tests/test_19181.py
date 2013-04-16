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

class test_19181(GaiaTestCase):
    _Description = "Remove a photo,a phone number, an email, an address and a comment from a contact and restore the phone number and the comment."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
        self.settings   = AppSettings(self)
                
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
        # Set up to use data connection.
        #
        self.settings.turn_dataConn_on_if_required()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Launch contacts app.
        #
        self.contacts.launch()
        
        #
        # View our contact.
        #
        self.contacts.viewContact(self.Contact_1)
        
        #
        # Edit our contact.
        #
        self.contacts.pressEditContactButton()
        
        self.UTILS.savePageHTML("/tmp/roy1.html")