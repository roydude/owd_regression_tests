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
import time

class test_19181(GaiaTestCase):
    _Description = "[CONTACTS] Remove a photo,a phone number, an email, an address and a comment from a contact and restore the phone number and the comment."

    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.contacts   = AppContacts(self)
        self.settings   = AppSettings(self)
                
        #
        # Set timeout for element searches.
        #
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
 
        #
        # Get details of our test contacts.
        #
        self.Contact_1 = MockContacts().Contact_1
        self.data_layer.insert_contact(self.Contact_1)
        self.UTILS.addFileToDevice('./tests/resources/contact_face.jpg', destination='DCIM/100MZLLA')
          
        #
        # Launch contacts app.
        #
        self.contacts.launch()
          
        #
        # View our contact.
        #
        self.contacts.viewContact(self.Contact_1['name'])
          
        #
        # Edit our contact.
        #
        self.contacts.pressEditContactButton()
          
        #
        # Give our contact a photo.
        #
        self.contacts.addGalleryImageToContact(0)

    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        self.UTILS.logResult("info", "*** Switching 'reset' mode ON ... ***")
        self.toggle_reset_button("phone")
        self.check_kbd_appears("number", "phone number", False)
        self.UTILS.logResult("info", "*** Switching 'reset' mode OFF ... ***")
        self.toggle_reset_button("phone")
        self.check_kbd_appears("number", "phone number", True)
        
        self.UTILS.logResult("info", "*** Switching 'reset' mode ON ... ***")
        self.toggle_reset_button("email")
        self.check_kbd_appears("email", "email", False)
        self.UTILS.logResult("info", "*** Switching 'reset' mode OFF ... ***")
        self.toggle_reset_button("email")
        self.check_kbd_appears("email", "email", True)
        
        self.UTILS.logResult("info", "*** Switching 'reset' mode ON ... ***")
        self.toggle_reset_button("address")
        self.check_kbd_appears("streetAddress", "address", False)
        self.UTILS.logResult("info", "*** Switching 'reset' mode OFF ... ***")
        self.toggle_reset_button("address")
        self.check_kbd_appears("streetAddress", "address", True)
        
        self.UTILS.logResult("info", "*** Switching 'reset' mode ON ... ***")
        self.toggle_reset_button("comment")
        self.check_kbd_appears("note", "comment", False)
        self.UTILS.logResult("info", "*** Switching 'reset' mode OFF ... ***")
        self.toggle_reset_button("comment")
        self.check_kbd_appears("note", "comment", True)

        self.UTILS.logResult("info", "*** Switching 'reset' mode ON ... ***")
        self.toggle_reset_button("photo")
        self.check_photo_tap(False)
        self.UTILS.logResult("info", "*** Switching 'reset' mode OFF ... ***")
        self.toggle_reset_button("photo")
        self.check_photo_tap(True)
        
    def check_photo_tap(self, p_boolEditable):
        
        # Check tapping photo (same link for add and edit)
        _comment = "Photo is " + ("not " if not p_boolEditable else "")
        x = self.UTILS.getElement(DOM.Contacts.add_photo, "Photo")
        self.UTILS.TEST(x.is_enabled() == p_boolEditable, _comment + "enabled.")
        self.marionette.tap(x)
        time.sleep(1)
            
        self.marionette.switch_to_frame()
            
        boolED=False
        try:
            x = self.marionette.find_element(*DOM.Contacts.photo_from_gallery)
            x = self.marionette.find_element(*DOM.Contacts.cancel_photo_source)
            self.marionette.tap(x)
            boolED = True
        except:
            boolED=False
        self.UTILS.TEST(boolED == p_boolEditable, _comment + "editable.")
           
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Contacts.frame_locator)

        
    def toggle_reset_button(self, p_el):
        #
        # Press reset button on the required fields ...
        #
        reset_btn = DOM.Contacts.reset_field_xpath
        
        if p_el == "photo":
            x = self.UTILS.getElement(("xpath",reset_btn % "thumbnail-action"), "Photo reset button")
            self.marionette.tap(x)
          
        if p_el == "phone":
            x = self.UTILS.getElement(("xpath",reset_btn % "add-phone-0"), "Phone reset button")
            self.marionette.tap(x)
          
        if p_el == "email":
            x = self.UTILS.getElement(("xpath",reset_btn % "add-email-0"), "Email reset button")
            self.marionette.tap(x)
           
        if p_el == "address":
            x = self.UTILS.getElement(("xpath",reset_btn % "add-address-0"), "Address reset button")
            self.marionette.tap(x)
           
        if p_el == "comment":
            x = self.UTILS.getElement(("xpath",reset_btn % "add-note-0"), "Comment reset button")
            self.marionette.tap(x)
        
    def check_kbd_appears(self, p_elItem, p_desc, p_KBD_displayed):
        #
        # Taps the field and checks to see if the keyboard appears.
        # When marionette "is_enabled()" is working , we can forget all this.
        #
        _comment = "The " + p_desc + " field can " + ("not " if not p_KBD_displayed else "") + "be edited."

        x = self.UTILS.getElement(("id", "%s_0" % p_elItem), "Field for " + p_desc)
#         self.UTILS.TEST(x.is_enabled() == p_KBD_displayed, _comment + "enabled.")
#         return
    
        # ROY - from here on does the keyboard verification .....
        # The problem is that the keyboard frame is always present
        # once it's been launched, so I need a way to either KILL
        # the keyboard, or see what's currently displayed.
        x.click()
        
        boolKBD=False
        self.marionette.switch_to_frame()
        x = self.marionette.find_element("xpath", 
                                         "//iframe[@" + DOM.GLOBAL.keyboard_iframe[0]+ \
                                         "='" + DOM.GLOBAL.keyboard_iframe[1] + "']")
        if x.is_displayed():
            boolKBD = True
        else:
            boolKBD=False
        self.UTILS.TEST(boolKBD == p_KBD_displayed, _comment)
        
        #
        # Return to the contacts iframe.
        #
        self.marionette.switch_to_frame()
        self.UTILS.switchToFrame(*DOM.Contacts.frame_locator)
        
        #
        # Tap the header to remove the keyboard.
        #
        x = self.marionette.find_element(*DOM.GLOBAL.app_head)
        x.click()
        
        
        
        