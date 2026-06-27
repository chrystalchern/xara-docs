.. _eleResponse:

``eleResponse``
***************

This command is used to obtain state information from an element. 

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.eleResponse(tag, *args)
               
   .. tab:: Tcl 

      .. function:: eleResponse $tag $args ....

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, integer tag identifying element
         $args,  |list|, list of the arguments

The quantities that can be obtained from the element are the same as that which can be obtained using the :ref:`elementRecorder`. Note:

#. The values obtained are for the *current* state of the element. 
#. The arguments are specific to the type of element being used and are the same as those that are used in :ref:`elementRecorder`.

Example
-------

Then following code can be used to obtain the *current* state related to the **forces** and the **material stress** in element **1**, a Truss element.

1. **Tcl Code**

   .. code-block:: Tcl

      set forces [eleResponse 1 forces]
      set stress [eleResponse 1 material stress]


1. **Python Code**

   .. code-block:: python

      forces = model.eleResponse(1, "forces")
      stress = model.eleResponse(1, 'material', "stress")

Code developed by: |fmk|

