CST 236 Lab 5 - Writeup
-----------------------

What was the hardest part of this lab?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Figuring out how to add 1,000,000 questions in a reasonable amount of time, and coming up with things that can be threaded.

What is the difference between performance testing and performance measurement?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preformance testing is ensuring that the preformance standard is met, while mesurement shows what the actual values are.

What new bugs did you encounter with the new code?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- I can get the 1001th fibonacci number. My tests fail because of this.
- Not all questions are completed in 5ms.
- Spike and stress testing fail.

Did you mock anything to speed up performance testing? Do you see any issues with this?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not to speed up, but I did use it to ensure one value.

Generate at least 5 performance measurement value sets and graphs (these sets must be worthwhile)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will find them in the Plots/ folder after running nose2.

Explain Load Testing, stress testing, endurance testing, spike testing configuration testing and isolation testing. How did you implement each of these?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Load testing is when an interface is put under a constant load. Stress/Endurance testsing is basically the same thing. Spike testing is when an interface it hit
with a lot of users / load at a sudden time for a short period of time. Isolation testing is when one specific part is being tested by itself.

- For Load/Stress/Endurance testing, I asked a question 1000 times in a row.
- For Spike testing, I set up 1000 tests on different threads, and then ran nearly all at once.
- Isolation testsing was done with basically all the other tests.

How long did this lab take to accomplish?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5-6 hours, not counting waiting time. Lots of, "Nope, that didn't work. What about..."