.. _nodeCoord:

nodeCoord
*********

.. tabs::

   .. tab:: Python

      .. py:method:: Model.nodeCoord(tag [, dim])

         Return the coordinate at a specified node.

         :param |integer| tag: The tag of the :ref:`node` whose coordinates are sought.
         :param |integer| dim: Optional: specific coordinate dimension at the node (between 1 and :py:attr:`Model.ndm`).
         :returns: A |list| of the coordinate components at the node.

   .. tab:: Tcl

      .. function:: nodeCoord $tag <$dim>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, tag identifying node whose velocities are sought
         $dim, |integer|, optional: specific crd dimension at the node (1 through ndm)

If optional ``dim`` is not provided, an array containing all coordinate components is returned.

Example
-------

The following example is used to set the variable **crdNode** to the nodal coordinates for the node given by the variable **nodeTag**.

1. **Tcl Code**

   .. code-block:: tcl

      set crdNode [nodeCoord $nodeTag]

2. **Python Code**

   .. code-block:: python

      crdNode = model.nodeCoord(nodeTag)


Code developed by: |fmk|
