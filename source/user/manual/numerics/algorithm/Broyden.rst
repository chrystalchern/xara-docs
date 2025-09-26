.. _Broyden:

Broyden/BFGS
^^^^^^^

The Broyden algorithm for general unsymmetric systems which performs successive rank-one updates of the tangent at the first iteration of the current time step.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.algorithm("Broyden" [, count, symmetric=False])
         :no-index:
   
   .. tab:: Tcl

      .. function:: algorithm Broyden <$count>

      .. list-table:: 
        :widths: 10 10 40
        :header-rows: 1

        * - Argument
          - Type
          - Description
        * - $count
          - |integer|
          - number of iterations within a time step until a new tangent is formed
    

BFGS 
====


BFGS implements the `Broyden–Fletcher–Goldfarb–Shanno <https://en.wikipedia.org/wiki/BFGS>`_  (BFGS) algorithm for symmetric systems.
This performs successive rank-two updates of the tangent at the first iteration of the current time step.
