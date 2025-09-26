.. _element-two-node-link:

Link
^^^^^^

``Link`` connects two nodes with a set of uncoupled
uniaxial springs/dashpots acting along user-selected basic directions.
It supports 1D, 2D, and 3D kinematics and can include geometric
(P–Δ) effects, optional Rayleigh damping, and a lumped translational mass.

The element operates in three coordinate systems:

- **Global (g)** – the analysis coordinates at the nodes.
- **Local (l)** – the element’s orthonormal triad :math:`\{\mathbf{e}_x,\mathbf{e}_y,\mathbf{e}_z\}`.
- **Basic (b)** – the collection of scalar deformation modes that are each driven
  by a single uniaxial material.

Only diagonal coupling is used in the basic system: each basic mode is
assigned exactly one uniaxial material.

Formulation
===========

Let :math:`\mathbf{u}_g` be the global nodal DOF vector ordered as the DOF of
node *i* followed by the DOF of node *j*. 
The element forms the local
displacements

.. math::

   \mathbf{u}_l \;=\; \mathbf{T}_{gl}\,\mathbf{u}_g,

where :math:`\mathbf{T}_{gl}` is assembled from the 3×3 direction cosine matrix
``trans`` (defined below) according to the element dimensionality and the
per-node DOF layout.

The basic deformations :math:`\mathbf{u}_b` are linear combinations of
:math:`\mathbf{u}_l`:

.. math::

   \mathbf{u}_b \;=\; \mathbf{T}_{lb}\,\mathbf{u}_l,

with :math:`\mathbf{T}_{lb}` constructed as follows:

- For a basic direction with ID ``Type``, the relative displacement between the
  two nodes’ local DOF in that direction is taken with coefficients :math:`[-1,\,+1]`.
- For shear-type basic directions in formulations with rotations,
  additional terms proportional to the element length :math:`L` are included
  using the *shear distance ratios* ``shearDistI = [s_y, s_z]``
  (see *Shear distance ratios* below).

The same transformations are applied to velocities to obtain the basic velocities :math:`\dot{\mathbf{u}}_b`.

Local Orientation
------------------

Let :math:`\Delta \mathbf{x}` be the chord from node *i* to node *j* and
:math:`L=\lVert\Delta \mathbf{x}\rVert`. The user may provide vectors ``x`` and ``y``
to define the local axes. If not provided, the element sets:

- :math:`\mathbf{e}_x` parallel to :math:`\Delta \mathbf{x}` (or :math:`[1,0,0]` if :math:`L\le \varepsilon`),
- :math:`\mathbf{e}_y` perpendicular to :math:`\mathbf{e}_x` (default in 2D: rotate in-plane; in 3D, a warning is issued if no valid :math:`\mathbf{e}_y` is given).

Then

.. math::

   \mathbf{e}_z \;=\; \mathbf{e}_x\times\mathbf{e}_y, \qquad
   \mathbf{e}_y \;=\; \mathbf{e}_z\times\mathbf{e}_x,

and the 3×3 direction cosine matrix ``trans`` has rows
:math:`\hat{\mathbf{e}_x}^\top,\hat{\mathbf{e}_y}^\top,\hat{\mathbf{e}_z}^\top`.


You choose which basic modes are active by listing direction IDs in
``direction`` (1–6 entries allowed, depending on dimensionality). The IDs are:

- ``0``: axial (local :math:`x`)
- ``1``: shear along local :math:`y`
- ``2``: shear along local :math:`z`
- ``3``: torsion about local :math:`x`
- ``4``: bending about local :math:`y` (produces local :math:`M_y`)
- ``5``: bending about local :math:`z` (produces local :math:`M_z`)

Each active basic direction is assigned one uniaxial material. The basic
force vector :math:`\mathbf{q}_b` and diagonal basic tangent
:math:`\mathbf{K}_b=\mathrm{diag}(k_i)` are obtained from those materials via

.. math::

   q_{b,i} \leftarrow \sigma_i(u_{b,i}, \dot{u}_{b,i}), \qquad
   k_i \leftarrow \frac{\partial \sigma_i}{\partial u_{b,i}}, \qquad
   c_i \leftarrow \frac{\partial \sigma_i}{\partial \dot{u}_{b,i}}.



The element adapts to the problem dimension and the nodal DOF count:

- 1D with 1 DOF per node → :math:`\text{numDOF}=2`
- 2D with 2 DOF per node → :math:`\text{numDOF}=4`
- 2D with 3 DOF per node → :math:`\text{numDOF}=6`
- 3D with 3 DOF per node → :math:`\text{numDOF}=6`
- 3D with 6 DOF per node → :math:`\text{numDOF}=12`

Only direction IDs valid for the chosen configuration are accepted.


Internal forces
---------------

1) **Material (basic) forces.** From the uniaxial materials, :math:`\mathbf{q}_b`.

2) **Transform to local.**

   .. math::
   
      \mathbf{q}_l \;=\; \mathbf{T}_{lb}^\top\,\mathbf{q}_b

   .. math::

      \mathbf{K}_l \;=\; \mathbf{T}_{lb}^\top\,\mathbf{K}_b\,\mathbf{T}_{lb}.

3) **Add geometric (P–Δ) forces** if enabled, using the current axial force :math:`N` and transverse relative locals :math:`\Delta u_{l,y}`, :math:`\Delta u_{l,z}`. These terms depend on the current axial basic force :math:`N` and the relative local transverse displacements :math:`\Delta u_{l,y}` and :math:`\Delta u_{l,z}`:

   - Let
   
     .. math::
        \Delta u_{l,y} = u_l(y@j) - u_l(y@i), \qquad
        \Delta u_{l,z} = u_l(z@j) - u_l(z@i).
   
   - With element length :math:`L` and ratios ``Mratio``:
   
     - For in-plane shear directions, add :math:`(N/L)\,(1 - r_{y2} - r_{y3})` to the appropriate local shear-shear subblocks.
     - For bending directions, add terms :math:`\pm r\,N` coupling shear and bending DOF as specified below (*P–Δ formulas*).

4) **Transform to global.**

   .. math::
   
      \mathbf{p} \;=\; \mathbf{T}_{gl}^\top\,\mathbf{q}_l

   .. math::
   
      \mathbf{K}_g \;=\; \mathbf{T}_{gl}^\top\,\mathbf{K}_l\,\mathbf{T}_{gl}.




Geometric (P–Δ) options
-----------------------

P–Δ effects are included when a four-entry vector ``Mratio`` is given:

.. code-block:: text

   Mratio = [ r_y1, r_y2, r_z1, r_z2 ]

with constraints

.. math::

   r_{y1}, r_{y2}, r_{z1}, r_{z2} \ge 0, \qquad
   r_{y1}+r_{y2} \le 1, \qquad
   r_{z1}+r_{z2} \le 1.

These ratios distribute the geometric moments generated by axial force
and transverse sway to the element’s end rotations in the local system.

**P–Δ force contributions (local system).** Using :math:`N` (basic axial force):

- *2D, 2 dof/node (numDOF=4):* for local shear in :math:`y` (``Type=1``)
  add a shear pair

  .. math::
     V_{\Delta} = \frac{N}{L}\,(1-r_{z1}-r_{z2})\,\Delta u_{l,y},

  with opposite signs at the two ends’ shear DOF.

- *2D, 3 dof/node (numDOF=6):*
  - for local shear :math:`y` (``Type=1``): same :math:`V_{\Delta}` as above;
  - for bending about :math:`z` (``Type=2``): add end moments :math:`M_{\Delta} = N\,\Delta u_{l,y}` split as :math:`[+r_{z1} M_{\Delta},\; +r_{z2} M_{\Delta}]`.

- *3D, 3 dof/node (numDOF=6):*
  - for local shear :math:`y` (``Type=1``): as above with :math:`\Delta u_{l,y}`;
  - for local shear :math:`z` (``Type=2``): analogous with :math:`\Delta u_{l,z}` and :math:`(1-r_{y1}-r_{y2})`.

- *3D, 6 dof/node (numDOF=12):*
  - shear :math:`y` (``Type=1``) and shear :math:`z` (``Type=2``): same pattern as above but applied to the corresponding local DOF indices;
  - bending about :math:`y` (``Type=4``): add end moments :math:`[-\,r_{y1}\,N\,\Delta u_{l,z},\; -\,r_{y2}\,N\,\Delta u_{l,z}]`;
  - bending about :math:`z` (``Type=5``): add end moments :math:`[+\,r_{z1}\,N\,\Delta u_{l,y},\; +\,r_{z2}\,N\,\Delta u_{l,y}]`.

**P–Δ stiffness contributions (local system).** The linearization adds:

- shear–shear terms of the form
  :math:`(N/L)\,(1-r_{z1}-r_{z2})` or
  :math:`(N/L)\,(1-r_{y1}-r_{y2})` to the appropriate 2×2 subblocks; and
- shear–bending (and bending–shear) couplings proportional to :math:`\pm r\,N`
  in the 2D/3D cases that include rotations, with the same sign patterns as the
  force contributions listed above.

Shear distance ratios
---------------------

For formulations that include rotations, the basic shear deformations are
formed using the *shear distance ratios* ``shearDistI = [s_y, s_z]``
(only used where applicable):

- In 2D with rotations, for local shear :math:`y` (``Type=1``),

  .. math::
     u_{b}^{(1)} = \big(u_{l,y}@j - u_{l,y}@i\big)
                    - s_y\,L\,\theta_{l,z}@i
                    - (1-s_y)\,L\,\theta_{l,z}@j.

- In 3D with rotations,
  an analogous relation is used for the :math:`y`- and :math:`z`-shear modes,
  with :math:`s_y` or :math:`s_z` respectively.

Valid range is :math:`0 \le s_y, s_z \le 1`. If not provided, both default to 0.5.


Inertia
-------

If a positive scalar ``mass`` is provided, a **lumped translational mass**
is formed with :math:`m=\tfrac{1}{2}\,\text{mass}` applied to the
first ``numDIM`` translational DOF at each node in the global system.
Rotational DOF receive no element mass.

- **Element loads.** No distributed/thermal/etc. elemental loads are handled.
- **Inertia.** With nonzero ``mass``, the consistent unbalance from an input
  ground acceleration vector :math:`\mathbf{a}` is assembled using the lumped
  mass at the translational DOF.
- **Damping forces.** When Rayleigh damping is enabled and/or materials provide
  a damping tangent, the corresponding damping forces are included in
  ``resistingForceIncInertia``.


Damping
-------

The element damping matrix is the sum of:

- **Optional Rayleigh damping** inherited from the analysis (enabled when
  ``addRayleigh=1`` in this element).
- **Material damping** assembled from the uniaxial materials’ damping
  tangents: form :math:`\mathbf{C}_b=\mathrm{diag}(c_i)`, then

  .. math::

     \mathbf{C}_l = \mathbf{T}_{lb}^\top\,\mathbf{C}_b\,\mathbf{T}_{lb}, \qquad
     \mathbf{C}_g = \mathbf{T}_{gl}^\top\,\mathbf{C}_l\,\mathbf{T}_{gl}.


Response Quantities
===================

The element can report:

- **Global forces** :math:`\mathbf{p}`.
- **Local forces** :math:`\mathbf{q}_l` (including P–Δ if enabled).
- **Basic forces** :math:`\mathbf{q}_b`.
- **Local displacements** :math:`\mathbf{u}_l`.
- **Basic deformations** :math:`\mathbf{u}_b`.
- **Basic (deformation, force)** concatenated vector.
- **Material responses** for any basic direction (delegated to the
  associated uniaxial material).

Practical notes
===============

- Provide a valid local orientation; in 3D, :math:`\mathbf{e}_x` and
  :math:`\mathbf{e}_y` must not be parallel or zero-length.
- The number and types of nodal DOF must match at both nodes.
- Direction IDs must be valid for the chosen dimension/DOF layout.
- P–Δ effects are active only when a four-entry ``Mratio`` is supplied and the
  axial basic force is nonzero.
- The element’s own mass is translational only and lumped; set ``mass=0`` to
  omit it entirely.
