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

class test_19199(GaiaTestCase):
    _Description = "[SMS] Delete a SMS in a conversation with several sms"
    
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
        returnedSMS = self.messages.waitForReceivedMsgInThisThread(30)
        self.messages.enterSMSMsg(self._TestMsg2)
        self.messages.sendSMS()
        returnedSMS = self.messages.waitForReceivedMsgInThisThread(30)
        self.messages.enterSMSMsg(self._TestMsg3)
        self.messages.sendSMS()
        returnedSMS = self.messages.waitForReceivedMsgInThisThread(30)

        #
        # Check how many elements are there
        #
        x = self.UTILS.getElements(DOM.Messages.thread_messages,"Messages")
        original_count = len(x)
        self.UTILS.logResult("info", 
                             "Before deleting the message, there were " + str(original_count) + " messages in this thread")
        
        #
        # Go into edit mode..
        #
        x= self.UTILS.getElement(DOM.Messages.edit_messages_icon, "Edit button" )
        self.marionette.tap(x)
        
        #
        # Check the thread.
        #
        x = self.UTILS.getElements(DOM.Messages.thread_messages, "Messages")
        self.marionette.tap(x[0])
        
        #
        # Tap delete
        #
        x= self.UTILS.getElement(DOM.Messages.delete_messages_button, "Delete message" )
        self.marionette.tap(x)
        
        self.marionette.switch_to_frame()
        x = self.UTILS.getElement(DOM.Messages.confirm_delete_threads, "OK button in question dialog")
        self.marionette.tap(x)
        self.UTILS.switchToFrame(*DOM.Messages.frame_locator)
        time.sleep(2)
        
        #
        # Check message isn't there anymore.
        #
        x = self.UTILS.getElements(DOM.Messages.thread_messages,"Messages")
        final_count = len(x)
        real_count= original_count-1
        self.UTILS.TEST(final_count == (original_count-1), 
                        "After deleting the message, there were " + \
                        str(real_count) + \
                        " messages in this thread (" + str(final_count) + " found).")      