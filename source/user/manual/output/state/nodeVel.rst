.. _nodeVel:

nodeVel
*******


.. tabs::

   .. tab:: Python 

      .. py:method:: Model.nodeVel(tag, dof=None)

         Return the velocity at a specified node.

         :param |integer| tag: The tag of the :ref:`node` whose velocities are sought.
         :param |integer| dof: Optional: specific degree of freedom at the node (between 1 and :py:attr:`Model.ndf`, inclusive).

   .. tab:: Tcl

      .. function:: nodeVel $tag <$dof>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, tag identifying node whose velocities are sought
         $dof, |integer|, optional: specific dof at the node (1 through ndf)

If optional ``dof`` is not provided, an array containing all velocity components for every dof at the node is returned.

Example
-------

The following example is used to set the variable **vel** to the nodal velocity at node given by the variable **nodeTag** in the **1** degree-of-freedom direction.

1. **Tcl Code**

   .. code-block:: tcl

      set vel [nodeVel $nodeTag 1]

2. **Python Code**

   .. code-block:: python

      vel = model.nodeVel(nodeTag,1)


Code developed by: |fmk|
