.. _load:

load
^^^^

This command is used to define a nodal load.

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.load(tag, load, pattern=None)

         :param tag: integer tag identifying the :meth:`Model.node` on which the load acts
         :param load: tuple of **ndf** load values that are to be applied to the node.
         :param pattern: integer tag identifying the :ref:`pattern` to which the load belongs.

   .. tab:: Tcl

      .. function:: load $tag $LoadValues...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, tag of node on which loads act
         $LoadValues, |listFloat|, **ndf** load values that are to be applied to the node.


The nodal load is added to the LoadPattern being defined in the enclosing scope of the :ref:`pattern` command.


Example
-------

The following example demonstrates how to create a **Linear** time series, and asociate it with a **Plain** load pattern which contains **nodal loads** to be applied to nodes **3** and **4** of reference magnitude **(0,-50)** and **(50.0, -100)** respectivily. 

1. **Tcl Code**

   .. code-block:: tcl

      pattern Plain 1 Linear {
      	load  3   0.0  -50.0  0.0
    	   load  4   50.0  -100.0 0.0
      }

2. **Python Code**

   .. code-block:: python

      model.pattern("Plain", 1, "Linear")
      model.load(3, ( 0.0,  -50.0), pattern=1)
      model.load(4, (50.0, -100.0), pattern=1)

Code Developed by: |fmk|
