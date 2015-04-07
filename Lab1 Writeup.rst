CST 236 - Lab 1 - David Antonucci
---------------------------------

Lab 1 Write Up
^^^^^^^^^^^^^^

What was the hardest part of this lab
=====================================

Getting everything set up and working, considering I had zero experince with everything but Python
before this class / lab.

During the course of this lab, why did we exclude .pyc files?
=============================================================

Because compiled files are typically frowned upon in repositories. Any compiled files should be
able to be compiled by the end user. It also means that more data will have to be committed or
downloaded with each change.

Name three files which would likely need to have a gitignore added?
===================================================================

#. .coverage
#. source\source1.pyc
#. source\source2.pyc

What is a pyunit TestCase?
==========================

It is a testing method which tests a unit of Python code.

What is the difference between a git cherry pick and a rebase?
==============================================================

Rebase is used to place changes on a branch back on the master.
Cherry picking allows taking one file from a commit, and placing it in the current branch.

How could you use git to print out just the author name of a given file for the current version of the repo?
============================================================================================================

.. code::
    
    git log --format=%an --since [filename]

During this lab did you explore Tortoise Git or GIT Extensions?
===============================================================

No, I did not.