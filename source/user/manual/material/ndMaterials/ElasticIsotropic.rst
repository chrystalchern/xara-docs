.. _ElasticIsotropic:

Elastic Isotropic
^^^^^^^^^^^^^^^^^

This command is used to construct an *ElasticIsotropic* material.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.material("ElasticIsotropic", tag, E, v, rho=0.0)
         :no-index:

         :param |integer| tag: integer tag identifying material
         :param |float| E: Young's elastic modulus :math:`E`
         :param |float| v: Poisson's ratio :math:`\nu`
         :param |float| rho: mass density :math:`\rho`. optional default = 0.0.

   .. tab:: OpenSees

      .. function:: nDMaterial ElasticIsotropic $tag $E $v <$rho>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	   unique tag identifying material
         $E, |float|,	   elastic Modulus
         $v, |float|,	   Poisson's ratio
         $rho, |float|, mass density. optional default = 0.0.


..
  The material formulations for the ElasticIsotropic object are "ThreeDimensional", "PlaneStrain," "Plane Stress," "AxiSymmetric," and "PlateFiber."


Theory
------

The formulation of the Elastic Isotropic material is often referred to as the *Saint Venant–Kirchhoff model*.
Any linear isotropic function can be expressed in terms of two parameters :math:`\lambda` and :math:`\mu` as follows :cite:p:`gurtin1981introduction`:

.. math::

   \boldsymbol{S} = \lambda \text{tr}(\boldsymbol{E}) \boldsymbol{1} + 2\mu \boldsymbol{E}

However, a more common representation of the model is in terms of the compression modulus :math:`K` and the shear modulus :math:`\mu`:

.. math::

   \boldsymbol{S} = K \text{tr}(\boldsymbol{E}) \boldsymbol{1} + 2\mu \operatorname{dev}\boldsymbol{E}

where :math:`\operatorname{dev}\boldsymbol{E}` is the deviatoric part of the strain tensor :math:`\boldsymbol{E}`.



Plane Sections
~~~~~~~~~~~~~~

When used in a :ref:`PlaneStrain` section, the constitutive relation becomes:

.. math::

   \frac{E}{(1+\nu)(1-2 \nu)}\left[\begin{array}{ccc}
   1-\nu & \nu & 0 \\
   \nu & 1-\nu & 0 \\
   0 & 0 & \frac{1-2 \nu}{2}
   \end{array}\right]

When used in a :ref:`PlaneStress` section, the constitutive relation becomes:

.. math::

   \left[\begin{array}{l}
   \sigma_{11} \\
   \sigma_{22} \\
   \sigma_{12}
   \end{array}\right]=\frac{E}{\left(1-\nu^2\right)}\left[\begin{array}{ccc}
   1 & \nu & 0 \\
   \nu & 1 & 0 \\
   0 & 0 & (1-\nu) / 2
   \end{array}\right]\left[\begin{array}{c}
   \varepsilon_{11} \\
   \varepsilon_{22} \\
   2 \varepsilon_{12}
   \end{array}\right]


Examples
--------


.. ref-gallery::
    :tooltip:

    gallery/plane-0002/main


References
----------

Code Developed by: |mhs|

