Lab 7 Writeup
-------------

**What bugs did you find?**

#. Ask: *[A question with 1+ "?" in the question, none of which are at the end, and does not meet Bug 2's criteria]*
#. Ask: *[A question with (n * 5) characters]*
#. Ask: *[A question with 51+ characters which does not meet bug 2's criteria]*
#. Happens upon teaching after 10 Q/A's have been stored.
#. When the answer to "What is the answer to everything?" is either an integer or a string, 
   and correcting it to be integer or string (whichever it is currenlty not), Bug 5 occurs.
#. Randomly "fails" to open correctly
#. Teach: *[Anything with a "?" in the answer]*

**What are the advantages and disadvantages of fuzz testing?**

**Advantages:** Can find bugs that would probably not be found by testing, since it will do things that no human would probably ever do, save a hacker.

**Disadvantages:** Takes a very long time, and will only find some of the simplest bugs in a reasonable amount of time.

**What was the hardest part of this lab?**

Bugs 4 and 5.

**How would you apply the concept of fuzz testing to testing a phone? a webpage? a library?**

#. "Calling" random numbers
#. Entering random data, clicking weird places, and going to links in a non-logical order.
#. Umm, pull random books off the shelf and make sure they're in the right place (Can libraries be tested?)

**How could throttling fuzz test scripts help with finding bugs?**

Making things go faster than a human may cause problems.

**What is Delta Debugging and how would it help with fuzz testing?**

A process which narrows down what is the problem by making the problem set smaller and smaller.

**If steps 1-20 were to produce an error using delta debugging what are the steps that 
would arrive at steps 8, 12, 13, 19 and 20 being necessary to reproduce the error?**

I'm not sure of the EXACT steps that would be necessary, as that would be difficult to figure out.
However, if we assume really complicated if/else tree that goes way too many levels in, and at certain
points in the tree, the logic calls a certain problem function, then by toggling the T/F sequence, to 
where sometimes the blocks that call the function are hit, and other times, they are not, it could 
get the problem at those specific step numbers.