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

class main(GaiaTestCase):

    def setUpEmail(self):
        
        GaiaTestCase.setUp(self)
        self.UTILS  = UTILS(self)
        
        self.USER1  = self.UTILS.get_os_variable(self.testType.upper() + "_1_USER")
        self.EMAIL1 = self.UTILS.get_os_variable(self.testType.upper() + "_1_EMAIL")
        self.PASS1  = self.UTILS.get_os_variable(self.testType.upper() + "_1_PASS")
        self.USER2  = self.UTILS.get_os_variable(self.testType.upper() + "_2_USER")
        self.EMAIL2 = self.UTILS.get_os_variable(self.testType.upper() + "_2_EMAIL")
        self.PASS2  = self.UTILS.get_os_variable(self.testType.upper() + "_2_PASS")
        
        self.UTILS.logComment("Using username 1 '" + self.USER2 + "'")
        self.UTILS.logComment("Using password 1 '" + self.PASS2 + "'")
        self.UTILS.logComment("Using email    1 '" + self.EMAIL2 + "'")
        self.UTILS.logComment("Using username 2 '" + self.USER1 + "'")
        self.UTILS.logComment("Using password 2 '" + self.PASS1 + "'")
        self.UTILS.logComment("Using email    2 '" + self.EMAIL1 + "'")

        self.Email      = AppEmail(self)
        self.settings   = AppSettings(self)
        
        #
        # Set up specific folder names.
        #
        self.UTILS.logComment("Non-gmail account being used.")
        self.sentFoldername = "Sent"
        
        if "gmail" in self.testType.lower():
            self.UTILS.logComment("Gmail account being used.")
            self.sentFolderName = "Sent Mail"
        
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
        
        #
        # Make sure we have some data connectivity.
        #
        self.settings.getNetworkConnection()
        
    def send_email(self):
        
        self.setUpEmail()


        #
        # We're sending, so create (and record) a unique 'subject'.
        #
        self.subject    = self.testNum + " - " + str(time.time())
        self.body       = "This is the test email body."
        
        self.UTILS.logComment("Using subject \"" + self.subject + "\".")
                
        #
        # Keep the subject in a file so the next test (receive email)
        # can see what subject to search for.
        #
        SUBJECT_FILE = open(os.environ['RESULT_DIR'] + "/.email_subject", "w")
        SUBJECT_FILE.write(self.subject)
        SUBJECT_FILE.close()
          
                          
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
        time.sleep(10)
        self.UTILS.TEST(self.Email.emailIsInFolder(self.subject),
            "Email '" + self.subject + "' found in the Sent folder.", False)
        

    def receive_email(self):

        self.setUpEmail()

        #
        # Get the unique 'subject'.
        #
        try:
            SUBJECT_FILE = open(os.environ['RESULT_DIR'] + "/.email_subject", "r")
        except:
            self.UTILS.logResult(False, "Email subject file was not found - this test should only be run in conjunction with a 'send email' test.")
            self.UTILS.quitTest()
             
        self.subject = SUBJECT_FILE.read()
        SUBJECT_FILE.close()
        self.UTILS.logComment("Using subject \"" + self.subject + "\".")
                
        #
        # Launch Email app.
        #
        self.Email.launch()
         
        #   
        # Login.
        #
        self.Email.setupAccount(self.USER2, self.EMAIL2, self.PASS2)
             
        #
        # Open the email.
        #
        self.UTILS.TEST(self.Email.openMsg(self.subject),
            "Email was opened successfully.", True)
         
        #
        # Verify the contents - the email address is shortened to just the name (sometimes!).
        #
        email1_name = self.EMAIL1.split("@")[0]
        email2_name = self.EMAIL2.split("@")[0]
         
        x = self.UTILS.getElement(DOM.Email.open_email_from, "'From' field")
         
        self.UTILS.TEST((x.text == self.EMAIL1 or x.text == email1_name), 
            "'From' field = '" + self.EMAIL1 + "' (it was '" + x.text + "').")
 
        x = self.UTILS.getElement(DOM.Email.open_email_to, "'To' field")
        self.UTILS.TEST((x.text == self.EMAIL2 or x.text == email2_name), 
            "'To' field = '" + self.EMAIL2 + "', (it was '" + x.text + "').")
 
        x = self.UTILS.getElement(DOM.Email.open_email_subject, "'Subject' field")
        self.UTILS.TEST(x.text == self.subject, 
            "'From' field = '" + self.subject + "', (it was '" + x.text + "').")
         

