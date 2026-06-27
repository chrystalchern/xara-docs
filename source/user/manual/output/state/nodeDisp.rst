.. _nodeDisp:

nodeDisp
********


.. tabs::

   .. tab:: Python 

      .. py:method:: Model.nodeDisp(tag, dof=None)

         Return the displacement at a specified node.

         :param |integer| tag: The tag of the :ref:`node` whose displacements are sought.
         :param |integer| dof: Optional: specific degree of freedom at the node (between 1 and :py:attr:`Model.ndf`, inclusive).
         :returns: A |list| of :py:attr:`Model.ndf`  displacement values at the node when ``dof=None``. When ``dof`` is supplied, the result is a |float|.

   .. tab:: Tcl

      .. function:: nodeDisp $tag <$dof>


      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, tag identifying node whose displacements are sought
         $dof, |integer|, optional: specific dof at the node (1 through ndf)


After an analysis step, the displacement at each :ref:`node <node>` is updated in the domain.
``nodeDisp`` returns the current displacement (and rotation, when applicable) for the specified node and optional DOF.
Returned values are in the length and angle units of the user's chosen system (see :ref:`units`).

The components are ordered as follows for various combinations of dimension (:py:attr:`Model.ndm`) and degrees of freedom (:py:attr:`Model.ndf`):

.. csv-table::
   :header: "ndm", "ndf", "Order of components"
   :widths: 10, 10, 40

   1, 1, "u1"
   2, 2, "u1, u2"
   3, 3, "u1, u2, u3"
   2, 3, "u1, u2, r3"
   3, 6, "u1, u2, u3, r1, r2, r3"


Example
-------

The following example is used to set the variable ``disp1`` to the nodal displacement at node given by the variable **tag** in the **1** degree-of-freedom direction.

1. **Tcl Code**

   .. code-block:: tcl

      set disp1 [nodeDisp $tag 1]

2. **Python Code**

   .. code-block:: python

      u1 = model.nodeDisp(tag,1)

Code developed by: |fmk|
