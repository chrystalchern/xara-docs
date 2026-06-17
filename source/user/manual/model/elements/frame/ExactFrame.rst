
.. _ExactFrame:

``ExactFrame``
^^^^^^^^^^^^^^

.. figure:: ExactFrame_Fig1.png
	:align: center
	:figclass: align-center
	:scale: 55

	Fig. 1: Torsional instability captured by the **ExactFrame** formulation and rendered with `veux <https://veux.io>`__.


The **ExactFrame** element is a geometrically exact [4]_ beam element based on Simo's
parameterization [1]_ of Antman's *Special Cosserat Rod* [2]_. 
This element is formulated without any geometric simplifications, and consequently,
is capable of modeling highly nonlinear geometric phenomena with extreme accuracy.
The implementation closely follows the treatment by Perez and Filippou (2024) [3]_. 


.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.element("ExactFrame", tag, nodes, section, transform)
         :no-index:

         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of integer node tags (see :ref:`node`)
         :type nodes: tuple 
         :param section: Section object to be created at the element Gauss points. 
         :type section: :py:class:`xara.Section`
         :param transform: identifier for previously-defined coordinate-transformation (see :ref:`geomTransf`)
         :type transform: |integer|

   .. tab:: Tcl

      .. function:: element ExactFrame $tag $iNode $jNode $sect $tran

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``tag``, |integer|,	       unique :ref:`Element` tag
         ``iNode`` ``jNode`` , |integer|,  end nodes
         ``sect``, |integer|,         section tag
         ``tran``, |integer|,      identifier for previously-defined coordinate-transformation



The valid :ref:`eleResponse` queries to this element are ``"force"``.

Geometrically exact elements often exhibit undesirable features. These are rectified
as follows:

* **Path Dependence** The geometrically exact Cosserat rod theory is posed over a
  non-vectorial configuration space, and consequently may exhibit minor 
  path-dependence.
* **Rotation parameters** for post-processing purposes, rotations should be obtained using the :ref:`nodeRotation`. Recall that in a finite rotation analysis, "rotational" components of the nodal displacement vector (ie, the vector returned by :ref:`nodeDisp`) is meaningless.

The ``ExactFrame`` formulation is appropriate for a wide variety of structural members including thin-walled sections, asymmetric sections, and inelasticity.

As of ``xara`` version ``0.1.15``, the ``ExactFrame`` element can be used to model cross-sectional warping through an additional seventh degree of freedom.


.. note::

   This element always employs a :ref:`Gauss-Legendre <Legendre-BeamIntegration>` quadrature of order ``nen-1`` for an element with ``nen`` nodes, and does not accept user-defined quadrature schemes.


Example 
-------

The following example demonstrates the command to create an **ExactFrame** element.

.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.element('ExactFrame', 1, (1, 2), section=1, transform=1)

   .. tab:: OpenSees (Tcl)

      .. code-block:: tcl

         element ExactFrame 1 1 2 -section 1 -transform 1




References
----------

.. [1] Simo, J.C. (1985) ‘A finite strain beam formulation. The three-dimensional dynamic problem. Part I’, Computer Methods in Applied Mechanics and Engineering, 49(1), pp. 55–70. Available at: https://doi.org/10.1016/0045-7825(85)90050-7.

.. [2] Antman, S.S. (2005) Nonlinear problems of elasticity. 2nd ed. New York: Springer (Applied mathematical sciences, v. 107).

.. [3] Perez, C.M. and Filippou, F.C. (2024) ‘On nonlinear geometric transformations of finite elements’, International Journal for Numerical Methods in Engineering, p. e7506. Available at: https://doi.org/10.1002/nme.7506.

.. [4]  "geometrically exact" in this context refers to a specific class of formulations that are highly accurate in capturing geometric nonlinearities associated with large deformations and rotations, as seen in beam and shell theories. They are still approximations, but they aim for greater fidelity to the underlying physical theory by considering all relevant geometric terms without simplification. 

Code developed by: |cmp|

