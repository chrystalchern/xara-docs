.. _analysis:

Analysis Classes
^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.analysis(type, *opts)

         Set the analysis type to be performed on the next call to :py:meth:`Model.analyze`.

         :param |string| type: The analysis type. Three variants are supported:

             - :ref:`"Static" <StaticAnalysis>` : for static analysis
             - :ref:`"Transient" <TransientAnalysis>` : for standard dynamic analysis with constant time step
             - **VariableTransient** : for transient analysis with variable time step

         :param opts: Additional optional arguments for the analysis type.

   .. tab:: Tcl

      .. function:: analysis type? <-numSublevels $x -numSubSteps $y>

         .. csv-table:: 
            :header: "Argument", "Type", "Description"
            :widths: 10, 10, 40

            ``type``, |string|, type of analysis to be configured. Three variants are supported:
            , ,  :ref:`"Static" <StaticAnalysis>` - for static analysis
            , ,  :ref:`"Transient" <TransientAnalysis>` - for standard dynamic analysis with constant time step
            , ,  **VariableTransient** - for transient analysis with variable time step
            ``x``, |integer|, number of sublevels transient analysis should try if failure
            ``y``, |integer|, number of subdivisions to be tried at each sublevel


.. toctree::
   :hidden:

   StaticAnalysis
   transient


.. note::

   The components of the analysis, i.e. numberer, constraint handler, system, test, integrator, algorithm, should all be issued **before** the analysis object is created.


The ``<-numSublevels $x -numSubSteps $y>`` options only work for :ref:`Transient <TransientAnalysis>`.

The **VariableTransient** option is still available. The optional additions for the Transient analysis have been found to provide better options for nonlinear problems with convergence issues.


.. warning::

   When switching from one type of analysis to another, e.g. ``Static`` to ``Transient``, it is necessary to issue a :ref:`wipeAnalysis`.


Examples
--------

The following example shows how to construct a Static analysis.

.. tabs::

   .. tab:: Tcl

      .. code:: tcl

         system SuperLU
         constraints Transformation
         numberer RCM
         test NormDispIncr 1.0e-12  10 3
         algorithm Newton
         integrator LoadControl 0.1
         analysis Static

   .. tab:: Python

      .. code:: python

         model.system("SuperLU")
         model.constraints("Transformation")
         model.numberer("RCM")
         model.test("NormDispIncr", 1.0e-12, 10, 3)
         model.algorithm("Newton")
         model.integrator("LoadControl", 0.1)
         model.analysis("Static")


The following example shows how to construct a :ref:`Transient <TransientAnalysis>` analysis.

.. tabs::

   .. tab:: Tcl

      .. code:: tcl

         system SuperLU
         constraints Transformation
         numberer RCM
         test NormDispIncr 1.0e-12  10 3
         algorithm Newton
         integrator Newmark 0.5 0.25
         analysis Transient -numSubLevels 3  -numSubSteps 10

   .. tab:: Python

      .. code:: python

         model.system("SuperLU")
         model.constraints("Transformation")
         model.numberer("RCM")
         model.test("NormDispIncr", 1.0e-12, 10, 3)
         model.algorithm("Newton")
         model.integrator("Newmark", 0.5, 0.25)
         model.analysis("Transient")


Code Developed by |fmk|
