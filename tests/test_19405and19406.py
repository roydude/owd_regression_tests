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
from tests.shared_test_functions import EMAIL_SEND_AND_RECEIVE

class test_19405and19406(GaiaTestCase):
    _Description = "[BASIC][EMAIL] Send and receive email with gmail.com."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS  = UTILS(self)
        
        #
        # Establish parameters.
        #
        self.USER1  = self.UTILS.get_os_variable("GMAIL_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable("GMAIL_1_PASS")
        self.USER2  = self.UTILS.get_os_variable("GMAIL_2_USER")
        self.EMAIL2 = self.UTILS.get_os_variable("GMAIL_2_EMAIL")
        self.PASS2  = self.UTILS.get_os_variable("GMAIL_2_PASS")
        self.UTILS.logComment("Using username 1 '" + self.USER1 + "'")
        self.UTILS.logComment("Using password 1 '" + self.PASS1 + "'")
        self.UTILS.logComment("Using email    1 '" + self.EMAIL1 + "'")
        self.UTILS.logComment("Using username 2 '" + self.USER2 + "'")
        self.UTILS.logComment("Using password 2 '" + self.PASS2 + "'")
        self.UTILS.logComment("Using email    2 '" + self.EMAIL2 + "'")
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.EMAIL  = EMAIL_SEND_AND_RECEIVE.main(self, 
                                                  "19405 and 19406",
                                                  "Sent Mail",
                                                  self.EMAIL1,
                                                  self.USER1,
                                                  self.PASS1,
                                                  self.EMAIL2,
                                                  self.USER2,
                                                  self.PASS2)

        self.EMAIL.run()
