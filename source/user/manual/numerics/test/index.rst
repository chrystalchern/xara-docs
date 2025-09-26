.. _test:

test
****

This method is used to define the *Convergence Test*. 
The convergence test is used by an :ref:`algorithm` to detect if convergence has been achieved. 

.. tabs::
   .. tab:: Python
      .. py:method:: Model.test(type, *args)

         :param type: the type of convergence test to be used
         :type type: str
         :param args: the arguments required for the specified convergence test
         :return: None
         :rtype: None

   .. tab:: Tcl

      .. function:: test type? args? ...

The following contain information about ``type`` and the ``args`` required for each of the available system types:

.. toctree::
   :maxdepth: 1

   NormUnbalance
   NormDispIncr
   NormEnergyIncr
   RelativeNormUnbalance
   RelativeNormDispIncr
   RelativeEnergyIncr
   TotalRelativeNormDisplacementIncrement
   FixedNumberIterations


Theory
------


The convergence test is applied to the linearized residual :math:`\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}` stored in the :ref:`system`. 
In the finite element setting and under normal integration schemes and algorithms, the :math:`\boldsymbol{x}` corresponds to the displacement increment and :math:`\boldsymbol{b}` the equilibrium residual.
