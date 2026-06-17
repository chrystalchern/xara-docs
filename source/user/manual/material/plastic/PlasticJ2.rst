

Plastic
^^^^^^^


.. tabs::

   .. tab:: Python
      
      .. py:class:: xara.MultiaxialMaterial("Plastic", K, G, Fy, Fs, Hsat, Hiso)
         :no-index:

         :gparam Elastic K: Bulk modulus, :math:`\kappa` [1]_
         :gtype K: |float|
         :gparam Elastic G: Shear modulus, :math:`\mu` [1]_
         :gtype G: |float|
         :gparam Elastic E: Young's modulus, :math:`E` [1]_
         :gtype E: |float|
         :gparam Plastic Fy: Initial yield stress, :math:`F_y` [1]_
         :gparam "Isotropic Hardening" Hiso: linear isotropic hardening modulus
         :gtype Hiso: |float|
         :gparam "Nonlinear Hardening" Fs: Saturation yield stress
         :gtype Fs: |float|
         :gparam "Nonlinear Hardening" Hsat: exponential hardening parameter
         :gtype Hsat: |float|
   
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
