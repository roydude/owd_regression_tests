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

class test_4700(GaiaTestCase):
    _Description = "[SMS] Receive an SMS with a link to a web site and open it."
    
    _link        = "www.google.com"
    _TestMsg     = "Test " + _link + " this."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = AppMessages(self)
        self.browser    = AppBrowser(self)
        
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
        
        #
        # Switch to the top level frame and select browser
        # from the popup dialog.
        #
        time.sleep(1)
        self.marionette.switch_to_frame()
        
        x = self.UTILS.getElement( ("xpath", "//a[text()='Browser']"), "Browser button", True, 5, False)
        x.click()
                
        #
        # Give the browser time to start up, then
        # switch to the browser frame and check the page loaded.
        #
        time.sleep(2)
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        
        self.UTILS.TEST(self.browser.check_page_loaded(self._link),
                        "Web page loaded correctly.")
        

