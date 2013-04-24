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

class test_19421(GaiaTestCase):
    _Description = "[BASIC][CONTACTS] Send an sms from a contact detail - Verify the contact receives the SMS."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.messages   = AppMessages(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
            
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
#         self.messages.removeAllThreads()
        
        self.UTILS.clearAllStatusBarNotifs()
        
