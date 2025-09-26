.. _NormUnbalance:

Residual
^^^^^^^^

What the right-hand-side of the matrix equation is depends on integrator and constraint handler chosen. 
Usually, though not always, it is equal to the equilibrium residual. 

.. tabs::

   .. tab:: Python
      .. py:method:: Model.test("Residual", tol, iter, verb=0, norm=2)
         :no-index:
          
         Define a convergence test which uses the residual norm :math:`b` vector in :math:`Ax=b`, to determine if convergence has been reached. 

         :param tol: the tolerance criteria used to check for convergence
         :type tol: |float|
         :param iter: the max number of iterations to check before returning failure condition
         :type iter: |integer|
         :param verb: print flag (optional: default is 0) valid options:
         :type verb: |integer|
         :param norm: type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm ...))
         :type norm: |integer|

   .. tab:: Tcl

      .. function:: test NormUnbalance tol? iter? <pFlag?> <nType?>

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
         $nType, |integer|, "type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm ...))"


.. note::

   When using a :ref:`penalty` constraint handler, large forces (those necessary to enforce the constraint) are included in the :math:`b` vector. 
   Even for very small changes in the displacement, if user has selected overly large penalty factor, large forces can appear in the :math:`b` vector.


Examples
--------

The following examples demonstrate the command to create a ``NormUnbalance`` test which allows ``10`` iterations with a 2-norm in the residual :math:`b` vector, i.e. :math:`\sqrt(b \cdot b)` of **1.0e-2**.

.. tabs::

   .. tab:: Tcl 

      .. code-block:: tcl

         test NormUnbalance 1.0e-2  10 2


   .. tab:: Python

      .. code-block:: python

         model.test("NormUnbalance", 1.0e-2, 10, 2)


Code Developed by: |fmk|

