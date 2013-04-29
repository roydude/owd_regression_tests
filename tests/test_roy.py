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

class test_19205(GaiaTestCase):
    _Description = "(Roy testing something - ignore this)."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Email   = AppEmail(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        self.USER1  = self.UTILS.get_os_variable("GMAIL_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable("GMAIL_1_PASS")
        self.USER2  = self.UTILS.get_os_variable("GMAIL_2_USER")
        self.EMAIL2 = self.UTILS.get_os_variable("GMAIL_2_EMAIL")
        self.PASS2  = self.UTILS.get_os_variable("GMAIL_2_PASS")
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.Email.launch()
        
        self.Email.setupAccount(self.USER1, self.EMAIL1, self.PASS1)
        