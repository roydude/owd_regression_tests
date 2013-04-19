#Instructions for setting up and running automated regression tests.

<b>1.</b> Clone and install the OWD_TEST_TOOLKIT repository (https://github.com/roydude/OWD_TEST_TOOLKIT).

<b>2.</b> Type:

<pre>
./run_tests.sh
</pre>

... or specify particular test numbers, like this:

<pre>
./run_tests 7 8 21 40 41
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
    <td  align=center>19183</td><td  align=left>[CONTACTS] Verify that when looking at the details of a contact, the user can make a call to the contact with several phone numbers added.</td>
  </tr>

  <tr>
    <td  align=center>19190</td><td  align=left>[CONTACTS] Verify that the user can send a SMS from a contact details - SMS conversation doesn't exist.</td>
  </tr>

  <tr>
    <td  align=center>19191</td><td  align=left>[CONTACTS] Search by text string (UPPER CASE) that matches the last name.</td>
  </tr>

  <tr>
    <td  align=center>19192</td><td  align=left>[CONTACTS] Search by text string that not matches with any contact name/last name.</td>
  </tr>

  <tr>
    <td  align=center>19231</td><td  align=left>[HOME SCREEN] Verify that the user can uninstall a everything.me app through the grid edit mode.</td>
  </tr>

  <tr>
    <td  align=center>19246</td><td  align=left>[CAMERA] Go to Gallery from Camera.</td>
  </tr>

  <tr>
    <td  align=center>19416</td><td  align=left>[BASIC][GALLERY] Browse photos in gallery - verify you can see each picture of your sdcard.</td>
  </tr>

  <tr>
    <td  align=center>19418</td><td  align=left>[BASIC][CAMERA] Make a video recording - verify the recording is successful and added to the gallery.</td>
  </tr>

  <tr>
    <td  align=center>19419</td><td  align=left>[BASIC][CAMERA] Take a picture with camera - verify the picture is successfully taken and added to the gallery.</td>
  </tr>

  <tr>
    <td  align=center>19421</td><td  align=left>[BASIC][CONTACTS] Send an sms from a contact detail - Verify the contact receives the SMS.</td>
  </tr>

  <tr>
    <td  align=center>19422</td><td  align=left>[BASIC][CONTACTS] Edit a contact changing the name and the phone number - verify that the values modified in the contact appear when viewing the updated contact.</td>
  </tr>

  <tr>
    <td  align=center>19423</td><td  align=left>[BASIC][CONTACTS] Add new contact filling all the fields - verify the contact is added with the correct values for each field.</td>
  </tr>
</table>
