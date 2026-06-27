.. _getCrdTransfTags:

getCrdTransfTags
^^^^^^^^^^^^^^^^

This command returns a list of all defined coordinate transformation tags

.. py:method:: Model.getCrdTransfTags()


Examples
--------

This example creates a set of **geomTransf** objects and the asks for a list of all the created objects using the 
method ``getCrdTransfTags`` and assigning the list to the variable called ``tags``.


1. **Tcl Code**

   .. code-block:: tcl

      model BasicBuilder -ndm 3 -ndf 6
      
      geomTransf Linear 1  0 -1 0    -jntOffset 100  0   0      0  0  0              
      geomTransf Linear 2  0 -1 0    -jntOffset 0    0   0      0  0  0              
      geomTransf Linear 3  0 -1 0    -jntOffset 0    0   0      0  0  0              
      geomTransf Linear 4  0 -1 0    -jntOffset 0    0   0      0  0  0              
      geomTransf Linear 5  0 -1 0    -jntOffset 0    0   0      0  0  0              
      
      set allCrdTransfTags [getCrdTransfTags]
      
      puts $allCrdTransfTags

2. **Python Code**

   .. code-block:: python

      model xara.Model(ndm=3, ndf=6)

      model.geomTransf("Linear", 1,  (0, -1, 0), jntOffset=(100, 0,  0,     0, 0, 0))
      model.geomTransf("Linear", 2,  (0, -1, 0), jntOffset=(0  , 0,  0,     0, 0, 0))
      model.geomTransf("Linear", 3,  (0, -1, 0), jntOffset=(0  , 0,  0,     0, 0, 0))
      model.geomTransf("Linear", 4,  (0, -1, 0), jntOffset=(0  , 0,  0,     0, 0, 0))
      model.geomTransf("Linear", 5,  (0, -1, 0), jntOffset=(0  , 0,  0,     0, 0, 0))

      tags = model.getCrdTransfTags()


Code developed by: |fmk|

