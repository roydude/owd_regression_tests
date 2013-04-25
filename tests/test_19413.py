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

class test_19413(GaiaTestCase):
    _Description = "[BASIC][BROWSER] Load a website via Cellular Data - verify the site loads in the browser correctly."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Settings   = AppSettings(self)
        self.Browser    = AppBrowser(self)
        self.testURL    = self.UTILS.get_os_variable("GLOBAL_TEST_URL")
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        self.UTILS.logComment("Using " + self.testURL)
        
        self.data_layer.disable_wifi()
        self.data_layer.disable_cell_data()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Wifi needs to be off for this test to work.
        #
        self.Settings.turn_dataConn_on()
        
        #
        # Open the browser app.
        #
        self.Browser.launch()
        
        #
        # Open our URL.
        #
        self.Browser.open_url(self.testURL)
        

