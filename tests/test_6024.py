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

class test_6024(GaiaTestCase):
    _Description = "[SMS] CLONE - Verify The phone number displayed in a conversation."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = AppMessages(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        #
        # Change the settings to vibration only (backdoor method since
        # this isn't what we're testing).
        #
        self.data_layer.set_setting("vibration.enabled", True)
        self.data_layer.set_setting("audio.volume.notification", 0)
        
        #
        # Add contact (with the correct number).
        #
        self.telNum = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Using target telephone number " + self.telNum)

        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch messages app.
        #
        self.messages.launch()
        self.messages.deleteAllThreads()

        #
        # Send a message to create a thread (use number, not name as this
        # avoids some blocking bugs just now). 
        #
        self.messages.createAndSendSMS( [self.telNum], "Test message.")
        returnedSMS = self.messages.waitForReceivedMsgInThisThread()
        
        #
        # Examine the header.
        #
        self.UTILS.headerCheck(self.telNum)

        #
        # Close the thread and check we can find it again with this number.
        #
        self.messages.closeThread()
        self.messages.openThread(self.telNum)