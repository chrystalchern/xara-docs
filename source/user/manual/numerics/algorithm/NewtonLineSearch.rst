.. _NewtonLineSearch:

Line Search
^^^^^^^^^^^

This command is used to select a NewtonLineSearch algorithm which introduces line search to the Newton-Raphson algorithm to solve the nonlinear residual equation. 
Line search increases the effectiveness of the Newton method when convergence is slow due to roughness of the residual. 

.. tabs::
   .. tab:: xara 
      .. autoclass:: xara.algorithm.NewtonLineSearch

   .. tab:: Python 

      .. py:method:: Model.algorithm("NewtonLineSearch", [ratio, maxIter, minEta, maxEta, type="InitialInterpolated"])
         :no-index: 

         Configure the *NewtonLineSearch* algorithm.

         :param ratio: limiting ratio between the residuals before and after the incremental update (between 0.5 and 0.8)
         :param maxIter: integer value of the maximum number of iterations to try. Optional; default is 10.
         :param minEta: float value of a minimum :math:`\eta` value. Optional; default is 0.1.
         :param maxEta: float value of a maximum :math:`\eta` value. Optional; default is 10.0.
         :param type: string specifying the line search algorithm. Optional; default is ``InitialInterpolated``. Valid types are: ``Bisection``, ``Secant``, ``RegulaFalsi``, ``InitialInterpolated``.
   

   .. tab:: OpenSees

      .. function:: algorithm NewtonLineSearch <-type $name> <-tol $tol> <-maxIter $maxIter> <-minEta $minEta> <-maxEta $maxEta> 

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         name, |string|,  "Line Search algorithm. Optional, default is ``InitialInterpolated``. Valid types are: ``Bisection``, ``Secant``, ``RegulaFalsi``
         ``InitialInterpolated``."
         tol, |float|,  tolerance for search. optional. The default is 0.8.
         maxIter, |integer|, maximum number of iteration to try. The default is 10.
         minEta, |float|, a minimum :math:`\eta` value. Optional; The default is 0.1
         maxEta, |float|, a maximum :math:`\eta` value. Optional; The default is 10.0


Theory
------

The rationale behind line search is that:

1. The direction behind :math:`\delta_U` found by the Newton-Raphson method is often a good direction, but the step size :math:`\Delta_U` is not.
2. It is cheaper to compute the residual for several point along :math:`\Delta_U` rather than form and factor a new system Jacobian.

In NewtonLineSearch, the regular Newton-Raphson method is used to compute the :math:`\Delta_U` but the update that is used is modified.. The modified update is:

:math:`U_{n+1} = U_n + \eta \delta_U`


The different line search algorithms use different root finding methods to obtain :math:`\eta`, a root to the function :math:`s(\eta)` defined as: 

:math:`s_\eta = \delta_U R(U_{n} + \eta \delta_U)`

with :math:`s_0 \triangleq \delta-U R(U_n)`

Code Developed by: |fmk|


Examples
--------


.. tabs::
   
   .. tab:: Python

      .. code-block:: python

         model.algorithm("NewtonLineSearch", 0.6)

   .. tab:: OpenSees

      .. code-block:: tcl

         algorithm NewtonLineSearch 0.6
