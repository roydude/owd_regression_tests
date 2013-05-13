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

class test_19417(GaiaTestCase):
    _Description = "[BASIC][VIDEO] Play the video you recorded, check for video and sound to verify the video could be successfully played."
    
    def setUp(self):
        #
        # Set up child objects.
        #
        GaiaTestCase.setUp(self)
        self.UTILS      = UTILS(self)
        self.camera     = AppCamera(self)
        self.video      = AppVideo(self)
        
        self.marionette.set_search_timeout(50)
        self.lockscreen.unlock()
    
        self.UTILS.setTimeToNow()
        
    def tearDown(self):
        self.UTILS.reportResults()
        
    def test_run(self):
        #
        # Record a test video.
        #
        self.camera.launch()
        self.camera.recordVideo("00:05")
        self.camera.checkVideoLength(0, 4.9, 10.1)

        #
        # Open the video player application.
        #
        self.video.launch()
        time.sleep(5)
         
        #
        # the first thumbnail should be our video.
        #
        self.video.checkThumbDuration(0, "00:05", 2)
         
        #
        # Check that the video is as long as expected.
        #
        self.video.checkVideoLength(0, 4.9, 10.1)
        
