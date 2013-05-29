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

class test_5983(GaiaTestCase):
    _Description = "[SMS] (BLOCKED BY BUG 876641) CLONE - Press delete all text button in contact name field."
    
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
        # Establish which phone number to use.
        #
        self.Contact_1 = MockContacts().Contact_1
        self.Contact_1["tel"]["value"] = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Using target telephone number " + self.Contact_1["tel"]["value"])
        self.data_layer.insert_contact(self.Contact_1)

        self.UTILS.setTimeToNow()
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.messages.launch()
        
        #
        # Start a new SMS and add the message and contact name.
        #
        self.messages.startNewSMS()
        self.messages.enterSMSMsg("Test message.")
        self.messages.addNumberInToField(self.Contact_1["name"])

        #
        # Verify the contact name is present before removing it.
        #
        self.messages.checkisintofield(self.contact_1["name"], True)
        
        #
        # Remove it.
        #
        self.messages.removeFromToField(self.Contact_1["name"])
        x = self.UTILS.getElement( ("xpath", "//button[text()='OK']"), "Ok confirmation button.")
        x.tap()
        
        #
        # Verify the contact name is present before removing it.
        #
        self.messages.checkIsInToField(self.Contact_1["name"], False)
        
        
