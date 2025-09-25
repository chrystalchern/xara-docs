.. _output:

Output
------

Model
=====

The following methods return mesh information for a :py:class`Model`, such as element connectivity and material definitions.

.. toctree::
   :maxdepth: 1

   print
   eleNodes

Solution
========

The following methods are used to retrieve information about a solution after an :ref:`analysis <lblAnalysisCommands>` has been performed.
*Global* methods pertain to assembled quantities like the residual and stiffness matrix, while *Nodal* methods
can be used to get quantities at specific :ref:`nodes <node>`.

.. toctree::
   :maxdepth: 1
   :caption: Global methods

   printA
   printB
   getTime
   recorder


.. toctree::
   :caption: Nodal methods
   :maxdepth: 1

   nodeResponse
   nodeDisp
   nodeVel
   nodeAccel
   nodeCoord   
   nodeRotation
   nodeEigenvector
   getNodeTags


.. toctree::
   :caption: Element methods
   :maxdepth: 1

   getEleTags
   eleNodes 
   eleResponse


.. toctree::
   :caption: Miscellaneous
   :maxdepth: 1

   getEleLoadTags
