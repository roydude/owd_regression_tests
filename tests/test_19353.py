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
        #
        # Open the status bar.
        #
        self.UTILS.displayStatusBar()
        
        #
        # Click on the data connection icon.
        #
        x = self.UTILS.getElement(DOM.Statusbar.toggle_dataconn, "Data conn icon")
        self.marionette.tap(x)
        
        self.UTILS.touchHomeButton()
        
        #
        # Wait for the data conn icon to be visible in the statusbar
        # (can take a while, so try for 2 mins).
        #
        self.UTILS.TEST(self.UTILS.waitForStatusBarNew(DOM.Statusbar.dataConn, 120),
                        "Data conn icon appears in statusbar before timeout.")
        
        #
        # Open the browser app. and check we can load a page.
        #
        self.Browser.launch()
        self.Browser.open_url("http://www.google.com")

        #
        # Open the status bar.
        #
        self.UTILS.displayStatusBar()
        
        #
        # Click on the data connection icon.
        #
        x = self.UTILS.getElement(DOM.Statusbar.toggle_dataconn, "Data conn icon")
        self.marionette.tap(x)
        
        self.UTILS.touchHomeButton()
        
        #
        # Wait for the data conn icon to be visible in the statusbar
        # (can take a while, so try for 2 mins).
        #
        self.UTILS.TEST(self.UTILS.waitForStatusBarNew(DOM.Statusbar.dataConn) == False,
                        "Data conn icon is no longer present in statusbar.")
        
#     def enableViaStatusBar(self, p_wifi=False, p_data=False, p_blueTooth=False, p_airplane=False):
#         #
#         # Enables the items you choose, using the statusbar.
#         #
#         _wifi       = {"name":"wifi", "notif_icon":DOM.Statusbar.wifi, "toggle_icon":DOM.Statusbar.toggle_wifi}
#         _data       = {"name":"data", "notif_icon":DOM.Statusbar.dataConn, "toggle_icon":DOM.Statusbar.toggle_dataconn}
#         _bluetooth  = {"name":"data", "notif_icon":DOM.Statusbar.bluetooth, "toggle_icon":DOM.Statusbar.toggle_bluetooth}
#         _airplane   = {"name":"data", "notif_icon":DOM.Statusbar.airplane, "toggle_icon":DOM.Statusbar.toggle_airplane}
#         
#         _todos = ()
#         if p_wifi: _todos = (_todos, _wifi)
#         if p_data: _todos = (_todos, _wifi)
#         if p_bluetooth: _todos = (_todos, _wifi)
#         if p_airplane: _todos = (_todos, _wifi)
#         
#         for _item in _todos:
#             #
#             # Is this enabled already?
#             #
#             if not self.UTILS.isIconInStatusBar(_item["notif_icon"]):
#                 #
#                 # Click on the toggle icon.
#                 #
#                 x = self.UTILS.getElement(_item["toggle_icon"], 
#                                           "Toggle " + _item["name"] + " icon")
#                 self.marionette.tap(x)
#                 self.UTILS.TEST(self.UTILS.waitForStatusBarNew(DOM.Statusbar.dataConn, 120),
#                             "Data conn icon appears in statusbar before timeout.")
#         
#          