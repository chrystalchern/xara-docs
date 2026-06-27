.. _nodeAccel:

nodeAccel
*********

This command returns the current acceleration at a specified node.


.. tabs::

   .. tab:: Python

      .. py:method:: Model.nodeAccel(tag, dof=None)

         Return the acceleration at a specified node.

         :param |integer| tag: The tag of the :ref:`node` whose accelerations are sought.
         :param |integer| dof: Optional: specific degree of freedom at the node (between 1 and :py:attr:`Model.ndf`, inclusive).
         :returns: A |list| of the acceleration components at the node when ``dof=None``, otherwise a |float|.

   .. tab:: Tcl

      .. function:: nodeAccel $tag <$dof>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, tag identifying node whose accelerations are sought
         $dof, |integer|, optional: specific dof at the node (1 through ndf)


Example
-------

The following example is used to set the array/list **accel1** equal to the nodal accelerations at the node given by the variable **nodeTag**.

1. **Tcl Code**

   .. code-block:: tcl

      set accel1 [nodeAccel $nodeTag]

2. **Python Code**

   .. code-block:: python

      accel1 = model.nodeAccel(nodeTag)


Code developed by: |fmk|
