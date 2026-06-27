State
^^^^^

The following methods are used to retrieve information about a solution after an :ref:`analysis <lblAnalysisCommands>` has been performed.
*Global* methods pertain to assembled quantities like the residual and stiffness matrix, while *Nodal* methods
can be used to get quantities at specific :ref:`nodes <node>`.


State information may generally be obtained by three approaches:

* The simplest approach is to invoke a response method on a :py:class:`xara.Model` object.
* A *Recorder* object writes state information to a file during an analysis.
* A *Response* object avoids repeated memory allocations and is more efficient for repeated queries. 

The response methods and recorders are inherited from |OpenSees|, while the response classes are a feature of |xara|.


.. toctree::
   :maxdepth: 1
   :caption: Model

   model/printA
   model/printB
   model/getTime
   recorder/index

.. _nodeOutput:

.. toctree::
   :maxdepth: 1
   :caption: Nodes

   nodeResponse
   nodeCoord
   nodeAccel
   nodeDisp
   nodeVel
   nodeRotation
   nodeEigenvector
   nodeUnbalance


.. toctree::
   :maxdepth: 1
   :caption: Elements

   ElementResponse
   ElementRecorder
   eleResponse

