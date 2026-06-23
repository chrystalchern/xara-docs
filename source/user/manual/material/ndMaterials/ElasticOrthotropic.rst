.. _ElasticOrthotropic:

Elastic Orthotropic
^^^^^^^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:class:: xara.MultiaxialMaterial("ElasticOrthotropic", Ex, Ey, Ez, vxy, vyz, vzx, Gxy, Gyz, Gzx, rho=0.0)
         :no-index:

         :param |float| Ex: elastic modulus in x direction
         :param |float| Ey: elastic modulus in y direction
         :param |float| Ez: elastic modulus in z direction
         :param |float| vxy: Poisson's ratio in xy plane
         :param |float| vyz: Poisson's ratio in yz plane
         :param |float| vzx: Poisson's ratio in zx plane
         :param |float| Gxy: shear modulus in xy plane
         :param |float| Gyz: shear modulus in yz plane
         :param |float| Gzx: shear modulus in zx plane
         :param |float| rho: mass density. optional default = 0.0


   .. tab:: OpenSees

      .. function:: nDMaterial ElasticOrthotropic $matTag $Ex $Ey $Ez $vxy $vyz $vzx $Gxy $Gyz $Gzx <$rho>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $matTag, |integer|, unique tag identifying material
         $Ex $Ey $Ez, 3 |float|, elastic moduli in three mutually perpendicular directions
         $vxy $vyz $vzx, 3 |float|, Poisson's ratios
         $Gxy $Gyz $Gzx, 3 |float|, shear moduli
         $rho, |float|, mass density. optional default = 0.0


The response of an elastic orthotropic material is defined by the following constitutive relation:

.. math::

  \boldsymbol{\sigma} = \mathbf{C} \boldsymbol{\varepsilon}


where :math:`\boldsymbol{\sigma}` and :math:`\boldsymbol{\varepsilon}` are the stress and strain vectors in Voigt notation, and :math:`\mathbf{C}` is the elastic stiffness matrix. 
The inverse of the stiffness matrix is given by:

.. math::

  \mathbf{C}^{-1} = \left[\begin{array}{cccccc}
  \frac{1}{E_1} & -\frac{\nu_{21}}{E_2} & -\frac{\nu_{31}}{E_3} & 0 & 0 & 0 \\
  -\frac{\nu_{12}}{E_1} & \frac{1}{E_2} & -\frac{\nu_{32}}{E_3} & 0 & 0 & 0 \\
  -\frac{\nu_{13}}{E_1} & -\frac{\nu_{23}}{E_2} & \frac{1}{E_3} & 0 & 0 & 0 \\
  0 & 0 & 0 & \frac{1}{G_{23}} & 0 & 0 \\
  0 & 0 & 0 & 0 & \frac{1}{G_{31}} & 0 \\
  0 & 0 & 0 & 0 & 0 & \frac{1}{G_{12}}
  \end{array}\right]

with

.. math::

   E_1>0, E_2>0, E_3>0, G_{12}>0, G_{23}>0, G_{13}>0


References
----------

- Zienkiewicz, Olgierd C., Robert L. Taylor, and Sanjay Govindjee. "The Finite Element Method: Its Basis and Fundamentals." Eighth edition. Butterworth-Heinemann, 2025. 


Code Developed by: |mhs|

