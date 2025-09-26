.. _KrylovNewton:

Accelerated Newton
^^^^^^^^^^^^^^^^^^

Accelerated Newton algorithms are designed to mitigate the slow convergence of the Modified Newton method and to accommodate complications such as tangent inconsistency, all while imposing minimal additional computational overhead.


.. tabs::

   .. tab:: Python
      
      .. py:method:: Model.algorithm("AcceleratedNewton", iterate='current', increment='current', maxDim=3, accelerator='raphson')
         :no-index:
         
         :param iterate: tangent to iterate on, options are ``current``, ``initial``, ``None``. default is ``current``. 
         :type iterate: |string|
         :param increment: tangent to increment on, options are ``current``, ``initial``, ``None``. default is ``current`` 
         :type increment: |string|
         :param maxDim: max number of iterations within a time step before the tangent is reformed and acceleration restarts (default = 3)
         :type maxDim: |float|

   .. tab:: Tcl
      
      .. function:: algorithm KrylovNewton <-iterate $tangIter> <-increment $tangIncr> <-maxDim $maxDim> 

      .. list-table:: 
        :widths: 10 10 40
        :header-rows: 1

        * - Argument
          - Type
          - Description
        * - $tangIter
          - |string|
          - tangent to iterate on, options are current, initial, noTangent. default is current. 
        * - $tangIncr
          - |string|
          - tangent to increment on, options are current, initial, noTangent. default is current 
        * - $maxDim
          - |float|
          - max number of iterations until the tangent is reformed and acceleration restarts (default = 3)  of iterations within a time step until a new tangent is formed


Accelerators
------------

Krylov-Newton
=============

The *KrylovNewton* algorithm uses a modified :ref:`Newton` method with Krylov subspace acceleration to advance to the next time step. 
The accelerator is described by Carlson and Miller (1998) and Scott and Fenves (2010).


Secant 
=======

The *SecantNewton* algorithm uses the two-term update to accelerate the convergence of the modified Newton method. 

.. note::

   * The default "cut-out" values recommended by Crisfield (R1=3.5, R2=0.3) are used. 


Examples
--------

The following examples demonstrate the command to create a SecantNewton solution algorithm.

.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.algorithm('SecantNewton', 
                         iterate='current', 
                         increment='current',
                         maxDim=3)

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm SecantNewton -iterate current -increment current -maxDim 3


References
----------

* Crisfield, M.A. "Non-linear Finite Element Analysis of Solids and Structures", Vol. 1, Wiley, 1991. 
* Carlson and Miller "Design and Application of a 1D GWMFE Code" SIAM Journal of Scientific Computing (Vol. 19, No. 3, pp. 728-765, May 1998)
* Scott, M.H. and G.L. Fenves. "A Krylov Subspace Accelerated Newton Algorithm: Application to Dynamic Progressive Collapse Simulation of Frames." Journal of Structural Engineering, 136(5), May 2010. DOI 
