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

class test_19420(GaiaTestCase):
    _Description = "[BASIC][SMS] Receive a sms with vibration (device unlocked) & confirm notification - verify that the notification is fired and that you can see the message received from the other phone."
    
    _TestMsg     = "Test message."
    
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
        # Establish which phone number to use.
        #
        self.target_telNum = self.UTILS.get_os_variable("GLOBAL_TARGET_SMS_NUM")
        self.UTILS.logComment("Sending sms to telephone number " + self.target_telNum)
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Start by making sure we have no other notifications.
        #
        self.UTILS.clearAllStatusBarNotifs()
        
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Delete all threads.
        #
        self.messages.deleteAllThreads()
          
        #
        # Create and send a new test message (don't use api - I want to be back in homepage
        # before the sms has finshed sending and the api waits).
        #
        newMsgBtn = self.UTILS.getElement(DOM.Messages.create_new_message_btn, "Create new message button")
        self.marionette.tap(newMsgBtn)
        numInput = self.UTILS.getElement(DOM.Messages.target_number, "Target number field")
        numInput.send_keys(self.target_telNum)
        self.messages.enterSMSMsg(self._TestMsg)
        
        # This wasn't always quick enough so I'm trying js to make it faster ...
#         sendBtn = self.UTILS.getElement(DOM.Messages.send_message_button, "Send sms button")
#         self.marionette.tap(sendBtn)        
        self.marionette.execute_script("document.getElementById('" + \
                                             DOM.Messages.send_message_button[1] + \
                                             "').click();")
        
        #
        # Bit of a race: QUICKLY go 'home' and wait for the notifier.
        # If we're not quick enough the returned sms will arrive while we're still in
        # messaging, in which case the statusbar notifier will never appear.
        #
        self.UTILS.goHome()
        self.messages.waitForSMSNotifier(self.target_telNum)
        
        #
        # Click the notifier.
        #
        self.messages.clickSMSNotifier(self.target_telNum)
          
        #
        # Wait for the last message in this thread to be a 'recieved' one.
        #
        returnedSMS = self.messages.waitForReceivedMsgInThisThread(30)
        self.UTILS.TEST(returnedSMS, "A receieved message appeared in the thread.", True)
          
        #
        # TEST: The returned message is as expected (caseless in case user typed it manually).
        #
        sms_text = returnedSMS.text
        self.UTILS.TEST((sms_text.lower() == self._TestMsg.lower()), 
            "SMS text = '" + self._TestMsg + "' (it was '" + sms_text + "').")
         
        x = self.UTILS.getElement(("id","messages-back-button"), "x")
        self.marionette.tap(x)
        
        #
        # Check the message via the thread.
        #
        self.messages.openThread(self.target_telNum)
        
        #
        # TEST: The returned message is as expected (caseless in case user typed it manually).
        #
        sms_text = returnedSMS.text
        self.UTILS.TEST((sms_text.lower() == self._TestMsg.lower()), 
            "SMS text = '" + self._TestMsg + "' (it was '" + sms_text + "').")

