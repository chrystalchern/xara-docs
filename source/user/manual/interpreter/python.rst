
Python
^^^^^^


With |xara|, nearly everything is done through an instance of the :ref:`Model <modelClass>` class.
Rather than invoking functions directly from the *xara* module, one instead typically creates
an *instance* of a model, 

.. code:: Python
   
   import xara
   model = xara.Model(ndm=2, ndf=2)

then constructs and analyzes a finite element simulation by invoking its *methods*:

.. code:: Python
   
   model.node(1, (0.0, 0.0))
   model.node(2, (1.0, 0.0))
   model.material("Elastic", 1, 29e3, 0.3)
   model.element("Truss", 1, (1, 2), 1, 20.0)
   model.analysis("Static")
   model.analyze(1)

Documentation of these methods is organized as follows:

* :ref:`Modeling <modeling>` methods are used to add components to the finite element model.
* :ref:`Loading <pattern>` methods are used to define loads and load patterns.
* :ref:`Analysis <lblAnalysisCommands>` methods are used to move the state of the model from one converged state to another via a number of trial steps.
* :ref:`Output <output>` methods allow one to obtain output from a finite element analysis, e.g. to record the node displacement history.

