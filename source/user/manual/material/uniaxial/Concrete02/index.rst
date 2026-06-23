.. _Concrete02:

Concrete02
^^^^^^^^^^

*Concrete02* is a uniaxial concrete material with linear tension softening as described by [Yassin1994]_

.. tabs::

   .. tab:: Python

      .. py:class:: xara.UniaxialMaterial("Concrete02", Fc, epsc0, fpcu, epsU, lamda, ft, Ets)
         :no-index:

         :param Fc: peak compressive stress
         :type Fc: |float|
         :param epsc0: strain at peak compressive stress
         :type epsc0: |float|
         :param fpcu: compressive crushing strength
         :type fpcu: |float|
         :param epsU: concrete strain at crushing strength
         :type epsU: |float|
         :param lamda: ratio between unloading slope at epscu and initial slope
         :gparam Tension Ft: tensile strength
         :gtype Ft: |float|
         :gparam Tension Ets: tension softening stiffness (absolute value) (slope of the linear tension softening branch)
         :gtype Ets: |float|


   .. tab:: Tcl

      .. function:: uniaxialMaterial Concrete02 $tag $fpc $epsc0 $fpcu $epsU $lambda $ft $Ets 


      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, integer tag identifying material.
         $fpc, |float|,  concrete compressive strength at 28 days (compression is negative)* .
         $epsc0, |float|, concrete strain at maximum strength* .
         $fpcu, |float|, concrete crushing strength*.
         $epsU, |float|, concrete strain at crushing strength*.
         $lambda, |float|, ratio between unloading slope at ``epscu`` and initial slope.
         $ft, |float|, tensile strength.
         $ets, |float|, tension softening stiffness (absolute value) (slope of the linear tension softening branch) 


.. note::
   
   * The initial slope for this model is :math:`E = 2 F_c/\epsilon_{c0}`.



.. figure:: figures/Concrete02.jpg
   :align: center
   :figclass: align-center


Comparison with :ref:`Concrete01`

.. figure:: figures/Concrete02Hysteretic.jpg
   :align: center
   :figclass: align-center

Hognestad's (\citet{hognestad1951study}, \citet{kent1973cyclic}, \textcite{scott1982stressstrain}) monotonic
compression envelope is simply the piecewise union of an initially parabolic response, followed by a linear loss of strength: 

.. math::
   :label: eq:hognestad

   \sigma(\varepsilon)=\left\{\begin{aligned}
   K f_{cp}\left[2\left(\frac{\varepsilon}{\varepsilon_{cp}}\right)-\left(\frac{\varepsilon}{\varepsilon_{cp}}\right)^{2}\right], &\quad \varepsilon \leq \varepsilon_{cp} \\
   K f_{cp}\left[1-Z\left(\varepsilon-\varepsilon_{cp}\right)\right], &\quad \varepsilon_{cp}<\varepsilon \leq \varepsilon_{cu} \\
   0.2 K f_{cu}, &\quad \varepsilon > \varepsilon_{cu}
   \end{aligned}\right.

where $K$ (a scaling for strength) and $Z$ (strain softening slope) are model parameters. 
A hysteretic loading-reloading algorithm for this curve was proposed by [Yassin1994]_


Examples
--------


.. ref-gallery::
   
   examples/material/material-0003


References
----------

Code Developed by: |fcf|

.. [Yassin1994]  Mohd Hisham Mohd Yassin, "Nonlinear Analysis of Prestressed Concrete Structures under Monotonic and Cycling Loads", PhD dissertation, University of California, Berkeley, 1994. 
