.. _linearTR:

Linear
^^^^^^

A *Linear* coordinate transformation performs a linear geometric transformation of a :ref:`Frame <Frame>` element's response from a basic system to the global coordinate system.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.geomTransf("Linear", tag, vecxz, [offi, offj])
         :no-index:

         :param integer tag: integer tag identifying transformation
         :type tag: |integer|
         :param vecxz: X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system, **required in 3D**. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         :type vecxz: tuple of floats
         :param offi: joint offset values for element end at node *i* (optional, the number of arguments depends on the dimensions of the current model).
         :type offi: tuple of floats
         :param offj: joint offset values for element end at node *j* (optional, the number of arguments depends on the dimensions of the current model).
         :type offj: tuple of floats

   .. tab:: Tcl

      .. function:: geomTransf Linear $transfTag < $vecxzX $vecxzY $vecxzZ > <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $transfTag, |integer|, integer tag identifying transformation
         $vecxzX $vecxzY $vecxzZ,  |float|,  "X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         
         These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.

         These items need to be specified for the three-dimensional problem."
         $dXi $dYi $dZi, |float|, "joint offset values for element end at node *i* (optional, the number of arguments depends on the dimensions of the current model)."
         $dXj $dYj $dZj, |float|, "joint offset values for element end at node *j* (optional, the number of arguments depends on the dimensions of the current model)."


.. note::

   Joint offsets are specified with respect to the global coordinate system


Theory
------

Orientation 
===========

The longitudinal basis vector :math:`\mathbf{i}` is derived from the two element end nodes. 
The vector **vecxz** is a vector the user specifies that must not be parallel to this axis. 
The x-axis along with the **vecxz** Vector define the xz plane. 
The local y-axis is defined by taking the cross product of the x-axis vector and the **vecxz** vector (:math:`\mathbf{i}_y = i_{xz} \times \mathbf{i}`). 
The local z-axis is then found by taking the cross product of the y-axis and x-axis vectors (:math:`\mathbf{i}_z = \mathbf{i} \times \mathbf{i}_y`). 
The section is attached to the element such that the y-z coordinate system used to specify the section corresponds to the y-z axes of the element.


.. note::

   When in 2D, local x and y axes are in the X-Y plane, where X and Y are global axes. 
   Local x axis is the axis connecting the two element nodes, and local y and z axes follow the right-hand rule (e.g., if the element is aligned with the positive Y axis, the local y axis is aligned with the negative X axis, and if the element is aligned with the positive X axis, the local y axis is aligned with the positive Y axis). 
   Orientation of local y and z axes is important for the definition of the :ref:`ShearFiber` section.

Joint Offsets
=============

Joint offsets are specified with respect to the global coordinate system.

Example
-------

.. ref-gallery::

   examples/frames/frame-0059


References
----------

Code Developed by: |rms| 

