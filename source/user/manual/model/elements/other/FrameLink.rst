.. _element-two-node-link-section:

FrameLink
^^^^^^^^^

Synopsis
========

A ``FrameLink`` connects two nodes using a **section-level** constitutive law
through a single ``SectionForceDeformation``. The element works in 1D, 2D, and 3D, and 
supports optional geometric (:math:`P\!-\!\Delta`) effects.

.. py:method:: Model.element("FrameLink", tag, nodes, section, *, orient=None, pDelta=None, shearDist=None, doRayleigh=False, mass=0.0)
   :no-index:

   Create a two–node link element whose behavior is defined by a section formulation.

   :param tag: unique :ref:`element` tag
   :type tag: |integer|
   :param nodes: pair of integer node tags ``(iNode, jNode)`` (see :ref:`node`)
   :type nodes: tuple
   :param section: section tag (see :ref:`section`)
   :type section: |integer|
   :param orient: element orientation. Accepts either
                  ``(x1, x2, x3, y1, y2, y3)`` or a single 3-vector depending on model dimension:
                  
                  - In 1D/2D, a single 3-vector is treated as :math:`\mathbf{e}_x`.
                  - In 3D, a single 3-vector is treated as :math:`\mathbf{e}_y` while :math:`\mathbf{e}_x` defaults from node coordinates.

                  If omitted, :math:`\mathbf{e}_x = \Delta \mathbf{x}/L` and :math:`\mathbf{e}_y = (0,1,0)`.
   :type orient: tuple or list of |float|
   :param pDelta: P-Δ moment distribution ratios. In 3D supply four values; in 2D supply two values.
   :type pDelta: tuple or list of |float|
   :param shearDist: shear distance from node *i*. In 3D supply two values; in 2D supply one value
                     (the second defaults internally to ``0.5`` if not provided).
   :type shearDist: tuple or list of |float|
   :param doRayleigh: include Rayleigh damping contributions
   :type doRayleigh: |bool|
   :param mass: lumped element mass
   :type mass: |float|


Formulation
===========


Frames of reference
-------------------

- **Global** frame with orthonormal basis :math:`\{\mathbf{E}_x,\mathbf{E}_y,\mathbf{E}_z\}`.
- **Local** element triad :math:`\{\mathbf{e}_x,\mathbf{e}_y,\mathbf{e}_z\}`, where
  :math:`\mathbf{e}_x` is along the chord from node :math:`i` to node :math:`j`
  (unless overridden by the user), and :math:`\mathbf{e}_y,\mathbf{e}_z` complete
  a right-handed system.
- **Basic (section)** coordinates, where each component is one entry of the
  section deformation vector used by the section law.

Let :math:`\mathbf{u}^i, \mathbf{u}^j` be the **local** translational DOF vectors at the two
nodes, and :math:`\boldsymbol{\theta}^i, \boldsymbol{\theta}^j` the **local** rotational DOF vectors.
We will use scalar components such as :math:`\mathbf{u}^i\!\cdot\!\mathbf{e}_x`
and :math:`\boldsymbol{\theta}^j\!\cdot\!\mathbf{e}_z`.



The element builds a 3×3 direction-cosine matrix :math:`\mathbf{T}` with rows
:math:`\mathbf{e}_x^\top,\mathbf{e}_y^\top,\mathbf{e}_z^\top`.
From this it assembles:

- :math:`\mathbf{T}_{gl}`: global → local transformation on the element DOF.
- :math:`\mathbf{T}_{lb}`: local → basic (section) transformation that extracts relative measures for the section.

Kinematics
----------

For each section entry :math:`t_k`, the element forms the section strains :math:`\boldsymbol{e}` from nodal locals as follows.

Let :math:`L` be the current chord length and let the **shear-distance ratios**
be :math:`s_y, s_z \in [0,1]`.

- **Axial** (:math:`t_k=\mathrm{P}`):

  .. math::
     \Delta u_x \;=\; (\mathbf{u}^j-\mathbf{u}^i)\!\cdot\!\mathbf{e}_x, \qquad
     \varepsilon_x \;\equiv\; \frac{\Delta u_x}{L}.

  The basic component sent to the section is :math:`u_b^{(k)}=\varepsilon_x`.

- Shear in :math:`\mathbf{e}_y` direction (:math:`t_k=\mathrm{VY}`; cases with rotations):

  .. math::
     \gamma_y^\ast \;=\; (\mathbf{u}^j-\mathbf{u}^i)\!\cdot\!\mathbf{e}_y
                        \;-\; s_y\,L\,(\boldsymbol{\theta}^i\!\cdot\!\mathbf{e}_z)
                        \;-\; (1-s_y)\,L\,(\boldsymbol{\theta}^j\!\cdot\!\mathbf{e}_z),\\[2mm]
     \gamma_y \;\equiv\; \dfrac{\gamma_y^\ast}{L}.

  The basic component is :math:`u_b^{(k)}=\gamma_y`.

- **Shear in } \mathbf{e}_z \text{ direction** (3D only, :math:`t_k=\mathrm{VZ}`):

  .. math::
     \gamma_z^\ast \;=\; (\mathbf{u}^j-\mathbf{u}^i)\!\cdot\!\mathbf{e}_z
                        \;+\; s_z\,L\,(\boldsymbol{\theta}^i\!\cdot\!\mathbf{e}_y)
                        \;+\; (1-s_z)\,L\,(\boldsymbol{\theta}^j\!\cdot\!\mathbf{e}_y),\\[2mm]
     \gamma_z \;\equiv\; \dfrac{\gamma_z^\ast}{L},
  and :math:`u_b^{(k)}=\gamma_z`.

- **Torsion** (:math:`t_k=\mathrm{T}`):

  .. math::
     \phi_x \;=\; (\boldsymbol{\theta}^j-\boldsymbol{\theta}^i)\!\cdot\!\mathbf{e}_x,
  
  and :math:`u_b^{(k)}=\phi_x`  (no :math:`1/L` normalization).

- **Flexure** about :math:`\mathbf{e}_y`:

  .. math::
     \Delta \theta_y \;=\; (\boldsymbol{\theta}^j-\boldsymbol{\theta}^i)\!\cdot\!\mathbf{e}_y,
  and :math:`u_b^{(k)}=\Delta \theta_y`  (no :math:`1/L` normalization). About :math:`\mathbf{e}_z`:

  .. math::
     \Delta \theta_z \;=\; (\boldsymbol{\theta}^j-\boldsymbol{\theta}^i)\!\cdot\!\mathbf{e}_z,
  and :math:`u_b^{(k)}=\Delta \theta_z`  (no :math:`1/L` normalization).


.. admonition:: Ordering-sensitive normalization (important)
   :class: note

   This implementation **divides only the first two section components** of the
   basic vector by :math:`L` *before* sending them to the section, i.e.,
   :math:`u_b^{(0)}\leftarrow u_b^{(0)}/L` and
   :math:`u_b^{(1)}\leftarrow u_b^{(1)}/L`.

   Consistency therefore requires that the section’s own ordering places
   :math:`t_0=\mathrm{P}` and :math:`t_1=\mathrm{VY}`. If your section orders
   resultants differently (e.g., many 2D sections use
   :math:`[\mathrm{P},\mathrm{MZ},\mathrm{VY}]`), you must verify the behavior
   carefully; the element will still divide entries 0 and 1 regardless of their types.


Section law, forces, and tangent
--------------------------------

Given the strains :math:`\boldsymbol{e}` and their rate, the section provides

- **stress resultants** :math:`\boldsymbol{s} = \{N, V_y, V_z, T, M_y, M_z\}`,
- **section tangent** :math:`\mathbf{K}_s = \left[\partial s^{(k)}/\partial e^{(\ell)}\right]`.

The state determination proceeds as follows.

1. Apply the same **index-wise normalization** to the section tangent
   diagonal entries:

   .. math::
      (K_b)_{00} \leftarrow \frac{(K_b)_{00}}{L}, \qquad
      (K_b)_{11} \leftarrow \frac{(K_b)_{11}}{L}.

   No other entries are rescaled.

2. Form the **local** tangent and force via the kinematic transform:

   .. math::
      \mathbf{K}_l \;=\; \mathbf{T}_{lb}^\top\,\mathbf{K}_b\,\mathbf{T}_{lb}, \qquad
      \mathbf{q}_l \;=\; \mathbf{T}_{lb}^\top\,\boldsymbol{s}.

3. Add geometric (:math:`P\!-\!\Delta`) contributions in the local system
   (see next section).

4. Transforms to the **global** system:

   .. math::
      \mathbf{K}_g \;=\; \mathbf{T}_{gl}^\top\,\mathbf{K}_l\,\mathbf{T}_{gl}, \qquad
      \mathbf{p} \;=\; \mathbf{T}_{gl}^\top\,\mathbf{q}_l.

Geometric (:math:`P\!-\!\Delta`) effects
----------------------------------------

When a 4-entry vector of **moment-distribution ratios**
:math:`\mathbf{r}=[r_{y1}, r_{y2}, r_{z1}, r_{z2}]` is provided, geometric
forces and stiffness are added in the local system based on:

- the current **axial resultant** :math:`N` extracted from :math:`\boldsymbol{s}`,
- the transverse relative locals
  :math:`\Delta u_y=(\mathbf{u}^j-\mathbf{u}^i)\!\cdot\!\mathbf{e}_y` and
  :math:`\Delta u_z=(\mathbf{u}^j-\mathbf{u}^i)\!\cdot\!\mathbf{e}_z`,
- the chord length :math:`L`.

The contributions match the standard two-node link formulas:

- **Forces (local)**:
  shear pairs :math:`V_\Delta = (N/L)\,(1-r_{z1}-r_{z2})\,\Delta u_y` in the
  :math:`\mathbf{e}_y` direction and similarly in :math:`\mathbf{e}_z`,
  plus end moments split by :math:`r_{\bullet}`.

- **Stiffness (local)**:
  shear–shear terms of magnitude :math:`(N/L)\,(1-r_{\bullet 1}-r_{\bullet 2})`
  and shear–bending couplings proportional to :math:`\pm r_{\bullet}\,N`.

(Exact index placements follow the element’s DOF layout in 2D/3D; the formulas
are identical to those of ``TwoNodeLink``.)

Parameters and constraints
--------------------------

- **Shear-distance ratios**: :math:`s_y,s_z\in[0,1]`. Defaults are
  :math:`s_y=s_z=0.5` when not specified.
- **Moment-distribution ratios**: :math:`r_{\bullet}\ge 0` with
  :math:`r_{y1}+r_{y2}\le 1` and :math:`r_{z1}+r_{z2}\le 1`.
- **Mass**: translational lumped mass only; :math:`m/2` is placed on the first
  :math:`\text{numDIM}` translational DOF at each node in the global frame.

Damping and inertia
-------------------

- **Rayleigh damping** is included if enabled for the element.
- **Material (section) damping** is not assembled here; only Rayleigh
  contributes.
- **Inertia** enters through the lumped translational mass and nodal
  accelerations (global frame).

Mapping between section resultants and local DOF
------------------------------------------------

The element maps each section type to a *local* DOF index used in
:math:`\mathbf{T}_{lb}`. This mapping depends on dimension:

- **2D (3 dof/node)**

  - :math:`\mathrm{P}\rightarrow 0` (axial, :math:`\mathbf{e}_x`)
  - :math:`\mathrm{VY}\rightarrow 1` (shear along :math:`\mathbf{e}_y`)
  - :math:`\mathrm{MZ}\rightarrow 2` (bending about :math:`\mathbf{e}_z`)

- **3D (6 dof/node)**

  - :math:`\mathrm{P}\rightarrow 0`, :math:`\mathrm{VY}\rightarrow 1`,
    :math:`\mathrm{VZ}\rightarrow 2`, :math:`\mathrm{T}\rightarrow 3`,
    :math:`\mathrm{MY}\rightarrow 4`, :math:`\mathrm{MZ}\rightarrow 5`

This mapping determines which translational difference and which end-rotation
differences appear in each :math:`u_b^{(k)}` via :math:`\mathbf{T}_{lb}`.

Outut
=====

- **Global forces** :math:`\mathbf{p}`.
- **Local forces** :math:`\mathbf{q}_l` (including :math:`P\!-\!\Delta` if active).
- **Basic (section) resultants** :math:`\boldsymbol{s}`.
- **Local displacements** :math:`\mathbf{u}_l`.
- **Basic (section) deformations** :math:`\boldsymbol{e}` (in the section’s own ordering).
- **Concatenated** :math:`[\boldsymbol{e};\,\boldsymbol{s}]`.
- **Section-level outputs**: whatever the underlying section supports.

Notes
=====

- Provide a valid local orientation; :math:`\mathbf{e}_x` and
  :math:`\mathbf{e}_y` must not be parallel and must be nonzero.
- The two nodes must have matching DOF patterns.
- :math:`P\!-\!\Delta` contributions require a nonzero axial resultant and the
  4-entry ratio vector.
- **Ordering caveat**: the element **divides entries 0 and 1** of
  :math:`\boldsymbol{e}` by :math:`L` and scales the **(0,0)** and **(1,1)**
  entries of :math:`\mathbf{K}_b` by :math:`1/L`. Ensure your section’s ordering
  matches the intended interpretation (typically :math:`[\mathrm{P},\mathrm{VY},\dots]`)
  or verify with a small test before production runs.
