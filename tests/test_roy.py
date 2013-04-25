#
# Runs through composing and sending an email as one user, then
# receiving it as another user.
#
# As I can't see ANY different between read and unread emails in the html,
# I need to rely on a totally unique subject line to identify the precise
# message sent between the two test accounts.
# Because of this I need to stay in the same python instance to remember
# the subject line I generated (and guarantee 100% that 24 ran before 25).
#
# Currently used by tests 22, 23, 24 and 25 (combined to 22 and 24).
#

#
# Imports which are standard for all test cases.
#
import sys
sys.path.insert(1, "./")
from marionette import Marionette
from gaiatest   import GaiaTestCase
from OWDTestToolkit import *
#
# Imports particular to this test case.
#
import os, time

class test_19405and19406(GaiaTestCase):
    _Description = "[BASIC][EMAIL] Send and receive email with gmail.com."
    
    def setUp(self):
        #
        # Set up child objects...
        #
        GaiaTestCase.setUp(self)
        self.UTILS  = UTILS(self)
        
        #
        # Establish parameters.
        #
        self.USER1  = self.UTILS.get_os_variable("GMAIL_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable("GMAIL_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable("GMAIL_1_PASS")
        self.USER2  = self.UTILS.get_os_variable("GMAIL_2_USER")
        self.EMAIL2 = self.UTILS.get_os_variable("GMAIL_2_EMAIL")
        self.PASS2  = self.UTILS.get_os_variable("GMAIL_2_PASS")
        self.UTILS.logComment("Using username 1 '" + self.USER1 + "'")
        self.UTILS.logComment("Using password 1 '" + self.PASS1 + "'")
        self.UTILS.logComment("Using email    1 '" + self.EMAIL1 + "'")
        self.UTILS.logComment("Using username 2 '" + self.USER2 + "'")
        self.UTILS.logComment("Using password 2 '" + self.PASS2 + "'")
        self.UTILS.logComment("Using email    2 '" + self.EMAIL2 + "'")
                     
        #
        # Establish parameters.
        #
        self.body           = "This is the test email body."
        self.sentFolderName = "Sent Mail"
        self.Email          = AppEmail(self)
        self.settings       = AppSettings(self)
        self.subject        = "Test roy - " + str(time.time())

        self.UTILS.logComment("Using subject \"" + self.subject + "\".")
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):

        #
        # Make sure we have some data connectivity.
        #
        self.settings.getNetworkConnection()
        
        ##################################################
        #
        # SEND EMAIL
        
        #
        # Launch Email app.
        #
        self.Email.launch()
                
        #
        # Login.
        #
        self.Email.setupAccount(self.USER1, self.EMAIL1, self.PASS1)
        
        #
        # Return to the Inbox.
        #
        self.Email.openMailFolder("Inbox")
                
        #
        # At the inbox, compose a new email.
        #
        self.Email.send_new_email(self.EMAIL2, self.subject, self.body)

        #
        # Check our email is in the sent folder.
        #
        self.Email.openMailFolder(self.sentFolderName)
        self.UTILS.TEST(self.Email.emailIsInFolder(self.subject),
            "Email '" + self.subject + "' found in the Sent folder.")
        
# 
#         ##################################################
#         #
#         # RECEIVE EMAIL
#         
#         #
#         # Launch Email app.
#         #
#         self.Email.launch()
#         
#         #   
#         # Login.
#         #
#         self.Email.setupAccount(self.USER2, self.EMAIL2, self.PASS2)
#             
#         #
#         # Open the email.
#         #
#         self.UTILS.TEST(self.Email.openMsg(self.subject),
#             "Email was opened successfully.", True)
#         
#         #
#         # Verify the contents - the email address is shortened to just the name (sometimes!).
#         #
#         email1_name = self.EMAIL1.split("@")[0]
#         email2_name = self.EMAIL2.split("@")[0]
#         
#         x = self.UTILS.getElement(DOM.Email.open_email_from, "'From' field")
#         
#         self.UTILS.TEST((x.text == self.EMAIL1 or x.text == email1_name), 
#             "'From' field = '" + self.EMAIL1 + "' (it was '" + x.text + "').")
# 
#         x = self.UTILS.getElement(DOM.Email.open_email_to, "'To' field")
#         self.UTILS.TEST((x.text == self.EMAIL2 or x.text == email2_name), 
#             "'To' field = '" + self.EMAIL2 + "', (it was '" + x.text + "').")
# 
#         x = self.UTILS.getElement(DOM.Email.open_email_subject, "'Subject' field")
#         self.UTILS.TEST(x.text == self.subject, 
#             "'From' field = '" + self.subject + "', (it was '" + x.text + "').")
#         

