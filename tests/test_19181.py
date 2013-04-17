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
        # Set up to use data connection.
        #        
        self.settings.turn_dataConn_on_if_required()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        
        self.UTILS.TEST(False, "Force fail at the moment - problems with gallery images via contacts.", True)
        
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
        
        #
        # Reset the fields ...
        #
        reset_btn = DOM.Contacts.reset_field_xpath
        
        # Photo
        x = self.UTILS.getElement(("xpath",reset_btn % "thumbnail-action"), "Photo reset button")
        self.marionette.tap(x)
        
        # Phone number
        x = self.UTILS.getElement(("xpath",reset_btn % "add-phone-0"), "Phone reset button")
        self.marionette.tap(x)
        
        # Email
        x = self.UTILS.getElement(("xpath",reset_btn % "add-email-0"), "Email reset button")
        self.marionette.tap(x)
        
        # Address
        x = self.UTILS.getElement(("xpath",reset_btn % "add-address-0"), "Address reset button")
        self.marionette.tap(x)
        
        # Comment
        x = self.UTILS.getElement(("xpath",reset_btn % "add-note-0"), "Comment reset button")
        self.marionette.tap(x)
        
        
        #
        # Test each field that's been reset cannot be edited.
        #
        
        # Photo
        x = self.UTILS.getElement(DOM.Contacts.edit_photo, "'Edit photo' link")
        self.marionette.tap(x)
        time.sleep(2)
         
        self.marionette.switch_to_frame()
         
        boolNotDisplayed=False
        try:
            x = self.marionette.find_element(*DOM.Contacts.photo_from_gallery)
            if not x.is_displayed():
                boolNotDisplayed = True
        except:
            boolNotDisplayed=True
        self.UTILS.TEST(boolNotDisplayed, "Edit photo options not displayed.")
        
        self.UTILS.switchToFrame(*DOM.Gallery.frame_locator)

        # Phone number
        x = self.UTILS.getElement(("id", "number_0"), "Phone number field")
        x.send_keys("XXX")
#         if x.value == XXX???
        