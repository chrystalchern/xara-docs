.. _Spload:

Sp
^^

This command is used to define a single-point constraint that scales under a load pattern.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.sp(node, dof, value, pattern)

         Constrain the ``dof`` component of the solution at ``node`` to ``value`` in ``pattern``.

         :param integer node: tag of node to which constraint is applied
         :param integer dof: the degree-of-freedom at the node to which constraint is applied (1 through :attr:`Model.ndf`)
         :param integer value: reference constraint value
         :param integer pattern: tag of the :ref:`Plain <plainPattern>` load pattern.

   .. tab:: Tcl 

      .. function:: sp $node $dof $value


      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $node, |integer|, tag of node to which constraint is applied
         $dof, |integer|, the degree-of-freedom at the node to which constraint is applied (1 through ndf)
         $value, |integer|, reference constraint value

.. note::
   
   The ``value`` is a reference value, it is the time series that provides the load factor. 
   The load factor times the reference value is the constraint that is actually applied to the node.


Examples
--------

1. **Tcl Code**

   .. code-block:: tcl

      pattern Plain 1 Linear {
          sp 1 1 0
          sp 1 2 0
          sp 1 3 0
      }


2. **Python Code**

   .. code-block:: python

      model.pattern('Plain', 1, 'Linear')
      model.sp(1, 1, 0, pattern=1)
      model.sp(1, 2, 0, pattern=1)
      model.sp(1, 3, 0, pattern=1)


Code Developed by: |fmk|
