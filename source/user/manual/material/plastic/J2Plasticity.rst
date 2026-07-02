.. _J2Plasticity:

J2Plasticity
^^^^^^^^^^^^

.. figure:: figures/j2-mises.png
   :align: center
   :figclass: align-center
   :width: 50%

   Tension test of a coupon using the :math:`J_2` plasticity model from the `STAIRLab gallery <https://gallery.stairlab.io/examples/tension-coupon/>`__.


*J2Plasticity* is a multi dimensional material model that incorporates plasticity using the von Mises :math:`J_2` yield criterion, with nonlinear isotropic hardening.


.. tabs::

   .. tab:: Python

      .. py:method:: Model.nDMaterial("J2", tag, K, G, Fy, Fs, Hsat, Hiso)
         :no-index:

         :param |integer| tag: unique tag identifying material
         :param |float| K: Bulk modulus, :math:`\kappa` [1]_
         :param |float| G: Shear modulus, :math:`\mu` [1]_
         :param |float| Fy: Initial yield stress, :math:`F_y` [1]_
         :param |float| Fs: Saturation yield stress
         :param |float| Hsat: exponential hardening parameter
         :param |float| Hiso: linear isotropic hardening modulus
   
   .. tab:: OpenSees

      .. function:: nDMaterial J2Plasticity $tag $K $G $sig0 $sigInf $delta $Hiso <$eta>;

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         tag, |integer|, unique tag identifying material
         K, |float|,	   bulk modulus
         G, |float|,	   shear modulus
         sig0, |float|,	   initial yield stress
         sigInf, |float|,	   final saturation yield stress
         delta, |float|,	   exponential hardening parameter
         H, |float|,linear hardening parameter

.. [1] These arguments are supported by the :ref:`parameter <parameter>` commands.

Notes
-----

Parameters
""""""""""

* ``K`` - Bulk modulus :math:`\kappa`
* ``G`` - Shear modulus :math:`\mu`
* ``E`` - Young's modulus :math:`E`

  .. note::

     Updates to :math:`E` are performed at constant Poisson ratio :math:`\nu`.

* ``Fy`` - Initial yield stress :math:`F_y`

Examples
--------


.. code-block:: Tcl

   nDMaterial J2 [incr i] -E $E -G $G $Fy $Fs $Hsat $Hiso $eta
   nDMaterial J2 [incr i] -E $E -G $G $Fy $Fs $Hsat $Hiso $eta -density $density
   nDMaterial J2 [incr i] -E $E -nu $nu $Fy $Fs $Hsat $Hiso $eta -density $density



Theory 
------

In the elastic range, the material response follows an :ref:`ElasticIsotropic` formulation:

.. math::

   \boldsymbol{T} = K \operatorname{tr} \boldsymbol{E}_e + 2 G \operatorname{dev} \boldsymbol{E}_e

Plastic response is distinguished by the yield function :math:`f`

.. math::

   f (\boldsymbol{T},h) \triangleq \| \operatorname{dev} \boldsymbol{T} \| - \sqrt{\tfrac{2}{3}} \, h^{\mathrm{iso}}(\bar{\epsilon}_{\mathrm{p}})

where :math:`\bar{\epsilon}_{\mathrm{p}}` is the scalar *equivalent plastic tensile strain*, and :math:`h^{\mathrm{iso}}` is a scalar function that defines the *saturation isotropic hardening* given by:

.. math::
   
   h^{\mathrm{iso}}(\bar{\epsilon}_{\mathrm{p}}) = H_{\mathrm{iso}} \bar{\epsilon}_{\mathrm{p}} + F_{s}  + (F_y - F_{s}) \exp \left(-H_{\mathrm{s}} \bar{\epsilon}_{\mathrm{p}} \right)

.. note:: 
   This is identical to the hardening function for :ref:`DruckerPrager`, when :math:`F_y \equiv F_0`.

This hardening rule is equivalent to the model implemented by FEAP. 
The flow rules are

.. math::

   \dot{\boldsymbol{E}}_{\mathrm{p}} = \gamma  \frac{\partial f}{\partial \boldsymbol{T}}

..
   \dot{\bar{\epsilon}}_{\mathrm{p}} = - \gamma  \frac{\partial f}{\partial Y}

where :math:`\gamma` is the plastic consistency parameter and :math:`\boldsymbol{E}_{\mathrm{p}}` is the plastic strain tensor.
linear viscosity is exhibited with :math:`\gamma = \frac{\phi}{\eta}` ( if :math:`\phi > 0` )

Backward Euler integration is employed in the implementation.

.. note::

   * For linear isotropic hardening, set :math:`F_{\infty} = F_0`
   * For rate independent cases, set :math:`\eta = 0`.

References
----------

Code Developed by: **Ed Love**
