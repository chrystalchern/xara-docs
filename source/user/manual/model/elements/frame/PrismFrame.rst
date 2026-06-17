.. _elasticBeamColumn:

``PrismFrame``
^^^^^^^^^^^^^^^

The ``PrismFrame`` element represents a linear-elastic prismatic beam element.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.element("PrismFrame", tag, nodes, *, section, transform, shear=0, *args)
         :no-index:
         
         Create a linear elastic prismatic frame element.
         
         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of *two* integer :ref:`node` tags
         :type nodes: tuple
         :param section: Section object to be created at the element Gauss points. 
         :type section: :py:class:`xara.Section`
         :param transform: identifier for previously-defined coordinate-transformation
         :type transform: |integer|
         :param shear: flag indicating whether shear deformations are included (default is ``0``)
         :type shear: |integer|, optional

   .. tab:: Tcl

      .. function:: element PrismFrame $tag $iNode $jNode $sect $tran

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``tag``, |integer|,	       unique :ref:`element` tag
         ``iNode`` ``jNode`` , |integer|,  end nodes
         ``sect``, |integer|,         section tag
         ``tran``, |integer|,      identifier for previously-defined coordinate-transformation


The valid :ref:`eleResponse` queries to this element are ``"force"``.


Example 
-------

The following example constructs an elastic element with tag ``1`` between nodes **2** and **4** with an area 
of **5.5**, Young's modulus :math:`E` of **100.0** and an Iz of **1e6** which uses the geometric transformation object with a tag of **9**

1. **Tcl Code**

   .. code-block:: tcl

      element PrismFrame 1 2 4 5.5 100.0 1e6 9; 


2. **Python Code**

   .. code-block:: python

      model.element("PrismFrame", 1, (2, 4), 5.5, 100.0, 1.0e6, 9)


Theory
------

.. Warping
.. =======

.. @baigent1982structural


Code developed by: |cmp|, |fmk|

