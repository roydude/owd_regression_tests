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

class test_4708(GaiaTestCase):
    _Description = "[SMS] Receive an SMS with a phone number and store it."

    _testNum = "089123456"
    _TestMsg = "Testing " + _testNum + " number."
    
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = AppMessages(self)
        self.phone      = AppPhone(self)
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
        # Establish which phone number to use.
        #
        self.target_telNum = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Sending sms to telephone number " + self.target_telNum)
        
        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.UTILS.getNetworkConnection()
        
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Make sure it's empty first.
        #
        self.messages.deleteAllThreads()
         
        #
        # Create and send a new test message.
        #
        self.messages.createAndSendSMS([self.target_telNum], self._TestMsg)
        
        #
        # Wait for the last message in this thread to be a 'recieved' one
        # and click the link.
        #
        x = self.messages.waitForReceivedMsgInThisThread()
        x.find_element("tag name", "a").click()        
        
        time.sleep(5)
        
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Phone.frame_locator_from_sms)
        
        #
        # Create a contact from this number.
        #
        self.phone.createContactFromThisNum()

        #
        # Make sure the number is automatically in the contact details.
        #        
        x = self.UTILS.getElement( ("id", "number_0"), "Mobile number field")
        self.UTILS.TEST(x.get_attribute("value") == self._testNum, 
                        "The correct number is automatically entered in the new contact's number field.")