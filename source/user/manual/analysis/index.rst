.. _lblAnalysisCommands:


Analysis
^^^^^^^^

.. list-table::
   :widths: 10, 40

   * - :ref:`solve <StaticAnalysis>`
     - Perform a static analysis.
   * - :ref:`trace <TraceAnalysis>`
     - Perform a nonlinear static analysis with load factor control.
   * - ``integrate``
     - Perform a dynamic analysis.
   * - ``eigen``
     - Perform an eigenvalue analysis.
   * - ``spectrum``
     - Perform a response spectrum analysis.


.. toctree::
   :maxdepth: 1
   :hidden:

   solve/index
   trace/index
   integrate/index
   eigen/index
   eigen/modes
   spectrum/index


Several additional aspects of the analysis procedure can be controlled in detail. 
These include:

#. :ref:`constraints <ConstraintHandler>` – Manages the enforcement of constraint equations during the analysis
#. :ref:`numberer <numberer>` – Establishes the correspondence between equation numbers in the system of equations and the degrees of freedom at the nodes.
#. :ref:`system <system>` – Defines the storage and solution algorithm for the linearized residual equations :math:`\boldsymbol{A}x=\boldsymbol{b}`.
#. :ref:`test <test>` – Identifies when the analysis has achieved convergence.

