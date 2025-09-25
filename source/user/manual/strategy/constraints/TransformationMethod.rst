Transformation
^^^^^^^^^^^^^^

A ``Transformation`` constraint handler enforces the constraints in a model by using the transformation method, also known as *static condensation*. 

.. tabs::

   .. tab:: Python

      .. py:method:: Model.constraints("Transformation")
         :no-index:

   .. tab:: Tcl
      
      .. function:: constraints Transformation


The single-point constraints when using the transformation method are done directly. 
The matrix equation is not manipulated to enforce them, rather the trial displacements are set directly at the nodes at the start of each analysis step.

.. note::

   Great care must be taken when multiple constraints are being enforced as the transformation method does not follow constraints:
   * If a node is fixed, constrain it with the :ref:`fix` command and not :ref:`equalDOF` or any other type of constraint.
   * If multiple nodes are constrained, make sure that the retained node is not constrained in any other constraint.


Example
-------

The following example shows how to construct a transformation constraint handler

1. **Tcl Code**

   .. code-block:: tcl

      numberer Transformation


2. **Python Code**

   .. code-block:: python

      model.numberer('Transformation')

Code Developed by: |fmk|
