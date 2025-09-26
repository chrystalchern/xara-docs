.. _PlainConstraints:

Plain Constraints
^^^^^^^^^^^^^^^^^


.. function:: constraints Plain

.. warning::

   This constraint handler can only enforce homogeneous single point constraints (:ref:`fix` command) and multi-pont constraints where the constraint matrix is equal to the identity (:ref:`equalDOF` command).

   It does not *follow* constraints, in the sense that the constrained node in a :ref:`multi-point constraint <ModelConstraints>` cannot be a retained node in another multi-point constraint.


Examples
--------

1. **Tcl Code**

   .. code-block:: tcl

      constraints Plain


2. **Python Code**

   .. code-block:: python

      model.constraints('Plain')


Code Developed by: |fmk|
