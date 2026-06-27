

setNodeCoord
^^^^^^^^^^^^


 .. py:method:: Model.setNodeCoord(tag, dim, value)

    Set the coordinates of a node in a :py:class`Model`. The node must already exist in the model.

    :param tag: The tag of the node to set the coordinates for.
    :type tag: |integer|
    :param dim: The dimension to set the coordinate for (0 for x, 1 for y, 2 for z).
    :type dim: |integer|
    :param value: The coordinate value to set.
    :type value: |float|
