from gaiatest import GaiaTestCase

class test_roy(GaiaTestCase):

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
            
    def tearDown(self):
        return
        
    def test_run(self):
        #
        # Launch contacts app.
        #
        self.app = self.apps.launch('Messages')
        self.wait_for_element_not_displayed('id', 'loading-overlay')
        
        newMsgBtn = self.marionette.find_element('id', 'icon-add')
        self.marionette.tap(newMsgBtn)
        
        #
        # Enter the number.
        #
        self.wait_for_element_displayed('id', 'messages-recipient')
        numInput = self.marionette.find_element('id', 'messages-recipient')
        if numInput.is_displayed():
            print "IT IS DISPLAYED"
        else:
            print "IT IS NOT DISPLAYED"
            
# (Switching the frame also doesn't work.)
#         self.marionette.switch_to_frame()
#         x=self.marionette.find_element("xpath", "//*[@src='app://sms.gaiamobile.org/index.html']")
#         self.marionette.switch_to_frame(x)
# 
#         numInput = self.marionette.find_element('id', 'messages-recipient')

        numInput.send_keys('123456')