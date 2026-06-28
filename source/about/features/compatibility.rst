.. _CompatibilityLayer:


Compatibility
^^^^^^^^^^^^^

*xara* is largely compatible with both *OpenSeesPy* and the original |OpenSees| Tcl interpreter.


Python
------

The *xara* package provides the ``opensees.openseespy`` module which is designed to be a drop-in replacement for the OpenSeesPy package. 
In order to execute an OpenSeesPy script with *xara*, just change the import from 

.. code-block:: Python

   import openseespy.opensees # OpenSeesPy import

to:

.. code-block:: Python

   import opensees.openseespy # Backwards-compatible xara import


Tcl
---

To execute a classic |OpenSees| Tcl file using *xara*, run the following command from a terminal:

.. code-block:: bash

   python -m opensees <file>

where ``<file>`` is a path to a Tcl file on your computer. 
To start an interactive Tcl interpreter using *xara*, run the following command from a terminal:

.. code-block:: bash

   python -m opensees


Details 
-------

While *xara* aims to be compatible with OpenSeesPy and OpenSees Tcl, there are some differences and limitations.
The following pages describe this in detail:

- :ref:`Deprecations <about-features-deprecated>` Features of OpenSeesPy that are discouraged in *xara*, but still supported for backwards compatibility.
- :ref:`Dropped Capabilities <about-features-dropped>` Features of OpenSeesPy that were *removed* in *xara*.
- :ref:`Suspended Capabilities <about-features-suspended>` Features of OpenSeesPy that are temporarily disabled in *xara*, but will be added in the future.
