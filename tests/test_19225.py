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

class test_19225(GaiaTestCase):
    _Description = "[HOME SCREEN] Verify that if no connection available when selecting a category in everything.me the user will be notified about the need to have a network connection to use this functionality."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        
        self.UTILS      = UTILS(self)
        self.EME        = AppEverythingMe(self)
        self.Settings   = AppSettings(self)
        
        self.marionette.set_search_timeout(50)
        self.data_layer.disable_cell_data()
        self.data_layer.disable_wifi()
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Dug to a bug, the message only appears if you 
        # have used eme with a network connection first,
        # but not if the first time you use eme is without
        # a network connection. So test for both situations.
        #

        #
        # Launch the 'everything.me' app.
        #
        self.UTILS.logResult("info", "Launching EME with NO network connection first ...")
        self.EME.launch()
        
        #
        # Select a category (group).
        #
        self.EME.pickGroup("Games")
        
        #
        # Verify that the message is displayed.
        #
        self.UTILS.waitForElements(DOM.EME.connection_warning_msg, 
                                   "Connection message (without using with a network first)",
                                   True, 30, False)
        
        #
        # Return home, turn on networking navigate to the group again, then return home.
        #
        self.UTILS.logResult("info", "Using EME with networking ...")
        self.UTILS.scrollHomescreenRight()
        self.UTILS.getNetworkConnection()
        self.EME.launch()
        self.EME.pickGroup("Local")
        self.UTILS.scrollHomescreenRight()
 
        #
        # Turn networking off and launch the 'everything.me' app again.
        #
        self.data_layer.disable_cell_data()
        self.data_layer.disable_wifi()
        self.UTILS.logResult("info", "Launching EME with NO network connection (after being used WITH a network connection) ...")
        self.EME.launch()
         
        #
        # Select a category (group).
        #
        self.EME.pickGroup("Music")
         
        #
        # Verify that the message is displayed.
        #
        self.UTILS.waitForElements(DOM.EME.connection_warning_msg, 
                                   "Connection message (after using with a network)",
                                   True, 30, False)
         
