.. _about-features-dropped:

Dropped Capabilities
^^^^^^^^^^^^^^^^^^^^

* All commands related to reliability analysis are dropped. This however does not include the commands for sensitivity analysis.
  In particular, the following are *not* supported:

  * randomVariable

* There are no plans to include the recently added ``damping`` commands.

* The recently added ``mesh`` and ``line`` commands of OpenSeesPy are replaced in |xara| by ``Model.surface``. 
  Motivation: ``mesh`` is unpredictable, questionably defined, and needlessly cumbersome.
