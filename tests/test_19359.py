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

class test_19359(GaiaTestCase):
    _Description = "[CONTACTS] Send an email to a contact from the contact details (Contact with multiple emails)"

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
        self.email      = AppEmail(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

        #
        # Get details of our test contacts.
        #
        self.Contact_1 = MockContacts().Contact_multipleEmails
        
        #
        # Set the emails to ones that work.
        #
        self.Contact_1["email"][0]["value"] = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.Contact_1["email"][1]["value"] = self.UTILS.get_os_variable("GMAIL_2_EMAIL")
        self.Contact_1["email"][2]["value"] = self.UTILS.get_os_variable("HOTMAIL_1_EMAIL")

        #
        # We're not testing adding a contact, so just stick one 
        # into the database.
        #
        self.data_layer.insert_contact(self.Contact_1)
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.UTILS.getNetworkConnection()
        
        #
        # Set up to use email (with account #1).
        #
        em_user = self.UTILS.get_os_variable("GMAIL_1_USER")
        em_email= self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        em_pass = self.UTILS.get_os_variable("GMAIL_1_PASS")
        self.email.launch()
        self.email.setupAccount(em_user, em_email, em_pass)
        
        #
        # Launch contacts app.
        #
        self.contacts.launch()
        
        #
        # View the details of our contact.
        #
        self.contacts.viewContact(self.Contact_1['name'])
        
        #
        # Click the 2nd email button
        #
        emailBTN = self.UTILS.getElement( ("id", DOM.Contacts.email_button_spec_id % 1), 
                                        "2nd send Email button")
        self.marionette.tap(emailBTN)

        #
        # Switch to email frame.
        #
        time.sleep(5)
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Email.frame_locator) 
        
        x = ("xpath", "//div[@class='cmp-to-container cmp-addr-container']//span[@class='cmp-peep-name']")
        y = self.UTILS.getElement(x, "'To' field")
        self.UTILS.TEST(y.text == self.Contact_1["email"][1]["value"],
                        "The 'to' field contains '" + \
                        self.Contact_1["email"][1]["value"] + \
                        "' (it was (" + y.text + ").")
        
        self.UTILS.screenShotOnErr()