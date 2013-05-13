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

class test_19195(GaiaTestCase):
    _Description = "[SMS] Verify the Carrier of number from which the contact is sending message to the user."
    _TestMsg     = "Test text - please ignore."

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
        # Establish which phone number to use.
        #
        self.contact_1["tel"]["value"] = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Using target telephone number " + self.contact_1["tel"]["value"])
         
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
     
        #
        #  Check the carrier is displayed here.
        #
        x = self.UTILS.getElement(DOM.Messages.type_and_carrier_field, "Contact phone 'type' and 'carrier' field")
        
        self.UTILS.TEST( self.contact_1["tel"]["type"]    in x.text, "Phone type is in the header.")
        self.UTILS.TEST( self.contact_1["tel"]["carrier"] in x.text, "Phone carrier is in the header.")
