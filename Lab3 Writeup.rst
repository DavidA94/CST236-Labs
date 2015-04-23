Lab 3 Writeup
-------------

What are five examples of other testing (nose2) plugins that might be useful?
=============================================================================

#. Coverage (Already used)
#. Test report in .xyz format
#. Code Analysis
#. A way to distinguesh between test categories
#. Keeping a history of test results

Do you plan to create any of these plugins for your term project?
=================================================================

Just coverage.

What is the hardest part of this lab?
=====================================

This one was much easier. Probably the "hardest" part was figuring out how to test 5-7.

Did the code fully and completely implement the requirements? Explain
=====================================================================

No. See bug reports.

Was the requirements complete? Explain
======================================

Yes. A functional program can be created from the requirements.

Time Spent
==========

| 1. Why are requirements tracing so important?
|    To prevent a requirement from being missed.

| 2. How long did it take to complete this lab?
|    2-3 hours I think, but I wasn't keeping track explicitly. 


Bug Reports
===========

+----------------------------------------------------------------------------------------------------------+
| | **Issue Number:** 1                                                                                    |
+----------------------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                             |
| | Does not extract number at the end                                                                     |
+----------------------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                                |
| | Create a question which takes an number in at the end                                                  |
| | Try to ask the question with the question mark                                                         |
+----------------------------------------------------------------------------------------------------------+
| | **Comments:**                                                                                          |
| | Seems to fail because float("00>") does not work. Removing ">" before parsing should fix the issue.    |
+----------------------------------------------------------------------------------------------------------+


+-------------------------------------------------------------------------------+
| | **Issue Number:** 2                                                         |
+-------------------------------------------------------------------------------+
| | **Brief:**                                                                  |
| | Req #0017 not correct                                                       |
+-------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                     |
| | Try to ask how many feet in miles                                           |
+-------------------------------------------------------------------------------+
| | **Comments:**                                                               |
| | The return is just the number. Adding "miles" to the end will make it work. |
+-------------------------------------------------------------------------------+


+---------------------------------------------------------------------------------------------------+
| | **Issue Number:** 3                                                                             |
+---------------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                      |
| | Req #0018 not properly extract                                                                  |
+---------------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                         |
| | Try asking:                                                                                     |
| | "How many seconds since 2015-04-23 12:30:00>"                                                   |
+---------------------------------------------------------------------------------------------------+
| | **Comments:**                                                                                   |
| | This seems to be due to the  not being extracted, therefore the 90% requirement fails.          |
+---------------------------------------------------------------------------------------------------+


+----------------------------------------------------------------------------------------------+
| | **Issue Number:** 4                                                                        |
+----------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                 |
| | Req #0018 returns the wrong time, and does not force  format.                              |
+----------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                    |
| | Ask: "How many seconds since May"                                                          |
+----------------------------------------------------------------------------------------------+
| | **Comments:**                                                                              |
| | The return is "42 seconds", always. Also, " seconds" at the end is not in the requirement. |
+----------------------------------------------------------------------------------------------+


+------------------------------------------+
| | **Issue Number:** 5                    |
+------------------------------------------+
| | **Brief:**                             |
| | Req #0019 has an invalid return        |
+------------------------------------------+
| | **Steps to Reproduce:**                |
| | Ask: "Who invented Python"             |
+------------------------------------------+
| | **Comments:**                          |
| | The acronym should not be spelled out. |
+------------------------------------------+


+-------------------------------------------------------------------------------------------------+
| | **Issue Number:** 6                                                                           |
+-------------------------------------------------------------------------------------------------+
| | **Brief:**                                                                                    |
| | Excess Code when trying to call method                                                        |
+-------------------------------------------------------------------------------------------------+
| | **Steps to Reproduce:**                                                                       |
| | See lines: 56-57                                                                              |
+-------------------------------------------------------------------------------------------------+
| | **Comments:**                                                                                 |
| | The requirements do not specify that an error should be thrown if the arguments do not match. |
+-------------------------------------------------------------------------------------------------+


+---------------------------+
| | **Issue Number:** 7     |
+---------------------------+
| | **Brief:**              |
| | Unused Dictionaries     |
+---------------------------+
| | **Steps to Reproduce:** |
| | See lines 13 - 16       |
+---------------------------+
| | **Comments:**           |
| | These are unused.       |
+---------------------------+


+------------------------------------------------+
| | **Issue Number:** 8                          |
+------------------------------------------------+
| | **Brief:**                                   |
| | Unwanted print statement                     |
+------------------------------------------------+
| | **Steps to Reproduce:**                      |
| | See line 49                                  |
+------------------------------------------------+
| | **Comments:**                                |
| | Pointless, but if anything, should be a log. |
+------------------------------------------------+
