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

class test_19224(GaiaTestCase):
    _Description = "[HOME SCREEN] Add and remove categories to everything.me grid."
    
    _newGroup = "Sports"
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        
        self.UTILS      = UTILS(self)
        self.Settings   = AppSettings(self)
        self.EME        = AppEverythingMe(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        return
        #
        # Make sure 'things' are as we expect them to be first.
        #
        self.UTILS.getNetworkConnection()

        #
        # Launch the 'everything.me' app.
        #
        self.UTILS.logResult("info", "Launching EME ...")
        self.EME.launch()
        
        #
        # Make sure our group isn't already present.
        #
        self.EME.removeGroup(self._newGroup)       
        
        #
        # Add the group.
        #
        self.EME.addGroup(self._newGroup)
            
        #
        # Remove the group.
        #
        self.EME.removeGroup(self._newGroup)
        
        