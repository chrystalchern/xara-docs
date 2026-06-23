
.. _bbarQuad:

Q4/P0
^^^^^^^^^

This command is used to construct a four-node quadrilateral element, which uses a bilinear isoparametric interpolation, derived against a three field variational principle in :math:`\boldsymbol{u}-p-\vartheta`. 

.. tabs::

   .. tab:: Python

      .. py:method:: Model.element("Q4/P0", tag, nodes, section)
         :no-index:

         :param tag: integer tag identifying the element
         :param nodes: tuple of integer tags identifying the nodes that form the element
         :param section: tuple or int. If int, it is the tag of a previously defined :ref:`PlaneSection <PlaneSection>`. If tuple, it is a tuple of the form (``thick``, ``type``, ``material``) where 
           
             ===================================   ==============================================================================================================
             ``thick`` |float|                     element thickness
             ``type`` |str|                        string representing material behavior. The type parameter can be either ``"PlaneStrain"`` or ``"PlaneStress"``
             ``material`` |integer|                tag of an :ref:`nDMaterial`
             ===================================   ==============================================================================================================
   

   .. tab:: Tcl

      .. function:: element Q4/P0 $tag {*}$nodes $thick $mat

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	unique :ref:`Element` tag
         $iNode $jNode $kNode $lNode, |integer|,  "four nodes defining element boundaries, input in counter-clockwise order around the element."
         $thick, |float|, element thickness
         $matTag, |integer|, tag of nDMaterial


.. note::

   This element is ``PlainStrain`` only.


.. figure:: Q4.svg
   :align: center
   :figclass: align-center

   MixedQuad element node numbering

Alternative element names that map to this element include ``"bbarQuad"`` and ``"constantPressureVolumeQuad"``.

The valid :ref:`eleResponse` queries to this element are 

* ``"forces"``, 
* ``"stresses"`` and 
* ``"material $matNum matArg1 matArg2 ..."`` Where $matNum refers to the material object at the integration point corresponding to the node numbers in the isoparametric domain.


Theory 
------

With four nodes, the element is equivalent to the *Q1/P0* formulation (Simo, Taylor, Pister 1984), also referred to as the *mean dilation formulation* of Nagtegaal, Parks and Rice (1974). 

This formulation is suitable for nearly-incompressible response, but is not suitable for bending dominated problems.

See also FEAP `elmt11`


Examples
--------

.. ref-gallery::

   examples/plane/plane-0002


Code Developed by: **Edward Love, Sandia National Laboratories**

