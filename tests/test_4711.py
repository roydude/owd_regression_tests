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

class test_4711(GaiaTestCase):
    _Description = "[SMS] ** Diffrent numbers but same device! ** Send an SMS to multiple contacts."
    
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
        self.Contact_2 = MockContacts().Contact_2
        
        self.Contact_1["tel"]["value"] = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.Contact_2["tel"]["value"] = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM_LONG")

        self.UTILS.logComment("Using target telephone number " + self.Contact_1["tel"]["value"])
        self.UTILS.logComment("Using target telephone number " + self.Contact_2["tel"]["value"])
        
        self.data_layer.insert_contact(self.Contact_1)
        self.data_layer.insert_contact(self.Contact_2)


        self.UTILS.setTimeToNow()
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # First, we need to make sure there are no statusbar notifs.
        #
        self.UTILS.clearAllStatusBarNotifs()
        
        #
        # Now create and send an sms to both contacts.
        #
        self.messages.launch()
        self.messages.startNewSMS()
        self.messages.addContactToThisSMS(self.Contact_1["name"])
        self.messages.addContactToThisSMS(self.Contact_2["name"])
        self.messages.enterSMSMsg("Test message.")
        self.messages.sendSMS()
        
        #
        # Wait for all statusbar notifs to arrive.
        # Because both sms's are to this device (via different numbers), both
        # messages will probably end up going to the same thread. So just do a count
        # based on the contact with the short number (since this is the one
        # it always comes to).
        #
        self.marionette.switch_to_frame()
        statusBarCheck = (DOM.Messages.statusbar_new_sms[0], 
                          DOM.Messages.statusbar_new_sms[1] % self.Contact_1["name"])
        
        # Loop for 2 minutes (the 2nd one can take a long time!).
        boolOK = False
        for i in range(1,120):
            # No verification because it's okay if the element's not there yet.
            x = self.marionette.find_elements(*statusBarCheck)
            if len(x) == 2:
                boolOK = True
                break
            
            time.sleep(1)
            
        self.UTILS.TEST(boolOK, "Two messages were returned for this device within 2 minutes (there were " + str(len(x)) + ").")
