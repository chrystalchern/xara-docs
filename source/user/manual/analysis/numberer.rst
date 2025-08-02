.. _numberer:

numberer
^^^^^^^^

The *numberer* determines the mapping between equation numbers in the system of equations and the degrees-of-freedom at the nodes.
Although this has no effect on the solution, it can have a significant effect on the efficiency of the solution process.


.. tabs::
   
   .. tab:: Python
      
      .. py:method:: Model.numberer(type, *args)

         Set the numberer type to be used by the :class:`Model`.

         :param string type: The numberer type.
         :param args: A sequence of arguments for that type.

   .. tab:: Tcl

      .. function:: numberer type? args? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
      
         $type, |string|,  the numberer type
         $args, |list|,   a sequence of arguments for that type

The following numberers are available:

.. toctree::
   :maxdepth: 1

   Plain <numberer/PlainNumberer>
   RCM (Reverse Cuthill McKee) <numberer/RCM>
   AMD (Alternative Min Degree) <numberer/AMD>

Code developed by: |fmk|
