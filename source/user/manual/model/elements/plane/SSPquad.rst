.. _SSPquad:

Q4/SSP
^^^^^^^

This command is used to construct a SSPquad element. 
The SSPquad element is a four-node quadrilateral element using physically stabilized single-point (SSP) integration. 
The stabilization incorporates an assumed strain field in which the volumetric dilation and the shear strain associated with the the hourglass modes are zero, resulting in an element which is free from volumetric and shear locking. 
The elimination of shear locking results in greater coarse mesh accuracy in bending dominated problems, and the elimination of volumetric locking improves accuracy in nearly-incompressible problems. 
Analysis times are generally faster than corresponding full integration elements. 
The formulation for this element is identical to the solid phase portion of the ``SSPquadUP`` element as described by [McGannEtAl2012]_.


.. tabs::
   .. tab:: Python

      .. py:method:: Model.element("Q4/SSP", tag, nodes, section [, pressure, rho, b1, b2])
         :no-index:

         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param section: tuple or int. If int, it is the tag of a previously defined :ref:`PlaneSection <PlaneSection>`. If tuple, it is a tuple of the form (``thick``, ``type``, ``material``) where 
           
             ===================================   ==============================================================================================================
             ``thick`` |float|                     element thickness
             ``type`` |str|                        string representing material behavior. The type parameter can be either ``"PlaneStrain"`` or ``"PlaneStress"``
             ``material`` |integer|                tag of an :ref:`nDMaterial`
             ===================================   ==============================================================================================================
           
         :param pressure: |float|, surface pressure (optional, default = 0.0)
         :param rho: |float|, element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
         :param b1: |float|, constant body forces defined in the domain (optional, default=0.0)
         :param b2: |float|, constant body forces defined in the domain (optional, default=0.0)
   

   .. tab:: Tcl

      .. function:: element SSPquad $eleTag $iNode $jNode $kNode $lNode $matTag $type $thick <$b1 $b2>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, unique integer tag identifying element object
         $iNode $jNode $kNode $lNode, 4 |integer|, the four nodes defining the element input in counterclockwise order (``ndm=2`` and ``ndf=2``)
         $thick, |float|, thickness of the element in out-of-plane direction
         $type, |float|, string to relay material behavior to the element (either ``"PlaneStrain"`` or ``"PlaneStress"``)
         $matTag, |integer|,	unique integer tag associated with previously-defined nDMaterial object
         $b1 $b2, |float|, constant body forces in global :math:`x`- and :math:`y`-directions respectively (optional: default = 0.0)


.. figure:: Q4.svg
   :align: center
   :figclass: align-center

   Numbering of nodes for the SSPquad element


Valid :ref:`eleResponse` queries to the SSPquad element correspond to those for the nDMaterial object assigned to the element (e.g., ``"stress"``, ``"strain"``). 
Material response is recorded at the single integration point located in the center of the element.

The SSPquad element was designed with intentions of duplicating the functionality of the Quad Element. 
If an example is found where the SSPquad element cannot do something that works for the Quad Element, e.g., material updating, please contact the developers listed below so the bug can be fixed.

Elemental recorders for stress and strain when using the SSPquad element (note the difference from the Quad Element)

Examples
--------

SSPquad element definition with element tag 1, nodes 1, 2, 3, and 4, material tag 1, plane strain conditions, unit thickness, horizontal body force of zero, and vertical body force of -10.0

1. **Tcl Code**

   .. code-block:: tcl

      element SSPquad 1  1 2 3 4  1 "PlaneStrain" 1.0 0.0 -10.0
      recorder Element -eleRange 1 $numElem -time -file stress.out  stress
      recorder Element -eleRange 1 $numElem -time -file strain.out  strain

1. **Tcl Code**

   .. code-block:: python

      model.element("SSPquad", 1, (1, 2,  3,  4),   (1, 'PlaneStrain',  1.0),  0.0,  -10.0)


.. admonition:: Another Tcl Example 

   The input file shown below creates a cantilever beam subject to a parabolic shear stress distribution at the free end. The beam is modeled with only one element over the height to test the coarse-mesh accuracy of the designated quadrilateral element. Anti-symmetry conditions hold, only the top half of the beam is modeled.

   Try running this with the SSPquad element and the Quad Element. Compare the results to each other and to the beam solution to see shear locking in action. Volumetric locking in the Quad Element can be observed by increasing Poisson's ratio to 0.49.

   .. literalinclude:: SSPquadExample.tcl
      :language: tcl


Code Developed by: |chris|, |pedro|, |peter| at University of Washington.

.. [McGannEtAl2012] McGann, C. R., Arduino, P., and Mackenzie-Helnwein, P. (2012). “Stabilized single-point 4-node quadrilateral element for dynamic analysis of fluid saturated porous media.” Acta Geotechnica, 7(4), 297-311.

