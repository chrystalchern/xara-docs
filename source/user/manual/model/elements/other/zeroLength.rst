.. _zeroLength:

ZeroLength
^^^^^^^^^^

A ZeroLength element is defined by two nodes at the same location. 
A ZeroLength element is similar to a set of springs placed between two nodes, each spring providing the force displacement relationship for a specified degree-of-freedom. 
The nodes are connected by multiple UniaxialMaterials, which provide the force-deformation relationship for the element in that degree-of-freedom direction.

.. function:: element zeroLength $eleTag $iNode $jNode -mat $matTag -dir $dir <-doRayleigh $rFlag> <-orient $x $yp>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique :ref:`Element` tag
   $endNodes, |integerList|, 2 end nodes
   $matTags, |integerList|, list of **n** material tags
   $dirIDs, |integerList|, "| list of **n** degree-of-freedom directions
   | 1,2,3 - translation along local x,y,z axes,
   | 4,5,6 - rotation about local x,y,z axes"
   $x, |floatList|,  (optional) 3 components in global coordinates defining local x-axis 
   $yp, |floatList|, "| (optional) 3 components in global coordinates defining vector yp 
   | which lies in the local x-y plane for the element."
   $rFlag, |integer|, "| optional, default = 0
   | rFlag = 0 NO RAYLEIGH DAMPING (default)
   | rFlag = 1 include rayleigh damping"


.. note::

   If the optional orientation vectors are not specified, the local element axes coincide with the global axes. Otherwise the local z-axis is defined by the cross product between the vectors x and yp vectors specified on the command line.

   The valid queries to a zero-length element when creating an ElementRecorder object are 'force,' 'deformation,' and 'material $i matArg1 matArg2 ...' Where $i is an integer indicating which of the materials whose data is to be output (a 1 corresponds to $matTag1, a 2 to $matTag2, and so on). 


.. warning::

   If the distance between end noes is not **0.0** a warning will be issued. ZeroLength elements can be used between nodes with non-zero length.


Examples
--------

The following examples demonstrate the commands in a script to add three zeroLength elements to domain. 
The three to be added have element tags **1**, **2**, and **3**. 
Element **1** has nodes **2** and **3** as its end ndes, has two materials **5** and **6** acting in directions **1** and **2**. 
Element **2** has as its end nodes **4** and **5**, has only one material **1** acting in direction **1**, the element has a global orientation.

   1. **Tcl Code**

   .. code-block:: tcl

      element zeroLength 1 2 4 -mat 5 6 -dir 1 2
      element zeroLength 2 4 5 -mat 1 -dir 1 -orient 1 1 0 -1 1 0
      element zeroLength 3 5 6 -mat 1 -dir 1 -doRayleigh 1

   2. **Python Code**

   .. code-block:: python

      model.element("zeroLength",1,2,4,"-mat",(5,6),"-dir",1,2)
      model.element("zeroLength",2,4,5,"-mat",1,"-dir",1,"-orient",1,1,0,-1,1,0)
      model.element("zeroLength",3,5,6,"-mat",1,"-dir",1,"-doRayleigh",1)

.. _zeroLength-penalty-2d:

Penalty Method for Skewed Supports in 2D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ZeroLength elements can be used with the penalty method to model rotated constraints in 2D problems, such as skewed supports. This approach is particularly useful when the :ref:`constrain <constrain>` command's rotation option is not available (it is only implemented for 3D problems).

The penalty method uses a very stiff spring (penalty stiffness) oriented in the desired constraint direction to approximate a rigid constraint. The zeroLength element connects a ground node (with fixed boundary conditions) to the constrained node, with the element's local coordinate system oriented to match the desired constraint direction.

The following example demonstrates modeling a 2D frame with a skewed support using the penalty method with a zeroLength element:

.. code-block:: python
   :linenos:

   import xara
   from xara.units.english import inch, kip, ksi
   from math import atan2
   from shps.rotor import exp

   # Geometry
   H = 144.0 * inch
   W = 144.0 * inch

   # Section properties
   width = 12.0 * inch
   height = 12.0 * inch
   Iz = (width * height**3) / 12.0
   A = width * height

   # Material
   E = 29000 * ksi
   nu = 0.30

   # Load
   P = -10.0 * kip
   angle = atan2(0.6, 0.8)  # Rotation angle for skewed support

   # Model (2D)
   model = xara.Model('basic', ndm=2, ndf=3)

   # Nodes
   model.node(1, (0.0, 0.0))      # Fixed support
   model.node(2, (0.0, H))        # Top-left
   model.node(3, (W/2, H))        # Load point
   model.node(4, (W,   H))        # Top-right
   model.node(5, (W, 0.0))        # Skewed support

   # Fixed support at node 1
   model.fix(1, (1, 1, 1))

   # Skewed support at node 5 using penalty method
   cos_theta = 0.8
   sin_theta = 0.6

   R = exp([0.0, 0.0, angle])
   ground_node = 100
   model.node(ground_node, (W, 0.0))
   model.fix(ground_node, (1, 1, 1))

   # Penalty stiffness (very large to approximate rigid constraint)
   k_penalty = 1.0e10 * kip / inch
   model.uniaxialMaterial('Elastic', 1001, k_penalty)

   # Normal direction for constraint (perpendicular to support)
   nx, ny = R[:2, 0]
   # Tangential direction (along support)
   tx, ty = cos_theta, sin_theta

   # Create zeroLength element with oriented local axes
   # The element constrains motion in the normal direction (dir=2, local y-axis)
   model.element('zeroLength', 1001, (ground_node, 5), 
                 mat=1001, 
                 dir=2,  # Constrain in local y-direction (normal to support)
                 orient=(nx, ny, 0.0, tx, ty, 0.0))

   # Frame section and elements
   model.material('ElasticIsotropic', 1, E, nu)
   model.section("ElasticFrame", 1, E=E, G=E/(2*(1+nu)), A=A, Iy=0, Iz=Iz, J=0)
   model.geomTransf("Linear", 1)

   model.element('PrismFrame', 1, (1, 2), section=1, transform=1)
   model.element('PrismFrame', 2, (2, 3), section=1, transform=1)
   model.element('PrismFrame', 3, (3, 4), section=1, transform=1)
   model.element('PrismFrame', 4, (4, 5), section=1, transform=1)

   # Load
   model.timeSeries('Constant', 1)
   model.pattern('Plain', 1, 1)
   model.load(3, (0.0, P, 0.0))

   # Analysis
   model.system('BandGeneral')
   model.numberer('RCM')
   model.constraints('Transformation')
   model.integrator('LoadControl', 1.0)
   model.algorithm('Newton')
   model.test('Energy', 1e-10, 10)
   model.analysis('Static')
   model.analyze(1)

.. note::

   The penalty stiffness should be chosen large enough to approximate a rigid constraint, but not so large that it causes numerical conditioning problems. A typical value is 1.0e10 times the characteristic stiffness of the structure. The orientation vectors define the local coordinate system of the zeroLength element, allowing the constraint to be applied in the desired direction (normal to the skewed support).

Code Developed by: |glf|
