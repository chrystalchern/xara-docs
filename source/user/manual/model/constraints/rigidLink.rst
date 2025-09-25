Rigid Link
^^^^^^^^^^

This command is used to define a *multi-point constraint*.

.. function:: rigidLink $type $retained_node $constrained_node

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $type, |string|,  "| string-based argument for rigid-link type:
   | **bar** only the translational degree-of-freedom will be constrained to be exactly the same as those at the master node 
   | **beam** both the translational and rotational degrees of freedom are constrained."
   $retainedNodeTag, |integer|, integer tag identifying the retained node
   $constrainedNodeTag, |integer|, integer tag identifying the constrained node

.. note::
   
   1. By *retained node*, we mean the node who's degrees-of-freedom are retained in the system of equations. 
      The constrained nodes degrees-of-freedom need not appear in the system (depending on the constraint :ref:`handler <ConstraintHandler>`). 


Theory
------

Beam
~~~~

For 2d and 3d problems with a **beam** type link, the constraint matrix (that matrix relating the responses at constrained node, :math:`u_c`, to responses at retained node, :math:`u_r`, i.e. :math:`u_c = C_{cr} u_r`, is constructed assuming small rotations. 
For 3d problems this results in the following constraint matrix:

.. math::

  \begin{bmatrix}
          1 & 0 & 0 & 0 & \Delta Z & -\Delta Y \\
          0 & 1 & 0 & -\Delta Z & 0 & \Delta X \\
          0 & 0 & 1 & \Delta Y & -\Delta X & 0 \\
          0 & 0 & 0 & 1 & 0 & 0 \\
          0 & 0 & 0 & 0 & 1 & 0 \\
          0 & 0 & 0 & 0 & 0 & 1 
  \end{bmatrix}


For 2d problems, the constraint matrix is:

.. math::

  \begin{bmatrix}
          1 & 0 & -\Delta Y \\
          0 & 1 & \Delta X \\
          0 & 0 & 1
  \end{bmatrix}

where :math:`\Delta X` is x coordinate of constrained node minus the x coordinate of the retained node. :math:`\Delta Y` and :math:`\Delta Z` being similarily defined for y and z coordinates of the nodes.

Rod
~~~

For 2d and 3d problems with a **rod** type link the constraint matrix, that which matrix relates the responses at translational degrees-of-freedom at the constrained node to corresponding responses at retained node, is the identity matrix. For 3d problems this results in the following constraint matrix:

.. math::

    \begin{bmatrix}
            1 & 0 & 0  \\
            0 & 1 & 0  \\
            0 & 0 & 1 
    \end{bmatrix}
 

For 2d problems, the constraint matrix is:

.. math::

  \begin{bmatrix}
          1 & 0 \\
          0 & 1 \\
  \end{bmatrix}   

Note that the rod constraint can also be generated using :ref:`equalDOF`.


Example
-------

The following command will constrain node **3** to move rigidly following rules for small rotations to displacements and rotations at node **2** is

1. **Tcl Code**

   .. code-block:: none
   
      rigidLink beam 2 3

2. **Python Code**

   .. code-block:: python
   
      model.rigidLink('beam', 2, 3)

