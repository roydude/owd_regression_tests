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
from tests.mock_data.contacts import MockContacts

class test_19403(GaiaTestCase):
    _Description = "[BASIC][SYSTEM] With two apps already running, launch the card view, kill one app process, and launch the other - verify the app killed is stopped and the other app starts up."

    _test_apps = ["Gallery", "FM Radio"]
    _img_list  = ('img1.jpg', 'img2.jpg')
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)

        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()

    def test_run(self):
        #
        # Load a couple of images into the gallery.
        #
        for i in self._img_list:
            self.UTILS.addFileToDevice('./tests/resources/' + i, destination='DCIM/100MZLLA')
    
        self.UTILS.goHome()
        
        #
        # launch the test apps (lifted directly from gaiatest).
        #
        self.test_apps = []
        for app in self._test_apps:
            app1 = app.split(" ")[0].lower()
            test_app = {
                'name'        : app,
                'app'         : self.apps.launch(app),
                'card'        : (DOM.Home.app_card[0], DOM.Home.app_card[1] % app1),
                'close_button': (DOM.Home.app_close[0], DOM.Home.app_close[1] % app1)
            }
            self.test_apps.append(test_app)
            self.UTILS.touchHomeButton()
            time.sleep(1)
        
        self.UTILS.holdHomeButton()
        
        x = self.UTILS.getElement(DOM.Home.cards_view, "App 'cards' list")
        
        #
        # Flick it up (not working currently - retry when marionette toch is working).
        #
# #         x = self.UTILS.getElement(*self.test_apps[len(self.test_apps)-1]["card"])
#         els = self.marionette.find_elements(*DOM.Home.app_cards)
#         from marionette import Actions
#         actions = Actions(self.marionette)
#         for x in els:
#             actions.press(x, x.size["width"], x.size["height"]).move_by_offset(x.size["width"], 0).release()
#             actions.perform()
#             
# #             x_x = int(x.size['width'] / 2)
# #             x_y = int(x.size['height'] / 2)
# #             self.marionette.flick(x, x_x, x_y, x_x, 0, 500)
        
        #
        # For now just click the close_button
        #
        self.UTILS.logComment("(Didn't drag the app 'up' to close it, I just clicked the 'close' button.)")
        self.UTILS.logResult(False, "NOTE: Need to launch 2nd app, not kill it!")
        i = 0
        for app in self._test_apps:
            x = self.UTILS.getElement(self.test_apps[i]["close_button"], "Close button on '" + self.test_apps[i]["name"] + "' card")
            self.marionette.tap(x)
 
            self.UTILS.waitForNotElements(self.test_apps[i]["card"], "Card for '" + self.test_apps[i]["name"] + "'", True, 5, False)
            i = i + 1

