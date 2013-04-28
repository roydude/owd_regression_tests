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
from tests.mock_data.contacts import MockContacts

class test_19201(GaiaTestCase):
    _Description = "[SMS] Select some conversations and press delete."
    
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
        # Prepare the contact we're going to insert.
        #
        self.contact_1 = MockContacts().Contact_1
        self.contact_2 = MockContacts().Contact_2
        self.contact_3 = MockContacts().Contact_longName
        
        #
        # Add this contact (quick'n'dirty method - we're just testing sms, no adding a contact).
        #
        self.data_layer.insert_contact(self.contact_1)
        self.data_layer.insert_contact(self.contact_2)
        self.data_layer.insert_contact(self.contact_3)
        
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Launch messages app.
        #
        self.messages.launch()
        
        #
        # Make sure we have no threads before we start.
        #
        self.messages.deleteAllThreads()
        
        #
        # Create and send a new test message.
        #
        self.messages.createAndSendSMS(self.contact_1["tel"]["value"], self._TestMsg)
        x = self.UTILS.getElement(DOM.Messages.header_back_button, "Back button")
        self.marionette.tap(x)
        self.messages.createAndSendSMS(self.contact_2["tel"]["value"], self._TestMsg)
        x = self.UTILS.getElement(DOM.Messages.header_back_button, "Back button")
        self.marionette.tap(x)
        self.messages.createAndSendSMS(self.contact_3["tel"]["value"], self._TestMsg)
        x = self.UTILS.getElement(DOM.Messages.header_back_button, "Back button")
        self.marionette.tap(x)
        
        #
        # Delete all threads, except the last one.
        #
        x = self.UTILS.getElement(DOM.Messages.edit_threads_button, "Edit threads button")
        self.marionette.tap(x)
        
        x = self.UTILS.getElements(DOM.Messages.threads, "Message thread checkboxes")
        for i in range(0,len(x)-1):
            self.marionette.tap(x[i])
        
        self.messages.deleteSelectedThreads()
        
        #
        # Check there is now only 1 thread.
        #
        x = self.UTILS.getElements(DOM.Messages.threads, "Message thread checkboxes")
        self.UTILS.TEST(len(x) == 1, "Only 1 thread is left after deleting the other two.")
        
        #
        # The message notifier returned by the weird 'you have sent a text' text
        # remains in the header unless we clear it.
        #
        time.sleep(10) # (in case we don't get a message in the statusbar)
        self.UTILS.clearAllStatusBarNotifs()
