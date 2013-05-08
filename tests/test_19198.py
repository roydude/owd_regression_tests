#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest import GaiaTestCase
from OWDTestToolkit import *

#
# Imports particular to this test case.
#

class test_19198(GaiaTestCase):
    _Description = "[SMS] Delete all SMS in a conversation with several sms"
    
    _TestMsg1 = "First message."
    _TestMsg2 = "Second message"
    _TestMsg3 = "Third message"
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS = UTILS(self)
        self.messages = AppMessages(self)
        
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
        
        
    def tearDown(self):
        self.messages.waitForSMSNotifier("222000",10)
        self.UTILS.clearAllStatusBarNotifs()

        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Launch messages app & delete all Threads
        #
        self.messages.launch()
        self.messages.deleteAllThreads()
        
        #
        # Create and send some new tests messages.
        #
        self.messages.createAndSendSMS(self.target_telNum, self._TestMsg1)
        returnedSMS = self.messages.waitForReceivedMsgInThisThread()
        self.messages.enterSMSMsg(self._TestMsg2)
        self.messages.sendSMS()
        returnedSMS = self.messages.waitForReceivedMsgInThisThread()
        self.messages.enterSMSMsg(self._TestMsg3)
        self.messages.sendSMS()
        returnedSMS = self.messages.waitForReceivedMsgInThisThread()
 
        #
        # Go into edit mode..
        #
        x= self.UTILS.getElement( ("id","icon-edit"), "Edit button" )
        self.marionette.tap(x)
        
        #
        # Tap Selected all
        #
        x = self.UTILS.getElement( ("id","messages-check-all-button"), "Sellect all")
        self.marionette.tap(x)

        #
        # Tap delete
        #
        x= self.UTILS.getElement( ("id","messages-delete-button"), "Delete message" )
        self.marionette.tap(x)
        self.marionette.switch_to_frame()        
        x = self.UTILS.getElement(DOM.Messages.confirm_delete_threads, "OK button in question dialog")
        self.marionette.tap(x)
        self.UTILS.switchToFrame(*DOM.Messages.frame_locator)
        time.sleep(2)
        
        #
        # Check conversation isn't there anymore.
        #
        self.UTILS.waitForNotElements(("xpath", DOM.Messages.thread_selector_xpath % self.target_telNum),"Thread")
 
        time.sleep(1)
        self.UTILS.screenShotOnErr()  