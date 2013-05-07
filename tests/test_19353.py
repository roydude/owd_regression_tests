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
import time

class test_19353(GaiaTestCase):
    _Description = "[UTILITY TRAY] As a user, I want to be able to enable/disable Data from the utility tray."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS     = UTILS(self)
        self.Browser   = AppBrowser(self)
                
        #
        # Set timeout for element searches etc...
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()

    
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Data conn icon is not in status bar yet.
        #
        self.UTILS.TEST( self.UTILS.isIconInStatusBar(DOM.Statusbar.dataConn) == False,
                         "Data conn icon is not in statusbar before the test.")
        
        self.UTILS.toggleViaStatusBar(p_data=True)
        
        #
        # Open the browser app. and check we can load a page.
        #
        self.Browser.launch()
        self.Browser.open_url("http://www.google.com")

        self.UTILS.toggleViaStatusBar(p_data=True)
        
        #
        # Data icon is no longer visible in status bar.
        #
        self.UTILS.waitForNotElements(DOM.Statusbar.dataConn, "Data icon in statusbar")
        