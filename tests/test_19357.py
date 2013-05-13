#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *
import time

#
# Imports particular to this test case.
#
from tests.mock_data.contacts import MockContacts

class test_19193(GaiaTestCase):
    _Description = "[SMS] CLONE - Verify that If the contact only has a phone number, that phone number is automatically selected and the user is returned to the compose SMS screenwidth the contacts name filled-in in the To Field..."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
        self.messages   = AppMessages(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

        self.data_layer.set_setting("vibration.enabled", True)
        self.data_layer.set_setting("audio.volume.notification", 0)

        #
        # Prepare the contact we're going to insert.
        #
        self.contact_1 = MockContacts().Contact_1

        #
        # Add this contact (quick'n'dirty method - we're just testing sms, no adding a contact).
        #
        self.data_layer.insert_contact(self.contact_1)

        
        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch contacts app.
        #
        self.contacts.launch()
        
        #
        # View the details of our contact.
        #
        self.contacts.viewContact(self.contact_1['name'])
        return
        
        #
        # Tap the sms button in the view details screen to go to the sms page.
        #
        smsBTN = self.UTILS.getElement(DOM.Contacts.sms_button, "Send SMS button")
        self.marionette.tap(smsBTN)

        #
        # Switch to the 'Messages' app frame (or marionette will still be watching the
        # 'Contacts' app!).
        #
        time.sleep(2)
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Messages.frame_locator)

        #
        # TEST: this automatically opens the 'send SMS' screen, so
        # check the correct name is in the header of this sms.
        #
        self.UTILS.TEST(self.UTILS.headerCheck(self.contact_1['name']),
                        "'Send message' header = '" + self.contact_1['name'] + "'.")
    