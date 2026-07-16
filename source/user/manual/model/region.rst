.. _region:

Region
------

The region command is used to label a group of nodes and elements.
This command is also used to assign rayleigh damping parameters to the
nodes and elements in this region. 

The region is specified by either elements or nodes, not both.

* If elements are defined, the region
  includes these elements and the all connected nodes, unless the ``-eleOnly``
  option is used in which case only elements are included. 
* If nodes are specified, the region includes these nodes and all elements of which all
  nodes are prescribed to be in the region, unless the ``-nodeOnly`` option is
  used in which case only the nodes are included.


.. function:: region $tag <-ele ($ele1 $ele2 ...)> <-eleOnly ($ele1 $ele2 ...)> <-eleRange $startEle $endEle> <-eleOnlyRange $startEle $endEle> <-node ($node1 $node2 ...)> <-nodeOnly ($node1 $node2 ...)> <-nodeRange $startNode $endNode> <-nodeOnlyRange $startNode $endNode> <-node all> <-rayleigh $alphaM $betaK $betaKinit $betaKcomm >

.. csv-table::

   $tag, unique integer tag
   $ele1 $ele2 ..., tags of selected elements in domain to be included in region (optional, default: omitted)
   $node1 $node2 ..., tags of selected nodes in domain to be included in region (optional, default: omitted)
   $startEle $endEle, tag for start and end elements -- range of selected elements in domain
   $startNode $endNode, tag for start and end nodes -- range of nodes in domain
   $alphaM $betaK $betaKinit $betaKcomm, Arguments to define Rayleigh damping matrix (optional, default: zero)

