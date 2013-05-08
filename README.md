WARNING: USING THESE TESTS WILL RESULT IN ALL DATA BEING REMOVED FROM THE DEVICE!
=================================================================================



#Instructions for setting up and running automated regression tests.

<b>1.</b> Clone and install the OWD_TEST_TOOLKIT repository (https://github.com/roydude/OWD_TEST_TOOLKIT).

<b>2.</b> Type:

<pre>
./run_tests.sh
</pre>

... or specify particular test numbers, like this:

<pre>
./run_tests.sh 7 8 21 40 41
</pre>

For more details, please refer to the README.md for OWD_TEST_TOOLKIT.


<!--testcoverage-->
TESTS COVERED
=============
<table>
  <tr>
    <th>Test Case</th><th>Description</th>
  </tr>

  <tr>
    <td  align=center>19180</td><td  align=left>[FACEBOOK] Unlink all Facebook contacts in the address book in a single step and verify the contacts who was linked to a facebook contacts.</td>
  </tr>

  <tr>
    <td  align=center>19181</td><td  align=left>[CONTACTS] Remove a photo,a phone number, an email, an address and a comment from a contact and restore the phone number and the comment.</td>
  </tr>

  <tr>
    <td  align=center>19182</td><td  align=left>[CONTACTS] Search a contact after edit contact name.</td>
  </tr>

  <tr>
    <td  align=center>19183</td><td  align=left>[CONTACTS] **INCOMPLETE** Verify that when looking at the details of a contact, the user can make a call to the contact with several phone numbers added.</td>
  </tr>

  <tr>
    <td  align=center>19184</td><td  align=left>[CONTACTS] Delete a contact from the contact details(all the fields filled).</td>
  </tr>

  <tr>
    <td  align=center>19185</td><td  align=left>[CONTACTS] The 'done' button in new contact mode (email parameter).</td>
  </tr>

  <tr>
    <td  align=center>19186</td><td  align=left>[CONTACTS] Delete all characters to the name and surname fields.</td>
  </tr>

  <tr>
    <td  align=center>19187</td><td  align=left>[CONTACTS] Remove a contact from the favorites list.</td>
  </tr>

  <tr>
    <td  align=center>19188</td><td  align=left>[CONTACTS] Configure a contact as a favourite.</td>
  </tr>

  <tr>
    <td  align=center>19189</td><td  align=left>[CONTACTS] Add multiple emails addresses.</td>
  </tr>

  <tr>
    <td  align=center>19190</td><td  align=left>[CONTACTS] **INCOMPLETE** Verify that the user can send a SMS from a contact details - SMS conversation doesn't exist.</td>
  </tr>

  <tr>
    <td  align=center>19191</td><td  align=left>[CONTACTS] Search by text string (UPPER CASE) that matches the last name.</td>
  </tr>

  <tr>
    <td  align=center>19192</td><td  align=left>[CONTACTS] Search by text string that not matches with any contact name/last name.</td>
  </tr>

  <tr>
    <td  align=center>19193</td><td  align=left>(BLOCKED BY: https://bugzilla.mozilla.org/show_bug.cgi?id=867119) [SMS] Receive an SMS from a contact with long name.</td>
  </tr>

  <tr>
    <td  align=center>19194</td><td  align=left>[SMS] ** Not checking popup warning! ** Try send a sms to a contact while airplane is enabled (from sms app - use contact option).</td>
  </tr>

  <tr>
    <td  align=center>19195</td><td  align=left>[SMS] Verify the Carrier of number from which the contact is sending message to the user.</td>
  </tr>

  <tr>
    <td  align=center>19196</td><td  align=left>[SMS] Send/Receive a new SMS when the conversation thread is empty.</td>
  </tr>

  <tr>
    <td  align=center>19197</td><td  align=left>[SMS] Verify the timestamp (received message) when the SMS has been sent from a different timezone.</td>
  </tr>

  <tr>
    <td  align=center>19198</td><td  align=left>[SMS] Delete all SMS in a conversation with several sms</td>
  </tr>

  <tr>
    <td  align=center>19199</td><td  align=left>[SMS] Delete a SMS in a conversation with several sms</td>
  </tr>

  <tr>
    <td  align=center>19200</td><td  align=left>[SMS] Receive a sms while device is locked(Vibration alert), screen off.</td>
  </tr>

  <tr>
    <td  align=center>19201</td><td  align=left>[SMS] Select some conversations and press delete.</td>
  </tr>

  <tr>
    <td  align=center>19202</td><td  align=left>[SMS] Delete a sms conversation.</td>
  </tr>

  <tr>
    <td  align=center>19203</td><td  align=left>[SMS] Open SMS app after all sms were deleted or there is any sms.</td>
  </tr>

  <tr>
    <td  align=center>19204</td><td  align=left>[SMS] Send a new SMS by entering manually the phone number (contact number).</td>
  </tr>

  <tr>
    <td  align=center>19205</td><td  align=left>[SMS] Send a new SMS by entering manually the phone number.</td>
  </tr>

  <tr>
    <td  align=center>19224</td><td  align=left>[HOME SCREEN] Add and remove categories to everything.me grid.</td>
  </tr>

  <tr>
    <td  align=center>19225</td><td  align=left>[HOME SCREEN] Verify that if no connection available when selecting a category in everything.me the user will be notified about the need to have a network connection to use this functionality.</td>
  </tr>

  <tr>
    <td  align=center>19226</td><td  align=left>[HOME SCREEN] Verify that when first launch a search-box is shown as well as a list of application categories.</td>
  </tr>

  <tr>
    <td  align=center>19227</td><td  align=left>[HOME SCREEN] Verify that when the user navigates from everything.me page to the grid, dock is shown again.</td>
  </tr>

  <tr>
    <td  align=center>19228</td><td  align=left>[HOME SCREEN] Verify that when the user navigates to everything.me page, dock is hidden.</td>
  </tr>

  <tr>
    <td  align=center>19230</td><td  align=left>    _Description = '[HOME SCREEN] Verify that user can click on "Add more categories" in everything.me grid so I am shown again the list and can add more categories.'</td>
  </tr>

  <tr>
    <td  align=center>19231</td><td  align=left>[HOME SCREEN] Verify that the user can uninstall a everything.me app through the grid edit mode.</td>
  </tr>

  <tr>
    <td  align=center>19241</td><td  align=left>[EMAIL] Basic: Deleting of a e-mail in Inbox.</td>
  </tr>

  <tr>
    <td  align=center>19245</td><td  align=left>[CAMERA] Delete a video just recorded.</td>
  </tr>

  <tr>
    <td  align=center>19246</td><td  align=left>[CAMERA] Go to Gallery from Camera.</td>
  </tr>

  <tr>
    <td  align=center>19247</td><td  align=left>[CAMERA] Delete a picture just taken.</td>
  </tr>

  <tr>
    <td  align=center>19253</td><td  align=left>[Gallery] Select multiple pictures and delete them.</td>
  </tr>

  <tr>
    <td  align=center>19325</td><td  align=left>(BLOCKED BY: https://bugzilla.mozilla.org/show_bug.cgi?id=867987) [CLOCK] Alarm- Delete an alarm.</td>
  </tr>

  <tr>
    <td  align=center>19328</td><td  align=left>[CLOCK] Clock in different modes (analog, digital).</td>
  </tr>

  <tr>
    <td  align=center>19350</td><td  align=left>[SMS] Send a SMS with more than 160 characters.</td>
  </tr>

  <tr>
    <td  align=center>19351</td><td  align=left>[SMS] Received a SMS with more than 160 characteres.</td>
  </tr>

  <tr>
    <td  align=center>19353</td><td  align=left>[UTILITY TRAY] As a user, I want to be able to enable/disable Data from the utility tray.</td>
  </tr>

  <tr>
    <td  align=center>19354</td><td  align=left>[UTILITY TRAY] Open settings app from utility tray.</td>
  </tr>

  <tr>
    <td  align=center>19355</td><td  align=left>[UTILITY TRAY] Activate/Deactivate ariplane  mode from Utility tray icon.</td>
  </tr>

  <tr>
    <td  align=center>19356</td><td  align=left>[SMS] Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field.</td>
  </tr>

  <tr>
    <td  align=center>19357</td><td  align=left>[SMS] CLONE - Verify that If the contact only has a phone number, that phone number is automatically selected and the user is returned to the compose SMS screenwidth the contacts name filled-in in the To Field...</td>
  </tr>

  <tr>
    <td  align=center>19358</td><td  align=left>[SMS] Verify that If the contact has more than one phone number, it opens a list of numbers. Clicking on a number in the list, returns the user to the compose SMS app with the contacts name filled-in in the To Field.(second phone number).</td>
  </tr>

  <tr>
    <td  align=center>19359</td><td  align=left>[CONTACTS] Send an email to a contact from the contact details (Contact with multiple emails)</td>
  </tr>

  <tr>
    <td  align=center>19392</td><td  align=left>[BASIC][FACEBOOK] Import Facebook contacts from contacts app settings.</td>
  </tr>

  <tr>
    <td  align=center>19393</td><td  align=left>[BASIC][EVERYTHING.ME] Install and launch an everything.me app - verify the everything.me app launches successfully to the right web content.</td>
  </tr>

  <tr>
    <td  align=center>19397</td><td  align=left>(BLOCKED BY: https://bugzilla.mozilla.org/show_bug.cgi?id=867987) [BASIC][CLOCK] Add an alarm - verify the alarm was added with the correct date and time.</td>
  </tr>

  <tr>
    <td  align=center>19398</td><td  align=left>[BASIC][CALENDAR] Add and view an event to an offline calendar in each calendar view - verify the event is shown on each calendar view with the correct title, location, and event time length.</td>
  </tr>

  <tr>
    <td  align=center>19400</td><td  align=left>[BASIC][HOMESCREEN] Delete a packaged app - verify the app was successfully removed from the homescreen.</td>
  </tr>

  <tr>
    <td  align=center>19401</td><td  align=left>[BASIC][HOMESCREEN] Launch a packaged app - verify the app launches successfully to the correct content.</td>
  </tr>

  <tr>
    <td  align=center>19403</td><td  align=left>[BASIC][SYSTEM] With two apps already running, launch the card view, kill one app process, and launch the other - verify the app killed is stopped and the other app starts up.</td>
  </tr>

  <tr>
    <td  align=center>19405</td><td  align=left>[BASIC][EMAIL] Send email with gmail.</td>
  </tr>

  <tr>
    <td  align=center>19406</td><td  align=left>[BASIC][EMAIL] Receive email with gmail.</td>
  </tr>

  <tr>
    <td  align=center>19407</td><td  align=left>[BASIC][EMAIL] Send email with hotmail.</td>
  </tr>

  <tr>
    <td  align=center>19408</td><td  align=left>[BASIC][EMAIL] Receive email with hotmail.</td>
  </tr>

  <tr>
    <td  align=center>19409</td><td  align=left>[BASIC][HOMESCREEN] Launch market installed hosted app - verify the app is launched successfully from the homescreen.</td>
  </tr>

  <tr>
    <td  align=center>19410</td><td  align=left>[BASIC][APP INSTALL] Install a market installed hosted app - verify the app is installed with the right icon.</td>
  </tr>

  <tr>
    <td  align=center>19413</td><td  align=left>[BASIC][BROWSER] Load a website via Cellular Data - verify the site loads in the browser correctly.</td>
  </tr>

  <tr>
    <td  align=center>19414</td><td  align=left>[BASIC][BROWSER] Load a website via Wifi - verify the site loads in the browser correctly.</td>
  </tr>

  <tr>
    <td  align=center>19416</td><td  align=left>[BASIC][GALLERY] Browse photos in gallery - verify you can see each picture of your sdcard.</td>
  </tr>

  <tr>
    <td  align=center>19417</td><td  align=left>[BASIC][VIDEO] Play the video you recorded, check for video and sound to verify the video could be successfully played.</td>
  </tr>

  <tr>
    <td  align=center>19418</td><td  align=left>[BASIC][CAMERA] Make a video recording - verify the recording is successful and added to the gallery.</td>
  </tr>

  <tr>
    <td  align=center>19419</td><td  align=left>[BASIC][CAMERA] Take a picture with camera - verify the picture is successfully taken and added to the gallery.</td>
  </tr>

  <tr>
    <td  align=center>19420</td><td  align=left>[BASIC][SMS] Receive a sms with vibration (device unlocked) & confirm notification - verify that the notification is fired and that you can see the message received from the other phone.</td>
  </tr>

  <tr>
    <td  align=center>19421</td><td  align=left>(BLOCKED BY: https://bugzilla.mozilla.org/show_bug.cgi?id=867119) [BASIC][CONTACTS] Send an sms from a contact detail - Verify the contact receives the SMS.</td>
  </tr>

  <tr>
    <td  align=center>19422</td><td  align=left>[BASIC][CONTACTS] Edit a contact changing the name and the phone number - verify that the values modified in the contact appear when viewing the updated contact.</td>
  </tr>

  <tr>
    <td  align=center>19423</td><td  align=left>[BASIC][CONTACTS] Add new contact filling all the fields - verify the contact is added with the correct values for each field.</td>
  </tr>

  <tr>
    <td  align=center>roy</td><td  align=left>(ignore me!)</td>
  </tr>
</table>
