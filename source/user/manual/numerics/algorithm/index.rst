algorithm 
==========


.. list-table::
   :widths: 25 75

   * - :ref:`Linear <LinearAlgorithm>`
     - A linear algorithm that does not iterate.
   * - :ref:`Newton <Newton>`
     - The standard Newton-Raphson algorithm.
   * - :ref:`NewtonLineSearch <NewtonLineSearch>`
     - A Newton-Raphson algorithm with a line search.
   * - :ref:`ModifiedNewton <ModifiedNewton>`
     - A modified Newton-Raphson algorithm that does not update the tangent matrix at each iteration.
   * - :ref:`QuasiNewton <KrylovNewton>`
     - An accelerated Newton-Raphson algorithm that uses subspace iteration to accelerate convergence.
   * - :ref:`Broyden <Broyden>`
     - A quasi-Newton algorithm that uses Broyden's method to update the tangent matrix.

.. toctree::
   :hidden:
   :maxdepth: 1

   LinearAlgorithm
   Newton
   NewtonLineSearch
   ModifiedNewton
   QuasiNewton
   Broyden
   ExpressNewton


