

getNodePressure
^^^^^^^^^^^^^^^

.. py:method:: Model.getNodePressure(nodeTag)

   Returns the pressure at a node, set with :py:meth:`Model.setNodePressure`.


   where :math:`\sigma_{xx}`, :math:`\sigma_{yy}`, and :math:`\sigma_{zz}` are the normal stresses in the x, y, and z directions, respectively.

   :param nodeTag: The tag of the node for which to retrieve the pressure.
   :type nodeTag: int
   :return: The pressure at the specified node.
   :rtype: float