.. _InitStress:

InitStress
^^^^^^^^^^

.. function:: nDMaterial InitStress $tag $otherTag $sig0_11 <$sig0_22 $sig0_33 $sig0_12 $sig0_23 $sig0_13>


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, "unique tag identifying this material"
   $otherTag, |integer|, "unique tag identifying the previously defined nD material"
   $sig0_11 <$sig0_22 $sig0_33 $sig0_12 $sig0_23 $sig0_13>, 1 or 6 |float|, "initial stress values. If only one is given, a volumetric strain = sig0_11 is imposed."


Notes
-----

It is a wrapper that imposes an inital stress to another material such that :math:`\sigma = f\left (\varepsilon + \varepsilon_{0}\right )`.


Parameters
""""""""""

* ``initial_stress``



Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
