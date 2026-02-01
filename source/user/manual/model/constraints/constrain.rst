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

Basic Constraint (No Rotation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates the basic usage of ``constrain`` without rotation, corresponding to the :ref:`Without Rotation <constrain-without-rotation>` theory section above. When no rotation is specified, the constraint matrix is the identity matrix :math:`\boldsymbol{C}_{cr} = \boldsymbol{I}`, making this equivalent to :ref:`equalDOF`.

The following example constrains node **5** to have the same degrees-of-freedom as node **100**. This works for both 2D and 3D problems:

.. tabs::
   .. tab:: Tcl

      .. code-block:: none

         constrain 100 5

   .. tab:: Python

      .. code-block:: python

         model.constrain(100, 5)

Constraint with Rotation
~~~~~~~~~~~~~~~~~~~~~~~~~

The following example constrains node **5** to node **100** with a rotation about the Y-axis. This requires a 3D model (ndm=3, ndf=6):

.. tabs::
   .. tab:: Tcl

      .. code-block:: none

         constrain 100 5 -rotate {0 -0.6435 0}

   .. tab:: Python

      .. code-block:: python

         angle = 0.5  # Rotation angle in radians (about 28.6 degrees)
         # Negative sign rotates clockwise about Y-axis (right-hand rule)
         model.constrain(100, 5, rotate=[0, -angle, 0])

Frame with Skewed Support
~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates using ``constrain`` to model a frame with a skewed support in 3D, where the support is not aligned with the global coordinate system.

.. code-block:: python
   :linenos:

   import xara
   from xara.units.english import inch, kip, ksi
   from shps.rotor import exp

   # Geometry
   H = 144.0 * inch
   W = 144.0 * inch

   # Section properties
   width = 12.0 * inch
   height = 12.0 * inch
   Iz = (width * height**3) / 12.0
   Iy = (height * width**3) / 12.0
   A = width * height
   J = (width * height**3) / 3.0

   # Material
   E = 29000 * ksi
   G = 11500 * ksi
   nu = 0.30

   # Load
   P = -10.0 * kip
   angle = 0.5  # Rotation angle in radians (about 28.6 degrees)
   # Negative sign rotates clockwise about Y-axis (right-hand rule),
   # rotating the support coordinate system clockwise from vertical

   # Compute rotation matrix for reaction transformation
   R = exp([0.0, -angle, 0.0])

   # Model (3D required for rotation)
   model = xara.Model('basic', ndm=3, ndf=6)

   # Nodes
   model.node(1, (0.0, 0.0, 0.0))      # Fixed support
   model.node(2, (0.0, 0.0, H))        # Top-left
   model.node(3, (W/2, 0.0, H))        # Load point
   model.node(4, (W,   0.0, H))        # Top-right
   model.node(5, (W,   0.0, 0.0))      # Skewed support

   # Fixed support at node 1
   model.fix(1, (1, 1, 1, 1, 1, 1))

   # Ground node for skewed support
   ground_node = 100
   model.node(ground_node, (W, 0.0, 0.0))
   model.fix(ground_node, (0, 1, 1, 0, 0, 0))  # Fixed in Y and Z, free in X

   # Apply rotated constraint: node 5 is constrained to ground_node with rotation
   model.constrain((ground_node, 5), rotate=[0, -angle, 0])

   # Frame section and elements
   model.material('ElasticIsotropic', 1, E, nu)
   model.section("ElasticFrame", 1, E=E, G=G, A=A, Iy=Iy, Iz=Iz, J=J)
   model.geomTransf("Linear", 1, (0, 1, 0))  # Columns
   model.geomTransf("Linear", 2, (0, 1, 0))  # Beams

   model.element('PrismFrame', 1, (1, 2), section=1, transform=1)
   model.element('PrismFrame', 2, (2, 3), section=1, transform=2)
   model.element('PrismFrame', 3, (3, 4), section=1, transform=2)
   model.element('PrismFrame', 4, (4, 5), section=1, transform=1)

   # Load
   model.timeSeries('Constant', 1)
   model.pattern('Plain', 1, 1)
   model.load(3, (0.0, 0.0, P, 0.0, 0.0, 0.0))

   # Analysis
   model.system('BandGeneral')
   model.numberer('RCM')
   model.constraints('Transformation')
   model.integrator('LoadControl', 1.0)
   model.algorithm('Newton')
   model.test('Energy', 1e-8, 10)
   model.analysis('Static')
   model.analyze(1)

   # Results
   model.reactions()

   # Reaction at fixed support (node 1)
   Fz_jt1 = model.nodeReaction(1, 3) / kip
   print(f"Reaction at node 1 (Z-direction): {Fz_jt1:.3f} kip")

   # Reaction at skewed support (node 5) - transform to rotated coordinate system
   R4 = model.nodeReaction(5)[:3]  # Get translational reactions (X, Y, Z)
   r4 = R.T @ R4 / kip  # Transform to rotated coordinate system
   F3_jt4 = r4[2]  # Z-component in rotated coordinate system
   print(f"Reaction at skewed support (node 5, normal direction): {F3_jt4:.3f} kip")

References
----------

*  Cook, R.D., Malkus, D.S., Plesha, M. E., and Witt, R. J., "Concepts and Applications of Finite Element Analysis," 4th edition, John Wiley and Sons publishers, 2002.

*  `Rodrigues' rotation formula <https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula>`_ - Wikipedia article on Rodrigues' rotation formula.

