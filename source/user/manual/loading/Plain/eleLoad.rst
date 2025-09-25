.. _eleLoad:

eleLoad
^^^^^^^

The eleLoad command is used to define distributed loads within elements.

.. function:: eleLoad {*}$args ...

.. note::

   The load values are reference loads values; it is the time series that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.


.. warning::

   At the moment, eleLoads do not work with 3D :ref:`Frame <frame>` elements if the :ref:`Corotational <CorotTR>` geometric transformation is used.


Examples
--------

.. code:: tcl

   set width 20.0
   set W 4000.0;
   timeSeries Linear 1
   pattern Plain 1 1 {
       eleLoad -ele 3 -type -beamUniform [expr -$W/$width]
   }

.. code:: Python

   width = 20.0;
   W = 4000.0;
   model.pattern("Plain", 1, "Linear")
   model.eleLoad("-ele",3, "-type", "-beamUniform", W/width, pattern=1)

Code Developed by: |fmk|

