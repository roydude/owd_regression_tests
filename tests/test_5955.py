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

class test_5955(GaiaTestCase):
    _Description = "[SMS] CLONE - Try to send an SMS when the introduced text has been deleted."
    
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
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Start a new sms.
        #
        self.messages.startNewSMS()
        
        #
        # Enter a number in the target field.
        #
        self.messages.addNumberInToField(self.target_telNum)

        #
        # Enter a message the message area.
        #
        x = self.messages.enterSMSMsg("xxx")
        
        #
        # Check the 'Send' button is now enabled.
        #
        x = self.UTILS.getElement(DOM.Messages.send_message_button, "Send message button")
        self.UTILS.TEST(x.is_enabled(), 
                        "Send button is enabled when everything's filled in.")
        
        #
        # Delete the text (we should already be in the message area with the
        # keyboard present, but we need to 'manually' use the keyboard for this).
        #
        orig_frame = self.UTILS.currentIframe()
        self.keyboard.tap_backspace()
        self.keyboard.tap_backspace()
        self.keyboard.tap_backspace()
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame("src", orig_frame)

        x = self.UTILS.getElement(DOM.Messages.input_message_area, "Message area")
        self.UTILS.TEST(x.text == "", "Message area is clear after deleting all characters in it.")

        #
        # Check the 'Send button isn't enabled any more.
        #
        x = self.UTILS.getElement(DOM.Messages.send_message_button, "Send message button")
        self.UTILS.TEST(not x.is_enabled(), 
                        "Send button is not enabled after target number is supplied, but message still empty.")
        
