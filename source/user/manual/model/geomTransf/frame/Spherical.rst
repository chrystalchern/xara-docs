
Spherical
^^^^^^^^^

A *Spherical* transformation is used to enforce strain objectivity in the geometrically exact frame element (:ref:`ExactFrame`).



Theory
------


.. note::

   For two nodes, the procedure implements spherical linear interpolation (SLERP):
   
   .. math::
   
      \operatorname{SLERP}\left(\boldsymbol{\Lambda}_I, \boldsymbol{\Lambda}_J, \xi\right)=\boldsymbol{\Lambda}_I \exp \left(\frac{\xi}{L} \log \left(\boldsymbol{\Lambda}_I^\mathrm{t} \boldsymbol{\Lambda}_J\right)\right)
   
   The SLERP construction is a geodesic on :math:`\mathrm{SO}(3)`, i.e. a
   walk along the shortest path, on the manifold, between the two
   rotations.

The procedure begins by selecting two node indices :math:`I` and
:math:`J` for an :math:`n`-noded element as follows:

.. math::


   I=\operatorname{floor}\left(\frac{1}{2}(n+1)\right)  \quad \text { and } \quad  J=\operatorname{floor}\left(\frac{1}{2}(n+2)\right).

An intermediate vector
:math:`\mathbf{t} = \operatorname{Log}\boldsymbol{\Lambda}_I^{\mathrm{t}} \boldsymbol{\Lambda}_J`
is formed, and the coordinate rotation is given by:

.. math::


   \left.\begin{array}{rl}
   \boldsymbol{R} &= \boldsymbol{\Lambda}_I \operatorname{Exp} \left(\frac{1}{2} \mathbf{t}\right). \\
   \end{array}\right.

