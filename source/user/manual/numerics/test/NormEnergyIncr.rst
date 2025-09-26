.. _EnergyIncr:

Energy Increment
^^^^^^^^^^^^^^^^

This command is used to construct a convergence test which uses the energy increment, :math:`0.5 (x \cdot \boldsymbol{b})`, where the two vector come from the matrix equation :math:`Ax=b`, to determine if convergence has been reached. What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. Usually, though not always, :math:`x` is equal to the incremental displacement and the residual :math:`b`. 

.. function:: test EnergyIncr $tol $iter <$pFlag>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $tol, |float|, the tolerance criteria used to check for convergence
   $iter, |integer|, the max number of iterations to check before returning failure condition
   $pFlag, |integer|, " | print flag (optional: default is 0) valid options:
    | 0 print nothing
    | 1 print information on norms each time test() is invoked
    | 2 print information on norms and number of iterations at end of successful test
    | 4 at each step it will print the norms and also the <math>\Delta U</math> and <math>R(U)</math> vectors.
    | 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test."

.. note::

   When using a :ref:`penalty` constraint handler, large forces (those necessary to enforce the constraint) are included in the :math:`x` vector. Even for very small changes in the displacement, if user has selected overly large penalty factor, large forces can appear in the :math:`x` vector.


Example
-------

The following examples demonstrate the command to create a ``NormEnergyIncr`` test which allows ``10`` iterations with an energy increment :math:`0.5 (x \cdot b)` of **1.0e-2**.

1. **Tcl Code**

   .. code-block:: tcl

      test EnergyIncr 1.0e-2  10 2

2. **Python Code**

   .. code-block:: python

      model.test("EnergyIncr", 1.0e-2, 10, 2)


Code Developed by: |fmk|
