Mumps
^^^^^

This command is used to construct a sparse system of equations which uses the `Mumps <http://mumps-solver.org/>`_  solver. 

.. function:: system Mumps

.. note:: 

   This system is presently limited to the parallel **OpenSeesSP** and **OpenSeesMP** applications.

Example
-------

The following example shows how to construct a sparse system solved using the Mumps solver.

1. **Tcl Code**

   .. code-block:: tcl

      system Mumps

2. **Python Code**

   .. code-block:: python

      model.system('Mumps')

Code developed by: |fmk|


