.. _equalDOF:

equalDOF
^^^^^^^^

``equalDOF`` imposes a constraint between nodes where the degrees-of-freedom at the constrained node move exactly the same as the degrees-of-freedom at the other node, the retained node.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.equalDOF(rnode, cnode, dofs)
         
         Set the degrees-of-freedom of node ``cnode`` to be equal to the degrees-of-freedom at the retained node ``rnode``.
   
         :param int rnode: integer tag identifying the retained node
         :param int cnode: integer tag identifying the constrained node
         :param list dofs: list of nodal degrees-of-freedom that are constrained
         :return: None

   .. tab:: Tcl 

      .. function:: equalDOF $rNodeTag $cNodeTag $dof1 $dof2 ..

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $rNodeTag, |integer|,	   integer tag identifying the retained node (*rNode*)
         $cNodeTag, |integer|,	   integer tag identifying the constrained node (*cNode*)
         $dof1 $dof2 ..., |integerList|, "list of nodal degrees-of-freedom that are constrained at the *cNode* (optional)"


.. note::

   The valid range of ``dof`` is 1 through **ndf** of the **constrained** node

   If no dofs are specified, *all* DOFs of the constrained node are used

Examples
--------

The following example will constrain the displacenents at DOFs **1, 3, and 5** at node **2** to be the same as those of node **33**.

1. **Tcl Code**

   .. code-block:: none

      equalDOF 2 33 1 3 5;

1. **Python Code**

   .. code-block:: python

      model.equalDOF(2,33, (1,3,5))



References
----------

*  Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., "Concepts and Applications of Finite Element Analysis," 4th edition, John Wiley and Sons publishers, 2002.

Code developed by: |fmk|

