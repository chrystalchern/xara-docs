.. _modeling:

.. py:currentmodule:: xara


Modeling
^^^^^^^^

..
  A finite element model consists of **Nodes**, **Elements**, **Constraints**, and **Loads**. 
  Constraints are divided into two types: *single-point constraints* for specifying the boundary condition for a specific degree-of-freedom at a node and *multiple-point constraints* for specifying the relationship between the responses between the degrees-of-freedom at two separate nodes. 
  Loads in are assigned to **LoadPatterns**. 
  Also associated with load patterns are **TimeSeries** objects and sometimes constraints when specifying time-varying single-point constraints. 

The *Modeling* methods are used to programatically build a finite element model. 


.. toctree::
   :maxdepth: 1

   model/model_class
   model/spConstraints
   material/index
   section
   model/element
   model/geomTransf
   model/beamIntegration
   model/constraints/index
   model/damping
   model/mass
   parameter/index


Misc.
-----

.. toctree::
   :maxdepth: 1

   model/region
   model/remove


