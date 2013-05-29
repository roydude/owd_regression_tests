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

class test_19356(GaiaTestCase):
    _Description = "[SMS] Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
        self.messages   = AppMessages(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

        #
        # Get details of our test contacts.
        #
        self.Contact_1 = MockContacts().Contact_multiplePhones

        #
        # We're not testing adding a contact, so just stick one 
        # into the database.
        #
        self.data_layer.insert_contact(self.Contact_1)
        
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
        self.contacts.viewContact(self.Contact_1['name'])

        #
        # Tap the 2nd sms button (index=1) in the view details screen to go to the sms page.
        #
        smsBTN = self.UTILS.getElement( ("id", DOM.Contacts.sms_button_specific_id % 0), 
                                        "1st send SMS button")
        self.marionette.tap(smsBTN)

        #
        # Switch to the 'Messages' app frame (or marionette will still be watching the
        # 'Contacts' app!).
        #
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Messages.frame_locator)
        time.sleep(2)

        #
        # TEST: this automatically opens the 'send SMS' screen, so
        # check the correct name is in the header of this sms.
        #
        self.UTILS.headerCheck("1 recipient")

        #
        # Check this is the right number.
        #
        self.messages.checkIsInToField(self.Contact_1["name"])
        self.messages.checkNumberIsInToField(self.Contact_1["tel"][0]["value"])
