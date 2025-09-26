.. _RelativeEnergyIncr:

Relative Energy Increment
^^^^^^^^^^^^^^^^^^^^^^^^^


This command is used to construct a convergence test which uses the
dot product of the solution vector and norm of the right hand side of
the matrix equation to determine if convergence has been reached. 
The physical meaning of this quantity depends on the integrator and
constraint handler chosen. Usually, though not always, it is equal to
the energy unbalance in the system. The test is relatively to the first
dot product computed for each step. 

.. function:: test RelativeEnergyIncr $tol $iter < $pFlag > < $nType >


* When using the :ref:`Penalty` method additional large forces to enforce the
  penalty functions exist on the right had side, making convergence using this test usually impossible (even though solution
  might have converged).

* When the :ref:`Lagrange <lagrangeHandler>` constraint handler is used, the solution vector :math:`\boldsymbol{x}` contains the Lagrange multipliers.
