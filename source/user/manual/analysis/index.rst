.. _lblAnalysisCommands:


Analysis
^^^^^^^^

Similar to modeling commands, all analysis commands should be executed as methods of the :ref:`Model <modelClass>` class.

The primary methods which determine *what* analysis is performed are:

#. :ref:`integrator <integrator>` Specifies the equations to solve, the predictive steps, and the method for updating the model state.
#. :ref:`algorithm <algorithm>` Outlines the sequence of steps to solve the non-linear equations at each analysis *step*.

Analysis is performed by invoking the :py:meth:`Model.analyze` method:

.. code:: Python

   model.analyze(1)

 
Several additional aspects of the analysis procedure can be controlled in detail. 
These include:

#. :ref:`constraints <ConstraintHandler>` – Manages the enforcement of constraint equations during the analysis
#. :ref:`numberer <numberer>` – Establishes the correspondence between equation numbers in the system of equations and the degrees of freedom at the nodes.
#. :ref:`system <system>` – Defines the storage and solution algorithm for the linearized residual equations :math:`\boldsymbol{A}x=\boldsymbol{b}`.
#. :ref:`test <test>` – Identifies when the analysis has achieved convergence.


.. toctree::
   :hidden:
   :maxdepth: 1

   analysis
   integrator
   algorithm
   analyze
   constraints
   system
   test
   eigen
   modalProperties
   responseSpectrumAnalysis


..
   numberer

