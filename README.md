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
    <td  align=center>19180</td><td  align=left>Unlink all Facebook contacts in the address book in a single step and verify the contacts who was linked to a facebook contacts.</td>
  </tr>

  <tr>
    <td  align=center>19181</td><td  align=left>Remove a photo,a phone number, an email, an address and a comment from a contact and restore the phone number and the comment.</td>
  </tr>

  <tr>
    <td  align=center>19182</td><td  align=left>Search a contact after edit name.</td>
  </tr>

  <tr>
    <td  align=center>19183</td><td  align=left>Verify that when looking at the details of a contact, the user can make a call to the contact with several phone numbers added.</td>
  </tr>
</table>
