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

class test_19400(GaiaTestCase):
    _Description = "[BASIC][HOMESCREEN] Delete a packaged app - verify the app was successfully removed from the homescreen."
    
    _URL         = "http://everlong.org/mozilla/packaged/"
    _appName     = "cool packaged app"
    _appOK       = True
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.Settings   = AppSettings(self)
        self.Browser    = AppBrowser(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        #
        # Uninstall the app (if need be).
        #
        if self.UTILS.findAppIcon(self._appName):
            self.UTILS.uninstallApp(self._appName)
        
        #
        # Ensure we have a connection.
        #
        self.UTILS.getNetworkConnection()
        
        #
        # Open the browser app.
        #
        self.Browser.launch()
        
        #
        # Open our URL.
        #
        self.Browser.open_url(self._URL)
        
        #
        # Install the app.
        #
        x = ('id', 'install-app')        
        install_btn = self.UTILS.getElement(x, "Install an app button")
        self.marionette.tap(install_btn)
        
        # Install button on the splash screen (switch to main frame to 'see' this).
        self.marionette.switch_to_frame()

        x = ('id', 'app-install-install-button')        
        install_btn = self.UTILS.getElement(x, "Install button")
        self.marionette.tap(install_btn)
        
        # ... and switch back to brwoser to see the next splash screen(!)
        self.UTILS.switchToFrame(*DOM.Browser.frame_locator)
        x = ('id', 'modal-dialog-alert-ok')
        btn = self.UTILS.getElement(x, "Ok button")
        self.marionette.tap(btn)

        #
        # Go back to the home page and check the app is installed.
        #
        self.UTILS.TEST(self.UTILS.findAppIcon(self._appName), "App icon is present in the homescreen.")
                
        #
        # Remove the app.
        #
        self.UTILS.uninstallApp(self._appName)
