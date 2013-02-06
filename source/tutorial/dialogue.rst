.. _dialogues:
.. include:: ..\include.inc

Dialogues
=========

This tutorial will explain the dialogue module that is included in FIFErpg.

Summary
-------

Here is a quick summary of how the dialogues in this module work.

1. The dialogue is initiated and the first greeting which condition passes
is selected as the current section.
2. The commands of the current section are executed.
3. If there are responses available go to 4. Otherwise go to 5.
4. Select a response as the current section. Go to 2.
5. End the dialogue.