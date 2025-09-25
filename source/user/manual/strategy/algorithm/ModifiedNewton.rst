.. _ModifiedNewton:

ModifiedNewton
^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.algorithm("ModifiedNewton" [, initial=False])
         :no-index:

         :param initial: optional flag to indicate to use initial stiffness iterations
         :param type: |bool| 

   .. tab:: Tcl

      .. function:: algorithm ModifiedNewton <-initial> 

      .. list-table:: 
         :widths: 10 10 40
         :header-rows: 1

         * - Argument
           - Type
           - Description
         * - ``-initial``
           - |string|
           - optional flag to indicate to use initial stiffness iterations

The ModifiedNewton algorithm uses the modified Newton-Raphson algorithm to solve the nonlinear residual equation. 

Example 
-------

The following examples demonstrate the command to create a ModifiedNewton solution algorithm.

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm ModifiedNewton -initial

   .. tab:: Python

      .. code-block:: python

         model.algorithm("ModifiedNewton", initial=True)
