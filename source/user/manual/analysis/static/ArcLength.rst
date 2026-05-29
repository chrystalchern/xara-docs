.. _ArcLengthControl:

Arc-Length Control
^^^^^^^^^^^^^^^^^^

The *ArcLength* static integrator is particularly useful for tracing the response of a structure across limit points, where the solution may exhibit snap-through or snap-back behavior [2]_.

.. tabs::
   
   .. tab:: Python 
      
      .. py:method:: Model.integrator("ArcLength", s, alpha, det=False, exp=0.0, iterScale=1.0)
         :no-index:

         :param |float| s: the initial arc-Length
         :param |float| alpha:  a scaling factor on the reference loads.
         :param bool det:  if True, use the determinant to choose incrementation sign [1]_.
         :param float exp: exponent parameter from [1]_
         :param iterScale: |float|, a scaling factor on the arc-length incrementation.

   .. tab::Tcl

      .. function:: integrator ArcLength $s $alpha < -det > < -exp $exp > < -iterScale $iterScale >

      .. list-table:: 
        :widths: 10 10 40

        * - Argument
          - Type
          - Description
        * - ``$s``
          - |float|
          - the arcLength
        * - ``$alpha``
          - |float|
          - a scaling factor on the reference loads. 
        * - ``-det``
          - Flag
          - use the determinant to choose incrementation sign.
        * - ``$exp``
          - |float|
        * - ``$iterScale``
          - |float|
          - a scaling factor on the arc-length incrementation. 


Examples
--------

The following snippets demonstrate the syntax for configuring the ArcLength integrator.
A complete example that reproduces the work presented in [1]_ is available `here <https://gallery.stairlab.io/examples/archstaticsnap/>`_.

.. code-block:: python

   import sees.openseespy as ops
   model = ops.Model(ndm=2, ndf=3)

   ...

   model.integrator("ArcLength", 1, det=True, exp=0.5)


.. code-block:: tcl

   integrator ArcLength 1 -det -exp 0.5

.. code-block:: tcl

   integrator ArcLength 1 -exp 0.5

Theory
------

The arc-length control method is a continuation method that appends the following constraint equation to the 
static residual given in :ref:`Static <StaticAnalysis>`:

.. math::


   \Delta \boldsymbol{u}_{i+1} \cdot \Delta \boldsymbol{u}_{i+1} + \alpha^2 \Delta \lambda_{i+1}^2
   = \Delta s^2

where

.. math::


   \begin{aligned}
   \Delta \boldsymbol{u}_{i+1}=\sum_{j=1}^i d \boldsymbol{u}_{(j)}
   =\Delta \boldsymbol{u}_{(i)} + d \boldsymbol{u} \\
   \Delta \lambda_{i+1}
   =\sum_{j=1}^i d \lambda_{(j)}=\Delta \lambda_{(i)} + d \lambda
   \end{aligned}

Recall the linearized static residual

.. math::


   \boldsymbol{K} d \boldsymbol{u} = d \lambda \, \boldsymbol{p}_{\mathrm{ref}} +
   \lambda_{(i)} \boldsymbol{p}_{\mathrm{ref}} - \boldsymbol{p}_{\sigma}(u_{(i)}) = d \lambda \, \boldsymbol{p}_{\mathrm{ref}} + g_{(i)}

and define :math:`d\hat{\boldsymbol{u}}` and :math:`d\bar{\boldsymbol{u}}` by

.. math::


   d \hat{\boldsymbol{u}} \triangleq \boldsymbol{K}^{-1}_{(i)}\boldsymbol{p}_{\mathrm{ref}}
   \qquad\text{ and }\qquad
   d \bar{\boldsymbol{u}} \triangleq \boldsymbol{K}^{-1}_{(i)} \boldsymbol{g}_{(i)}

so that

.. math::


   d \boldsymbol{u} = d \lambda \, d \hat{\boldsymbol{u}} + d \bar{\boldsymbol{u}}

Implementation
--------------

The arc-length control method is implemented with a distinct *increment* and *iteration* phase.

Increment
~~~~~~~~~

During load incrementation the iteration is :math:`i=1` and the following assumption is taken:

.. math::

   d \boldsymbol{u}_{(1)} = d \lambda_{(1)} \, d \hat{\boldsymbol{u}}_{(1)} + \boldsymbol{0}

Thus the constraint equation simplifies to

.. math::


   d \lambda_{(1)} = \pm \sqrt{\frac{\Delta s^2}{d\hat{\boldsymbol{u}} \cdot d\hat{\boldsymbol{u}} + \alpha^2}}

where :math:`d \lambda` from the previous time :math:`(n-1)` is used to
determine the sign; if it was positive then the new
:math:`d \lambda_{(1)}` is assumed positive, otherwise negative.

Iterations
~~~~~~~~~~

During iterations (ie :math:`i>1`) the constraint equation is expressed in terms of the linearization direction :math:`d\boldsymbol{u}`:

.. math::


   \left( \Delta \boldsymbol{u}_{(i)} + d\boldsymbol{u} \right) \cdot \left( \Delta \boldsymbol{u}_{(i)} +
   d \boldsymbol{u} \right)
   + \alpha^2 \left( \Delta \lambda_{(i)} + d\lambda
   \right)^2 = \Delta s^2

which expands to

.. math::


   \Delta u_{(i)} \cdot \Delta u_{(i)} + 2 \,d \boldsymbol{u} \cdot \Delta \boldsymbol{u}_{(i)} + d u \cdot du
   + \alpha^2 \, d {\lambda_{(i)}}^2
   + 2 \alpha^2 d\lambda \, \Delta \lambda_{(i)}
   + \alpha^2 \, \Delta \lambda^2_{(i)}
   = \Delta s^2

assuming the constraint equation was solved at :math:`i-1` then one has
:math:`\Delta \boldsymbol{u}_{(i)} \cdot \Delta \boldsymbol{u}_{(i)} + \alpha^2 \Delta \lambda^2_{(i)} = \Delta s^2`,
and the constraint for the current iteration simplifies to

.. math::


   d \boldsymbol{u} \cdot d \boldsymbol{u} + 2\, d\boldsymbol{u} \cdot \Delta \boldsymbol{u}_{(i)} +
   \alpha^2 d \lambda^2
   + 2 \alpha^2 d\lambda \, \Delta \lambda_{(i)}
   = 0

Substituting the decomposed representation for :math:`d \boldsymbol{u}`
this furnishes a quadratic equation in :math:`d \lambda`:

.. math::


     a \, d \lambda^2 +
   2 b \, d \lambda
   + c =0

where we have defined the scalar constants

.. math::


   \begin{aligned}
   a &\triangleq d\hat{\boldsymbol{u}} \cdot d\hat{\boldsymbol{u}} + \alpha^2 \\
   b &\triangleq d \hat{\boldsymbol{u}} \cdot \left( \Delta\boldsymbol{u}_{(i)} + d \bar{\boldsymbol{u}}\right) + \alpha^2 \Delta \lambda_{(i)} \\
   c &\triangleq d \bar{\boldsymbol{u}} \cdot d \bar{\boldsymbol{u}} + \Delta \boldsymbol{u}_{(i)} \cdot d \bar{\boldsymbol{u}}
   \end{aligned}

which can be solved for two roots. The root chosen is the one which will
keep a positive angle between the incremental displacement before and
after this step.


References
----------

.. [1] Clarke, M.J. and Hancock, G.J. (1990) ‘A study of incremental‐iterative strategies for non‐linear analyses’, International Journal for Numerical Methods in Engineering, 29(7), pp. 1365–1391. Available at: https://doi.org/10.1002/nme.1620290702 .
.. [2] Riks E, 'An incremental approach to the solution of snapping and buckling problems', Int. J. Solids Struct. (1979)

* Wempner, GA (1971) 'Discrete approximations related to nonlinear theories of solids'
* Crisfield, MA (1981) 'A fast incremental/iterative solution procedure that handles "snap-through"'
* Ramm E 'Strategies for tracing nonlinear response near limit points'
