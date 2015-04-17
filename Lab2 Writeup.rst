CST 236 - Lab 2 - David Antonucci
---------------------------------

Lab 2 Write Up
^^^^^^^^^^^^^^

Explain the major differences between TDD and BDD
=================================================
The main difference is that whereas TDD only tests are written, BDD puts another constraint on that you have to write feature files as well. 
TDD is much simplier in the idea of it, since it's easier to say, "I'm testing a == b", whereas with BDD, you have to come up with things like 
scenarios, features, and then wrap it all into a given (when) then statement, which is just a pain.


What is a mixin, what challenges can occur when testing them? What order are they initialized in
================================================================================================
A mixin is a special type of multiple inheritance, similar to the idea of interfaces, but without the need to be implemented, however, it can still
be overwritten. Since I didn't use them, I'm not sure how they would be hard to debug, but I suppose it could be difficult to track down which 
mixin is giving the problem, if that's a problem. As to which order they are initialized: That was not discussed as far as I can remember, but logically
it would be left to right.

In python what does "super" do?
===============================
Super initializes the class that is being inherited.


Was there any job stories that did not meet the criteria we discussed in class? How did you handle this case?
=============================================================================================================
Although perhaps nothing was not, not discussed, many things were difficult to do just because of what they were. I go into more detail
in the Student Notes below.

Which model did you find most challenging? Why?
===============================================
BDD. See differences section for why.

Which model did you find easiest to update/maintain?
====================================================
TDD.

How did you test that logging occurred only when desired?
=========================================================
Using the testfixtures module.

Students Notes
^^^^^^^^^^^^^^
This assignment wasn't really difficult in the sense that it was hard, but rather it was difficult to figure out what was 
going on. Because of that, some of my modules return magic numbers, or just strings saying what they would do based on the
job story. But still, I really have no clue what I just "made" for the BDD section. This also affected my abillity to write
decent code, since I didn't even have a half-picture of what I was making. This is also why you'll see almost no OOP in my
code, since inheritance is something that should not just be used for the fun of it, but only when needed. There is some 
composition in my code, but if you want to see that I can do OOP, I will show you other code. 

Now, I know this is your first class teaching, and I hope that you will be back next year to teach the next round. From
what I see, you seem to have a good potential to do well at teaching, especially since you do it for a living, with a
language that is about as simple as possible when it comes to testing (run nose2, run behave, done). However, I think
it would be good to spend some time, now that you know what you're doing better (with teaching), to develop some better
labs that are more complete, and that are simple enough to be fully implemented, but still interesting like your goal
was to do this round. As you said, some parts of this lab were imaginary, and that made it a bit difficult / annoying.

Also, for future reference, it would be good to plan to spend time going over the labs in what we're actually doing. Although
Python seems to be the perfect language for teaching this class, I would count on nobody having used it, as the school, as
I'm sure you know, focuses more on the C based langauges. Python is a different beast. On top of that, we're learning new
things that we've never seen done before. I think how you did the one lab was what needs to always be done: Take a part of the
lab, and show us how to implement it, then leave the rest for the students to do. One thing you missed on this lab would be 
logging. I know Python from before, but that part, until your coworker showed me how to keep track of stuff, was something I
was completely lost on, especially since I'd never used logging before. Add never having used Python on top of that (for 
other students) and things become even more difficult.

These notes are for you to consider and hopefully help you become an amazing teacher. As I said before, from what I see, you
have a good potential to achieve that, and I hope to see you do so.