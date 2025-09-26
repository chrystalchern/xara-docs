.. _FixedNumberIterations:

Fixed Iterations
^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.test("Count", niter [, verbosity=0])
         :no-index:

         Configure the analysis to perform a fixed number of iterations

         :param niter: number of iterations to perform
         :type niter: |integer|
         :param verbosity: verbosity level (default is 0)
         :type verbosity: |integer|

    
   .. tab:: Tcl 

      .. function:: test "FixedNumIter" numIter
         :no-index:


This test is particularly useful for hybrid simulations, or in conjunction with the ``operation`` 
keyword in the :py:meth:`Model.analyze` method for detailed control over the analysis procedure.
