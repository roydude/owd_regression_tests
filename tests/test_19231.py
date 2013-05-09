#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *


class test_19231(GaiaTestCase):
    _Description = "[HOME SCREEN] Verify that the user can uninstall a everything.me app through the grid edit mode."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.settings   = AppSettings(self)
        self.market     = AppMarket(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Get a conection.
        #
        self.UTILS.getNetworkConnection()
        self.UTILS.uninstallApp("Wikipedia")
                
        #
        # Get the app.
        #
        self.market.launch()
        self.UTILS.TEST(self.market.installApp("Wikipedia", "tfinc"),
                        "App is installed.")
        
        self.UTILS.uninstallApp("Wikipedia")
        
        