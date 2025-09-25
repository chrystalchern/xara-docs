.. _ConstraintHandler:

constraints
^^^^^^^^^^^

The *ConstraintHandler* determines how the constraint equations are enforced in the analysis. 
Constraint equations define a specified value for a DOF, or a relationship between DOFs.

.. tabs::
   
   .. tab:: Python
      .. py:method:: Model.constraints(type, *args)

         Configure the *ConstraintHandler* for a :class:`Model`. 

   .. tab:: Tcl
      .. function:: constraints type? arg1? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
         
         ``type``, |string|,  the constraints type
         ``args``, |list|,   a list of arguments for that type


The following contain information about ``type`` and the ``args`` required for each of the available constraint handlers:

.. toctree::
   :maxdepth: 1

   PlainConstraints
   PenaltyMethod
   TransformationMethod
   lagrangeMultipliers
   Auto
