.. _Truss:

Truss
^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.element("Truss", tag, nodes, section, density=0)
         :no-index:

         Create a truss element with tag *tag* between the nodes in *nodes* with
         cross-sectional area *section*.

         :param tag: The element tag.
         :param nodes: A tuple of two node tags.
         :param section: The cross-sectional area of the truss element.
         :param density: The mass density of the element.

   .. tab:: Tcl

      .. code:: tcl

         element truss $eleTag $iNode $jNode $A $matTag 
               < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >

      the other is to specify a *Section* identifier:

      .. code:: tcl

         element trussSection $eleTag $iNode $jNode $secTag
               < -rho $rho > < -cMass $cFlag > < -doRayleigh $rFlag >



* When constructed with a *UniaxialMaterial*, the truss element
  considers strain-rate effects, and is thus suitable for use as a damping
  element.

* The valid queries to a truss element when creating an ElementRecorder
  object are 

  * ``"axialForce"``, 
  * ``"forces"`` 
  * ``"localForce"``, 
  * ``"deformations"``, 
  * ``"material $args"`` 
  * ``"section $args"``



Examples
--------

Create a truss element with tag 1 added between nodes 1 and 2 with area 5.5 that uses material 1.
In the first two variants, a :ref:`Truss <TrussSection>` section is defined.

.. tabs::

  .. tab:: Python

     .. code-block:: Python

        import xara

        model = xara.Model(ndm=2, ndf=3)
        model.node(1, (0.0, 0.0))
        model.node(2, (1.0, 0.0))
        model.uniaxialMaterial("Elastic", 1, 29e3)
        model.section("Truss", 1, area=5.5, material=1)
        model.element("Truss", 1, (1, 2), section=1)


  .. tab:: OpenSees

     .. code-block:: Tcl

        uniaxialMaterial Elastic 1 29e3
        section Truss 1 -material 1 -area 5.5
        element Truss 1 1 2 -section 1;


  .. tab:: Tcl (legacy)

     .. code-block:: Tcl

        element Truss 1 1 2 5.5 1;

Code Developed by: |fmk|

