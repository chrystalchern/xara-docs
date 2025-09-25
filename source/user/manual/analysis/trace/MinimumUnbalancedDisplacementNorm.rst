.. _MinimumUnbalancedDisplacementNorm:

MinUnbalDispNorm
^^^^^^^^^^^^^^^^

.. tabs::
   
   .. tab:: Python 

      .. py:method:: Model.integrator("MinUnbalDispNorm", dlam0 [, jd, min, max])
         :no-index:

         Use the *minimum unbalanced displacement norm* continuation method [1]_
         
         :param dlam0: First load increment (pseudo-time step) at the first iteration in the next invocation of the analysis command.
         :type dlam0: |float|
         :param jd: Factor relating first load increment at subsequent time steps. (optional, default: 1.0)
         :type jd: |float|
         :param min: arguments used to bound the load increment (optional, default: dlam0)
         :type min: |float|
         :param max: arguments used to bound the load increment (optional, default: dlam0)
         :type max: |float|

   .. tab:: Tcl

      .. function:: integrator MinUnbalDispNorm $dlambda11 <$Jd $minLambda $maxLambda>

      .. list-table:: 
         :widths: 10 10 40
         :header-rows: 1

         * - Argument
           - Type
           - Description
         * - $dlambda11
           - |float|
           - First load increment (pseudo-time step) at the first iteration in the next invocation of the analysis command.
         * - $Jd
           - |float|
           - Factor relating first load increment at subsequent time steps. (optional, default: 1.0)
         * - $minLambda
           - |float| 
           - arguments used to bound the load increment (optional, default: $dLambda11)
         * - $maxLambda
           - |float| 
           - arguments used to bound the load increment (optional, default: $dLambda11)

Theory
------

Continuation
~~~~~~~~~~~~

In this method, the constraint equation governing the evolution of :math:`\Delta \lambda` is

.. math::


   \frac{\partial}{\partial \Delta \lambda}\left. d \boldsymbol{u} \cdot d \boldsymbol{u}\right.=0

which guarantees a minimum value for the unbalanced displacement norm in
each iteration. Evaluating the constraint equation furnishes

.. math::

   d \lambda = -\frac{d\hat{\boldsymbol{u}} \cdot d\bar{\boldsymbol{u}}}{d\hat{\boldsymbol{u}} \cdot d\hat{\boldsymbol{u}}}


Incrementation
~~~~~~~~~~~~~~

The load increment at iteration :math:`i`, :math:`d\lambda_{1,i}` , is
related to the load increment at :math:`(i-1)`,
:math:`d\lambda_{1,i-1}`, and the number of iterations at :math:`(i-1)`,
:math:`J_{i-1}`, by the following:

.. math::


   d\lambda_{1,i} = d\lambda_{1,i-1}\frac{J_d}{J_{i-1}}


References
----------

.. [1]  SL Chan, "Geometric and Material Non-Linear Analysis of Beam-Columns and Frames Using the Minimum Residual Displacement Method,"  International Journal for Numerical Methods in Engineering, Vol. 26, No. 12, 1988, pp. 2657-2669.  doi: `10.1002/nme.1620261206 <https://doi.org/10.1002/nme.1620261206>`_

