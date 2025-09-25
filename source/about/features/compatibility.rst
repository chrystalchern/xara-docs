.. _CompatibilityLayer:


Compatibility
^^^^^^^^^^^^^

*xara* is largely compatible with both *OpenSeesPy* and the classic OpenSees Tcl interpreter.


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

To execute a classic OpenSees Tcl file using *xara*, run the following command from a terminal:

.. code-block:: bash

   python -m opensees <file>

where ``<file>`` is a path to a Tcl file on your computer. 
To start an interactive Tcl interpreter using *xara*, run the following command from a terminal:

.. code-block:: bash

   python -m opensees


