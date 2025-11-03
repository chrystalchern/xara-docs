.. _about-features-suspended:

Suspended
^^^^^^^^^

Certain features of OpenSees have been *suspended* for development of OpenSeesRT, but are planned to be re-implemented in the near future. 
These features include:

* Save and restore of the model state. Motivation: the existing implementation is considered error prone and unmaintainable due to its reliance on hard-coded integer class tags and global interpreter variables. 

* support for the `modalProperties` command is suspended. This is because the original implementation was accessing the analysis model through a global variable, which was deemed too error prone. Progress is being tracked `here <https://github.com/peer-open-source/xara/issues/59>`__

