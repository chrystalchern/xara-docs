.. _conventions:

Conventions 
^^^^^^^^^^^


Degrees of Freedom
------------------

Several commands may accept an integer argument to specify a degree of freedom (DOF) in the model.
This is always a 1-based index, meaning that the first DOF is 1, the second DOF is 2, and so on (as opposed to 0-based indexing, which is common in some programming languages).
The DOFs are ordered as follows:

.. csv-table::
   :header: "ndm", "ndf", "Order of components"
   :widths: 10, 10, 40

   1, 1, "u1"
   2, 2, "u1, u2"
   3, 3, "u1, u2, u3"
   2, 3, "u1, u2, r3"
   3, 6, "u1, u2, u3, r1, r2, r3"
   3, 6+n, "u1, u2, u3, r1, r2, r3, d4, d5, ..., d6+n"

where:

* ``u1, u2, u3`` are the translational displacements in the x, y, and z directions respectively,
* ``r1, r2, r3`` are the rotational displacements about the x, y, and z axes respectively.


