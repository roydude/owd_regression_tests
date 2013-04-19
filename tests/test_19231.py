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
        self.market     = AppMarket(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        #
        # Get a conection.
        #
        self.connect_to_network()
        self.UTILS.uninstallApp("Wikipedia")
                
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Get the app.
        #
        self.market.launch()
        self.UTILS.TEST(self.market.install_app("Wikipedia", "tfinc"),
                        "App is installed.")
        
        self.UTILS.uninstallApp("Wikipedia")
        
        