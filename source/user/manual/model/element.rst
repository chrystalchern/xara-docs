.. _element:

Element
*******


.. tabs::

   .. tab:: Python

      .. py:method:: Model.element(type, tag, nodes, *args, **kwds)

         Construct an element and add it to the :class:`Model`. 

         :param |string| type: name of the element type to be added
         :param |integer| tag: tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param args, kwds: arguments particular to the element ``type``


   .. tab:: Tcl

      .. function:: element $type $tag (num $nodes) $args ...

         Construct an element and add it to the :class:`Model`. 

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``type``, |string|,      element type
         ``tag``,  |integer|,     unique element tag.
         ``nodes``,   |integerlist|, a list of element nodes with number dependent on ele type
         ``args``, |list|,        a list of element arguments with number dependent on ele type

The following subsections contain information about ``type`` and the number of nodes and args required for each of the available element types:

.. toctree::
   :maxdepth: 2

   elements/frame/index
   elements/Truss
   elements/plane/index
   elements/shell/index
   elements/solid/index
   elements/joint/index
   elements/other/index
   elements/fluid/index
   elements/bearing/index



