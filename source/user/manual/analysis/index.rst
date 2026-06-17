.. _lblAnalysisCommands:


Analysis
^^^^^^^^

.. list-table::
   :widths: 10, 40

   * - :ref:`StaticAnalysis <StaticAnalysis>`
     - Perform a static analysis.
   * - :ref:`TransientAnalysis <TransientAnalysis>`
     - Perform a dynamic analysis.


.. toctree::
   :maxdepth: 1
   :hidden:

   static/index
   transient/index
   eigen/index
   eigen/modes

..
   spectrum/index


Several additional aspects of the analysis procedure can be controlled in detail. 
These include:

#. :ref:`constraints <ConstraintHandler>` – Manages the enforcement of constraint equations during the analysis
#. :ref:`numberer <numberer>` – Establishes the correspondence between equation numbers in the system of equations and the degrees of freedom at the nodes.
#. :ref:`system <system>` – Defines the storage and solution algorithm for the linearized residual equations :math:`\boldsymbol{A}x=\boldsymbol{b}`.
#. :ref:`test <test>` – Identifies when the analysis has achieved convergence.

