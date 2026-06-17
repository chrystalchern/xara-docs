.. _node:

Node
====

This method is used to construct a ``Node`` which stores information about coordinates and mass at a single point.
The assignment of mass is optional.
Each node has :py:attr:`Model.ndm` coordinates (position in space) and :py:attr:`Model.ndf` degrees of freedom (displacement and, in 2D/3D frame models, rotation).


.. py:currentmodule:: xara

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.node(tag, coords, [mass])

         :param tag: integer tag identifying node
         :param coords: tuple of :py:attr:`Model.ndm` |float| coordinates
         :param mass: tuple of :py:attr:`Model.ndf` lumped mass values per DOF (see Theory for units and interpretation)


   .. tab:: Tcl 

      .. function:: node $tag [ndm $coords] <-mass [ndf $mass]>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, unique tag identifying node
         $coords,  |listFloat|,  **ndm** nodal coordinates
         $mass, |listFloat|, optional **ndf** lumped mass values per DOF (see Theory for units)


Theory
------

Nodes define the spatial discretization of the model: they carry coordinates (in the global system) and optional lumped mass.
The number of coordinates is **ndm** (number of dimensions); the number of degrees of freedom per node is **ndf** (typically ndm for trusses, ndm + rotational DOFs for frames).
See :ref:`nodeDisp` for the ordering of displacement components (u1, u2, u3, r1, r2, r3 in 3D).

**Units.** xara does not assume or enforce any unit system.
All numeric inputs (coordinates, mass, forces, etc.) are unitless; the user must choose and maintain a consistent unit system throughout the model.
See :ref:`units` for predefined constants and supported systems.

**Mass.** When the ``mass`` argument is provided, it is a tuple of **ndf** values: lumped mass (or rotational inertia) per degree of freedom, in the mass units of the chosen system (e.g. kg in SI, slug in fps).
For a 2D model with ndf=3, the first two values are translational mass for u1 and u2; the third is rotational inertia for r3.
A value of zero means no mass or inertia for that DOF.

Example
-------

The following example adds two nodes to a :class:`Model` with ``ndm=2`` and ``ndf=3``.
Node ``3`` is at coordinates (168.0, 0.0), node ``4`` at (168.0, 144.0).
Node ``4`` is assigned lumped mass ``(10.0, 10.0, 0.0)``: 10.0 for translational DOFs 1 and 2, and 0.0 for rotational DOF 3.
Units are those of the user's chosen system (e.g. kg in SI); see :ref:`units`.



.. tabs::

   .. tab:: Python

      .. code-block:: python

         model.node(3, (168.0, 0.0))
         model.node(4, (168.0, 144.0), mass=(10.0, 10.0, 0.0))

   .. tab:: Tcl

      .. code-block:: tcl

         node 3 168.0 0.0
         node 4 168.0 144.0 -mass 10.0 10.0 0.0


Code Developed by: |fmk|
