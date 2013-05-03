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

class test_19241(GaiaTestCase):
    _Description = "[EMAIL] Basic: Deleting of a e-mail in Inbox."
 
    def setUp(self):
            
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Email      = AppEmail(self)
        
        #
        # Set the timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

    def tearDown(self):
        self.UTILS.reportResults()

    def test_run(self):
        AppSettings(self).getNetworkConnection()

        self.USER1  = self.UTILS.get_os_variable("GMAIL_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable("GMAIL_1_PASS")
        
        self.UTILS.logComment("Using username 1 '" + self.USER1 + "'")
        self.UTILS.logComment("Using password 1 '" + self.PASS1 + "'")
        self.UTILS.logComment("Using email    1 '" + self.EMAIL1 + "'")

        #
        # Launch Email app.
        #
        self.Email.launch()
                
        #
        # Login.
        #
        self.Email.setupAccount(self.USER1, self.EMAIL1, self.PASS1)
        
        #
        # Return to the Inbox.
        #
        self.Email.openMailFolder("Inbox")
        
        #
        # Delete the first email we come across.
        #
        _subject = self.marionette.find_elements(*DOM.Email.folder_subject_list)[0].text
        self.UTILS.logComment("Deleting email with subject '" + _subject + "'.")

        self.Email.deleteEmail(_subject)