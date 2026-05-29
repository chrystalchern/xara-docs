.. _constrain:

constrain
^^^^^^^^^

The ``constrain`` command imposes a multi-point constraint between two nodes.
When no rotation is specified, it behaves like :ref:`equalDOF`, constraining the degrees-of-freedom at the constrained node to equal those at the retained node.
When a rotation vector is provided, the constraint enforces a rotated relationship between the nodes through a rotation matrix.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.constrain(rNode, cNode, rotate=None)

         Impose a multi-point constraint between a retained node and a constrained node.

         :param int|tuple rNode: integer tag identifying the retained node, or tuple (rNode, cNode) for both nodes
         :param int cNode: integer tag identifying the constrained node (required if rNode is not a tuple)
         :param list rotate: optional rotation vector [v1, v2, v3] representing axis-angle in radians (see :ref:`Rotation Vector <constrain-rotation-vector>` below). Only available for 3D problems (ndm=3, ndf=6).
         :return: None

   .. tab:: Tcl

      .. function:: constrain $rNodeTag $cNodeTag <-rotate {v1 v2 v3}>

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $rNodeTag, |integer|, integer tag identifying the retained node (*rNode*)
         $cNodeTag, |integer|, integer tag identifying the constrained node (*cNode*)
         -rotate {v1 v2 v3}, |optional|, rotation vector representing axis-angle in radians (see :ref:`Rotation Vector <constrain-rotation-vector>` below). Only available for 3D problems (ndm=3, ndf=6).


Theory
------

The ``constrain`` command creates a multi-point constraint that enforces the relationship :math:`\boldsymbol{u}_c = \boldsymbol{C}_{cr} \boldsymbol{u}_r`, where :math:`\boldsymbol{u}_c` is the response vector at the constrained node, :math:`\boldsymbol{u}_r` is the response vector at the retained node, and :math:`\boldsymbol{C}_{cr}` is the constraint matrix.

.. _constrain-without-rotation:

Without Rotation
~~~~~~~~~~~~~~~~

When no rotation is specified, the constraint matrix is the identity matrix, resulting in behavior equivalent to :ref:`equalDOF`: :math:`\boldsymbol{C}_{cr} = \boldsymbol{I}`.
This form of the constraint works for both 2D and 3D problems.

With Rotation
~~~~~~~~~~~~~

When a rotation vector :math:`\boldsymbol{v} = [v_1, v_2, v_3]` is provided, the rotation matrix :math:`\boldsymbol{R}` is computed using `Rodrigues' rotation formula <https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula#:~:text=In%20terms%20of%20the%20matrix%20exponential%2C>`_ as the matrix exponential :math:`\boldsymbol{R} = \exp(\theta \boldsymbol{K})`, where :math:`\theta` is the magnitude of the rotation vector and :math:`\boldsymbol{K}` is the skew-symmetric matrix corresponding to the normalized rotation axis.

.. _constrain-rotation-vector:

Rotation Vector
~~~~~~~~~~~~~~~

The rotation vector uses the **axis-angle representation**: the normalized direction defines the rotation axis, and the magnitude is the rotation angle in radians. The rotation follows the **right-hand rule**: a positive angle rotates counterclockwise when viewed from the tip of the axis vector.

In 3D models, the components :math:`[v_1, v_2, v_3]` correspond to rotations about the global X, Y, and Z axes respectively:
- :math:`[\theta, 0, 0]` rotates about the X-axis
- :math:`[0, \theta, 0]` rotates about the Y-axis
- :math:`[0, 0, \theta]` rotates about the Z-axis

The coordinate system and degrees-of-freedom conventions are documented in :ref:`Conventions <conventions>`.

For 3D problems (ndm=3, ndf=6), the constraint matrix is:

.. math::

   \boldsymbol{C}_{cr} = \begin{bmatrix}
          \boldsymbol{R} & \boldsymbol{0} \\
          \boldsymbol{0} & \boldsymbol{R}
   \end{bmatrix}

where the upper-left block applies the rotation matrix :math:`\boldsymbol{R}` to translational degrees-of-freedom (1-3), and the lower-right block applies the same rotation matrix to rotational degrees-of-freedom (4-6).

.. note::

   **3D limitation:** The rotation option is only implemented for 3D problems (ndm=3, ndf=6) because Rodrigues' formula requires a 3D rotation vector, and the constraint matrix applies the rotation to all six degrees-of-freedom.

   **2D alternative:** For 2D problems requiring rotated constraints (e.g., skewed supports), use the penalty method with :ref:`zeroLength <zeroLength>` elements, as demonstrated in the :ref:`Penalty Method for Skewed Supports in 2D <zeroLength-penalty-2d>` example.

   **Rotational DOF approximation:** The same rotation matrix :math:`\boldsymbol{R}` is applied to both translational and rotational DOFs. While this is a proper coordinate transformation for translational DOFs, it is an approximation for rotational DOFs (treating rotations as vectors) that is valid for small rotations but may have limitations for large finite rotations.

Examples
--------


.. ref-gallery::
    :tooltip:

    examples/general/model-0001


Basic Constraint (No Rotation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates the basic usage of ``constrain`` without rotation, corresponding to the :ref:`Without Rotation <constrain-without-rotation>` theory section above. When no rotation is specified, the constraint matrix is the identity matrix :math:`\boldsymbol{C}_{cr} = \boldsymbol{I}`, making this equivalent to :ref:`equalDOF`.

The following example constrains node **5** to have the same degrees-of-freedom as node **100**. This works for both 2D and 3D problems:

.. tabs::
   .. tab:: Python

      .. code-block:: python

         model.constrain(100, 5)

   .. tab:: Tcl

      .. code-block:: none

         constrain 100 5

Constraint with Rotation
~~~~~~~~~~~~~~~~~~~~~~~~~

The following example constrains node **5** to node **100** with a rotation about the Y-axis. This requires a 3D model (ndm=3, ndf=6):

.. tabs::
   .. tab:: Python

      .. code-block:: python

         angle = 0.5  # Rotation angle in radians (about 28.6 degrees)
         # Negative sign rotates clockwise about Y-axis (right-hand rule)
         model.constrain(100, 5, rotate=[0, -angle, 0])

   .. tab:: Tcl

      .. code-block:: none

         constrain 100 5 -rotate {0 -0.6435 0}


References
----------

*  Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., "Concepts and Applications of Finite Element Analysis," 4th edition, John Wiley and Sons publishers, 2002.

*  `Rodrigues' rotation formula <https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula>`_ - Wikipedia article on Rodrigues' rotation formula.

