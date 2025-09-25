.. _RelativeNormUnbalance:

Relative Norm Unbalance
^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a convergence test which uses the norms of the right hand side of the matrix equation, i.e. :math:`b` vector in :math:`Ax=b`, to determine if convergence has been reached. 
It uses the ratio of the current norm to the first norm, i.e. :math:`\frac{\sqrt(\boldsymbol{b}_i \cdot \boldsymbol{b}_i)}{\sqrt({b_1} \cdot {b_1})}`. 


.. tabs::

   .. tab:: Python 

      .. py:method:: Model.test("RelativeNormUnbalance", tol, iter, verbosity=0, norm=2)
         :no-index:

         :param tol: the tolerance criteria used to check for convergence
         :type tol: float  
         :param iter: the max number of iterations to check before returning failure condition
         :type iter: int
         :param verbosity: print flag (optional: default is 0) valid options:
            - 0 print nothing
            - 1 print information on norms each time test() is invoked
            - 2 print information on norms and number of iterations at end of successful test
            - 4 at each step it will print the norms and also the <math>\Delta U</math> and <math>R(U)</math> vectors.
            - 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test.
         :param norm: type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm ...))
         :type norm: int
         :return: None
         :rtype: None
   
   .. tab:: Tcl

      .. function:: test RelativeNormUnbalance $tol $iter <$verb> <$norm>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tol, |float|, the tolerance criteria used to check for convergence
         $iter, |integer|, the max number of iterations to check before returning failure condition
         $verb, |integer|, " | print flag (optional: default is 0) valid options:
         | 0 print nothing
         | 1 print information on norms each time test() is invoked
         | 2 print information on norms and number of iterations at end of successful test
         | 4 at each step it will print the norms and also the <math>\Delta U</math> and <math>R(U)</math> vectors.
         | 5 if it fails to converge at end of $numIter it will print an error message BUT RETURN A SUCCESSFUL test."
         $norm, |integer|, "type of norm (optional: default is 2 (0 = max-norm 1 = 1-norm 2 = 2-norm ...))"


.. note::

   The convergence test compares the current norm of the unbalance with the norm of the first step to determine if convergence has been achieved. As a consequence it will always take at least two steps to achieve convergence.

   If numerically the solution has a very small unbalance at the first step, this may mean that the test may never indicate success even though the solution had indeed converged to a solution. This is because machine precision and numerical round-off limit how small the unbalance can become.


Example
-------

The following examples demonstrate the command to create a RelativeNormUnbalance test which allows 10 iterations till failure with a 2-norm in the :math:`b` vector, i.e. :math:`\sqrt(b \cdot b)` of **1.0e-2**.

1. **Tcl Code**

   .. code-block:: tcl

      test RelativeNormUnbalance 1.0e-2  10 2

2. **Python Code**

   .. code-block:: python

      model.test('RelativeNormUnbalance', 1.0e-2, 10, 2)


Code Developed by: |fmk|
