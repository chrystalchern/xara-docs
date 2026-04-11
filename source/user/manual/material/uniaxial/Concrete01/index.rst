.. _Concrete01:

Concrete01
^^^^^^^^^^

This command is used to construct a uniaxial Kent-Scott-Park concrete material with degraded linear unloading/reloading stiffness according to the work of Karsan-Jirsa and no tensile strength. 

.. tabs::

   .. tab:: Python

      .. py:method:: uniaxialMaterial("Concrete01", tag, fpc, epsc0, fpcu, epsU)
         :no-index:

         :param int   tag: integer tag identifying material.
         :param float peak_stress: peak compressive stress, typically the concrete strength at 28 days :math:`f'_c` (``Fc``).
         :param float peak_strain: strain at peak stress, :math:`\varepsilon_{c0}`.
         :param float final_stress: Ultimate stress, typically the concrete crushing strength :math:`f'_{cu}` (``Fcu``).
         :param float final_strain: concrete strain at crushing strength.
   
   .. tab:: Tcl

      .. function:: uniaxialMaterial Concrete01  $tag $fpc $epsc0 $fpcu $epsu

      .. csv-table:: 
        :header: "Argument", "Type", "Description"
        :widths: 10, 10, 40

        $tag, |integer|, integer tag identifying material.
        $Fc, |float|,  concrete compressive strength at 28 days.
        $epsc0, |float|, concrete strain at maximum strength* .
        $Fcu, |float|, concrete crushing strength*.
        $epsU, |float|, concrete strain at crushing strength*.

.. note::

   * The initial slope for this model is :math:`E = 2 F_c/\epsilon_{c0}`.



.. figure:: figures/Concrete01.gif
  :align: center
  :figclass: align-center


Example 
-------

.. code-block:: Tcl

   uniaxialMaterial Concrete01 1 -4.0 -0.002 0.0 -0.005; 


The code above defines a *Concrete01* material with tag ``1``, compression strength of 4.0 at strain 0.002 and reaches ultimate strength of 0.0 at strain of 0.005


References
----------

Sensitivity is due to 
- Scott, Michael H., Paolo Franchin, Gregory L. Fenves, and Filip C. Filippou.  "Response Sensitivity for Nonlinear Beam–Column Elements.” 
  Journal of Structural Engineering 130, no. 9 (2004): 1281–88. 
  https://doi.org/10.1061/(asce)0733-9445(2004)130:9(1281).


Code Developed by: |fcf|, |mhscott|

