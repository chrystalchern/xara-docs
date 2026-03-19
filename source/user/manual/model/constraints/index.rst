.. _ModelConstraints:

Constraints
***********

*Multi-point constraints* (MP_Constraints) are constraints that allow the user to define the relationship between the response of a set of the degrees-of-freedom at one node (the constrained node) in relation to the response of the degrees-of-freedom at another node (the retained node).
In structural analysis MP_Constraints are used to enforce rigid-diaphragm constraints, equal constraints (response of degrees-of-freedom at two nodes move the same), or rotated constraints (response of degrees-of-freedom at two nodes related through a rotation matrix).


.. toctree::
   :maxdepth: 1

   constrain
   equalDOF
   diaphragm
   rigidLink


