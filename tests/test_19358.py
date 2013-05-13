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

class test_19358(GaiaTestCase):
    _Description = "[SMS] Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field.(second phone number)."

    def setUp(self):
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
        # Select our contact.
        #
        #
        # View the details of our contact.
        #
        self.contacts.viewContact(self.Contact_1['name'])

        #
        # Tap the 2nd sms button (index=1) in the view details screen to go to the sms page.
        #
        smsBTN = self.UTILS.getElement( ("id", DOM.Contacts.sms_button_specific_id % 1), 
                                        "2nd send SMS button")
        self.marionette.tap(smsBTN)

        #
        # Switch to the 'Messages' app frame (or marionette will still be watching the
        # 'Contacts' app!).
        #
        self.marionette.switch_to_frame()
#         self.UTILS.waitForElements(("xpath", "//iframe[@src='" + DOM.Messages.frame_locator[1] + "']"), 
#                                    "Messaging app frame", False, 20)
        self.UTILS.switchToFrame(*DOM.Messages.frame_locator)
        time.sleep(3)

        #
        # TEST: this automatically opens the 'send SMS' screen, so
        # check the correct name is in the header of this sms.
        #
        self.UTILS.TEST(self.UTILS.headerCheck(self.Contact_1['name']),
                        "'Send message' header = '" + self.Contact_1['name'] + "'.")
    

        #
        # Check this is the right number.
        #
        x = self.UTILS.getElement( ("id", "contact-carrier"), "Number and carrier field")

        self.UTILS.TEST(self.Contact_1["tel"][1]["type"] in x.text,
                        "'" + self.Contact_1["tel"][1]["type"] + "' displayed in the number / carrier field.")

        self.UTILS.TEST(self.Contact_1["tel"][1]["carrier"] in x.text,
                        "'" + self.Contact_1["tel"][1]["carrier"] + "' displayed in the number / carrier field.")
