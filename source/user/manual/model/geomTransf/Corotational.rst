.. _CorotTR:

Corotational
^^^^^^^^^^^^


.. deprecated:: 0.0.8

   This formulation is made obsolete by the new :ref:`Corotational02 <CorotTR02>` formulation. 
   ``Corotational02`` corrects several bugs in the original ``Corotational`` formulation. 
   The original ``Corotational`` transformation will continue 
   to be supported to ensure prior investigations remain reproducible, but all new analyses should use the new :ref:`Corotational02 <CorotTR02>` formulation.



The corotational coordinate transformation performs a geometric transformation from a *basic* system [1]_ to the global coordinate system. [2]_

.. tabs::

   .. tab:: Python

      .. py:method:: Model.geomTransf("Corotational", tag, vecxz, [offi, offj])
         :no-index:

         Define a corotational geometric transformation for frame elements.

         :param integer tag: integer tag identifying transformation
         :type tag: |integer|
         :param vecxz: X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system, **required in 3D**. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         :type vecxz: tuple of floats
         :param offi: joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model).
         :type offi: tuple of floats
         :param offj: joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model).
         :type offj: tuple of floats

   .. tab:: Tcl
   
      .. function:: geomTransf Corotational $transfTag < $vecxzX $vecxzY $vecxzZ > <-jntOffset $dXi $dYi $dZi $dXj $dYj $dZj>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $transfTag, |integer|, integer tag identifying transformation
         $vecxzX $vecxzY $vecxzZ,  |float|,  "X, Y, and Z components of vecxz, the vector used to define the local x-z plane of the local-coordinate system. The local y-axis is defined by taking the cross product of the vecxz vector and the x-axis.
         
         These components are specified in the global-coordinate system X,Y,Z and define a vector that is in a plane parallel to the x-z plane of the local-coordinate system.
         
         These items need to be specified for the three-dimensional problem."
         $dXi $dYi $dZi, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node i (optional, the number of arguments depends on the dimensions of the current model)."
         $dXj $dYj $dZj, |float|, "joint offset values -- offsets specified with respect to the global coordinate system for element-end node j (optional, the number of arguments depends on the dimensions of the current model)."


.. note::
	
   The element coordinate system and joint offsets are the same as that documented for the :ref:`Linear <linearTR>` transformation.


Examples
--------

This example is developed in detail on the examples `site <https://gallery.stairlab.io/examples/framevecxz/>`__.
In order to cover a wide range of cases, the strong axis of the first column, element `1`, 
is oriented so as to resist bending *outside* the plane of the portal, but the strong axis of the second column, element `3`, will resist bending *inside* the portal plane.

.. figure:: figures/vecxz.png
   :align: center
   :width: 50%

   A portal frame with :math:`X_3` vertical.


.. code-block:: Python

   model.node(1, (    0, 0,      0))
   model.node(2, (width, 0,      0))
   model.node(3, (width, 0, height))
   model.node(4, (    0, 0, height))

   model.geomTransf("Corotational", 1, (1, 0, 0)) # Column
   model.geomTransf("Corotational", 2, (0, 0, 1)) # Girder
   model.geomTransf("Corotational", 3, (0,-1, 0)) # Column



Theory
------

.. _corot-directors:

.. figure:: figures/directors.png
   :align: center
   :figclass: align-center

   Corotational transformation of a two-node frame.

The undeformed cross sections of a beam can be represented by a stationary field of 
three *reference* directors :math:`\mathbf{D}_k` that are orthonormal everywhere 
in :math:`\mathcal{B}`. 
As the beam deforms, these directors are transformed into the *deformed* directors :math:`\mathbf{d}_k`

Under a corotational transformation, an element's *state determination* is performed
in a transformed configuration space represented by director fields
:math:`\left\{\bar{\mathbf{d}}_k\right\}`, and
:math:`\left\{\bar{\mathbf{D}}_k\right\}` with the expressions:

.. math::

   \left.\begin{aligned}
   \mathbf{d}_k &\triangleq \boldsymbol{\Lambda}\mathbf{D}_k \\
   \bar{\mathbf{d}}_k &\triangleq \boldsymbol{R}\mathbf{D}_k \\
   \bar{\mathbf{D}}_k &\triangleq \bar{\boldsymbol{\Lambda}}\mathbf{D}_k \\
   \end{aligned}\right.,
   \quad\text{ implying }\qquad 
   \begin{aligned}
   \boldsymbol{\Lambda} &= \mathbf{d}_k\otimes\mathbf{D}_k \\
   \boldsymbol{R}       &= \bar{\mathbf{d}}_k\otimes\mathbf{D}_k \\
   \bar{\boldsymbol{\Lambda}} &= \bar{\mathbf{D}}_k\otimes\mathbf{D}_k \\
   \end{aligned}

.. note::
   It is more appropriate to think of the corotational transformation as a *family* of transformations.

Figure :numref:`corot-directors` illustrates this for an example embedding where a
single representative director from each of these fields, say
:math:`k=1`, is shown and :math:`\mathbf{D}_1` is taken to be aligned
with the reference configuration of an initially straight plane frame
(note that the subscript 1 will be dropped for clarity). Because
:math:`\mathbf{D}` was taken in a straight line for this example and
:math:`\boldsymbol{R}` is necessarily homogeneous, it follows from @eq:directors
that :math:`\bar{\mathbf{d}}` traces a similar straight line. It is also
useful to observe that @eq:tether implies the following alternative
representation for :math:`\boldsymbol{R}`, and :math:`\bar{\boldsymbol{\Lambda}}` which
is also apparent from the figure above:

.. math::


   \begin{aligned}
   \boldsymbol{R} &= \boldsymbol{\Lambda}\bar{\boldsymbol{\Lambda}}^{\mathrm{t}} \\
   &= (\mathbf{d}_k\otimes\mathbf{D}_k)(\mathbf{D}_k\otimes \bar{\mathbf{D}}_k) \\
   &= \mathbf{d}_k \otimes \bar{\mathbf{D}}_k
   \end{aligned}
   \quad\text{ and }\quad
   \begin{aligned}
   \bar{\boldsymbol{\Lambda}} 
   &= \boldsymbol{R}^{\mathrm{t}}\boldsymbol{\Lambda} \\
   &=\left(\mathbf{D}_k\otimes \bar{\mathbf{d}}_k\right)\left(\mathbf{d}_\ell\otimes\mathbf{D}_\ell\right) \\
   &= (\bar{\mathbf{d}}_k\cdot \mathbf{d}_\ell) \, \mathbf{D}_k \otimes \mathbf{D}_\ell
   \end{aligned}


where we use the identities
:math:`\left(\boldsymbol{a}\otimes\boldsymbol{b}\right)\left(\boldsymbol{c}\otimes\boldsymbol{d}\right) = \boldsymbol{b}\cdot\boldsymbol{c}\, \left(\boldsymbol{a}\otimes\boldsymbol{d}\right)`
and :math:`(\boldsymbol{a}\otimes\boldsymbol{b})^{\mathrm{t}} = \boldsymbol{b}\otimes\boldsymbol{a}` and
summation is again implied.

If a finite element implements an ideal strain measure that is exactly objective, then such 
a transformation will by definition be unobservable in the analysis results. 
However, due to the complexity 
in the configuration manifold of beams, such a strain measure is almost never used, and consequenty
the effect of the corotational transformation is *very* apparent.

.. math::


   \begin{aligned}
   \boldsymbol{\omega}_R &= \delta \bar{\mathbf{d}} \otimes \bar{\mathbf{d}} \\
   \boldsymbol{\omega} &= \delta \mathbf{d} \otimes \mathbf{d} \\
   \bar{\boldsymbol{\omega}} &= \delta \bar{\mathbf{D}} \otimes \bar{\mathbf{D}}
   \end{aligned}


References
----------

.. [1] Perez, Claudio M., and Filip C. Filippou. “On Nonlinear Geometric Transformations of Finite Elements.” International Journal for Numerical Methods in Engineering 125, no. 17 (September 15, 2024): e7506. https://doi.org/10.1002/nme.7506.

.. [2] De Souza, R. M. "Force-based finite element for large displacement inelastic analysis of frames" University of California, Berkeley (2000)

Code Developed by: |rms|, |cmp|

