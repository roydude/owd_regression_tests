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

class test_5980(GaiaTestCase):
    _Description = "[SMS] CLONE - Verify that If the contact has no phone number, a message stating that contact does not have a phone number is open up, and user is returned the contact list."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = AppMessages(self)
        self.contacts   = AppContacts(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        #
        # Change the settings to vibration only (backdoor method since
        # this isn't what we're testing).
        #
        self.data_layer.set_setting("vibration.enabled", True)
        self.data_layer.set_setting("audio.volume.notification", 0)
        
        #
        # Remove number and add contact.
        #
        self.Contact_1 = MockContacts().Contact_1
        self.Contact_1["tel"] = None
        self.data_layer.insert_contact(self.Contact_1)

        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Type a message containing the required string 
        #
        self.messages.startNewSMS()
        self.messages.enterSMSMsg("Test message")
        
        #
        # Search for our contact.
        #
        orig_iframe = self.messages.selectAddContactButton()
        
        #
        # Search the contacts list for our contact.
        #
        x = self.UTILS.getElements(DOM.Contacts.view_all_contact_list, "Contacts list")
        for i in x:
            if i.text == self.Contact_1["name"]:
                self.UTILS.logResult("info", "Tapping ...")
                i.tap()
                break
        
        self.UTILS.waitForElements(DOM.Messages.contact_no_phones_msg, "Message saying this contact has no phones")
        x = self.UTILS.getElement(DOM.Messages.contact_no_phones_ok, "OK button")
        x.tap()
        
        self.UTILS.headerCheck("Select contact")
          
