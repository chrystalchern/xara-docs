.. _ASDConcrete3D:

ASDConcrete3D
^^^^^^^^^^^^^

.. image:: ASDConcrete3D.gif
   :width: 20%
   :align: center


| This command is used to construct an ASDConcrete3D material, a plastic-damage model for concrete and masonry like materials. [Petracca2022]_, [Oliver2008]_
| It is based on continuum-damage theory, were the stress tensor can be explicitly obtained from the total strain tensor, without internal iterations at the constitutive level. This makes it fast and robust, suitable for the simulation of large-scale structures. Plasticity is added in a simplified way, in order to have the overall effect of inelastic deformation, but keeping the simplicity of continuum-damage models.
| To improve robustness and convergence of the simulation in case of strain-softening, this model optionally allows to use the IMPL-EX integration scheme (a mixed IMPLicit EXplicit integration scheme).

.. tabs::
   .. tab:: Python

      .. py:method:: Model.nDMaterial("ASDConcrete3D", tag, E, v, **kwds)
         
         :param tag: unique material tag
         :type tag: integer
         :param E: Young's modulus
         :type E: float
         :param v: Poisson's ratio
         :type v: float
         :param rho: mass density
         :type rho: float
         :param Fc: concrete compressive strength, :math:`F_c`
         :type Fc: float
         :param Ft: concrete tension (rupture) strength, :math:`F_t`
         :type Ft: float
         :param list Te:  Optional.  A list of total-strain values for the tensile hardening-softening law. If not specified, ``Te`` will be computed automatically from ``Fc`` and ``Ft``. If specified, ``Te`` will override ``Fc`` and ``ft``.
         :param list Ts:  Optional.  A list of stress values for the tensile hardening-softening law. If not specified, ``Ts`` will be computed automatically from ``Fc`` and ``Ft``. If specified, ``Ts`` will override ``Fc`` and ``ft``.
         :param list Td:  Optional.  A list of damage values for the tensile hardening-softening law. If not defined, no stiffness degradation will be considered.  If not specified, ``Td`` will be computed automatically from ``Fc`` and ``ft``. If specified, ``Td`` will override ``Fc`` and ``ft``.
         :param list Ce:  Optional.  A list of total-strain values for the compressive hardening-softening law.  If not specified, ``Ce`` will be computed automatically from ``Fc`` and ``ft``. If specified, ``Ce`` will override ``Fc`` and ``ft``.
         :param list Cs:  Optional.  A list of stress values for the compressive hardening-softening law.  If not specified, ``Cs`` will be computed automatically from ``Fc`` and ``ft``. If specified, ``Cs`` will override ``Fc`` and ``ft``.
         :param list Cd:  Optional.  A list of damage values for the compressive hardening-softening law. If not defined, no stiffness degradation will be considered. If not specified, ``Cd`` will be computed automatically from ``Fc`` and ``ft``. If specified, ``Cd`` will override ``Fc`` and ``ft``.
         :param bool implex: Optional. If defined, the IMPL-EX integration will be used, otherwise the standard implicit integration will be used (default).
         :param tuple implexControl: ``(implexErrorTolerance, implexTimeReductionLimit)``. Optional.  **implexErrorTolerance**: Relative error tolerance. **implexTimeReductionLimit**: Minimum allowed relative reduction of the time-step. If the error introduced by the IMPL-EX algorithm is larger than **implexErrorTolerance** , the material will fail during the computation. The user can therfore use an adaptive time-step to reduce the time-step to keep the error under control. If the reduction of the time-step is smaller than **implexTimeReductionLimit** , the error control will be skipped. Suggested values: ``implexControl=(0.05, 0.01)``.
         :param float implexAlpha: Optional. Default = 1. The :math:`\alpha` coefficient for the explicit extrapolation of the internal variables in the IMPL-EX algorithm. It can range from 0 to 1.
         :param tuple crackPlanes: Optional. ``(nct, ncc, smoothingAngle)``. If defined, it activates the anisotropy of internal variables. Tensile internal variables are stored on crack-planes that are equally spaced every :math:`90/nc_t` degrees. Compressive internal variables are stored on crack-planes that are equally spaced every :math:`90/nc_c` degrees. The active crack-plane is chosen based on the current principal stress directions. **smoothingAngle**: Angle in degrees used to smooth the internal variables on crack-planes around the active crack-plane. Suggested values: ``crackPlanes=(4, 4, 45.0)``
         :param float eta: Optional. The viscosity parameter :math:`\eta`, representing the relaxation time of the viscoplastic system.  If defined, the rate-dependent model is used (By default the model is rate-independent).
         :param bool tangent: Optional. If defined, the tangent constitutive matrix is used. By default, the secant stiffness is used.
         :param float autoRegularization: Optional. If defined, and if the tensile and/or the compressive hardening-softening law has strain-softening, the area under the hardening-softening law is assumed to be a real fracture energy (:math:`G_f` with dimension = :math:`F/L`), and the specific fracture energy :math:`g_f` (with dimension = :math:`F/L^2`) is automatically computed as :math:`g_f=G_f/l_{ch}`, where :math:`l_{ch}` is the characteristic length of the Finite Element. In this case ``autoRegularization`` is 1. If, instead, the area is a specific fracture energy (:math:`g_{f,ref}` with dimension = :math:`F/L^2`), ``autoRegularization`` should be set equal to the experimental size used to obtain the strain from the displacement jump. In this case, the regularization will be performed as :math:`g_f=G_f/l_{ch} = g_{f,ref}*l_{ch,ref}/l_{ch}`
         :param float Kc: Optional. A coefficient that defines the shape of the failure surface in triaxial compression. It must be :math:`1/2 < K_c \le 1`, default = :math:`2/3`. The lower :math:`K_c`, the stronger is the material in triaxial compression (see figure below).
         :param float cdf: Optional (default = 0). The Cross-Damage-Factor (CDF) controls the dilatancy of the material. ``cdf`` should be :math:`\ge 0`. The larger cdf, the smaller the dilatancy. 0 is the optimal value for concrete.


   .. tab:: Tcl 

      .. function::
         nDMaterial ASDConcrete3D $tag $E $v <-rho $rho>
         <-fc $fc> <-ft ``Ft``>
         <-Te $Te -Ts $Ts <-Td $Td>>
         <-Ce $Ce -Cs $Cs <-Cd $Cd>>
         <-implex> <-implexControl $implexErrorTolerance $implexTimeReductionLimit> <-implexAlpha $alpha>
         <-crackPlanes $nct $ncc $smoothingAngle>
         <-eta $eta> <-tangent> <-autoRegularization $lch_ref> <-Kc $Kc>
         <-cdf $cdf>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|, "Unique tag identifying this material."
         $E $v, 2 |float|, "Mandatory. Young's modulus and Poisson's ratio."
         -rho $rho, |string| + |float|, "Optional. **-rho**: A keyword that precedes the float. **$rho**: The mass density."
         -fc $fc, |string| + |float|, "Optional. **-fc**: A keyword that precedes the float. **$fc**: The concrete compressive strength."
         -ft ``Ft``, |string| + |float|, "Optional. **-ft**: A keyword that precedes the float. **$ft**: The concrete tension (rupture) strength."
         -Te $Te, |string| + |list|, "Optional. **-Te**: A keyword that precedes the list. **$Te**: A list of total-strain values for the tensile hardening-softening law. If not specified, $Te will be computed automatically from $fc and $ft. If specified, $Te will override $fc and $ft."
         -Ts $Ts, |string| + |list|, "Optional. **-Ts**: A keyword that precedes the list. **$Ts**: A list of stress values for the tensile hardening-softening law. If not specified, $Ts will be computed automatically from $fc and $ft. If specified, $Ts will override $fc and $ft."
         -Td $Td, |string| + |list|, "Optional. **-Td**: A keyword that precedes the list. **$Td**: A list of damage values for the tensile hardening-softening law. If not defined, no stiffness degradation will be considered.  If not specified, $Td will be computed automatically from $fc and $ft. If specified, $Td will override $fc and $ft."
         -Ce $Ce, |string| + |list|, "Optional. **-Ce**: A keyword that precedes the list. **$Ce**: A list of total-strain values for the compressive hardening-softening law.  If not specified, $Ce will be computed automatically from $fc and $ft. If specified, $Ce will override $fc and $ft."
         -Cs $Cs, |string| + |list|, "Optional. **-Cs**: A keyword that precedes the list. **$Cs**: A list of stress values for the compressive hardening-softening law.  If not specified, $Cs will be computed automatically from $fc and $ft. If specified, $Cs will override $fc and $ft."
         -Cd $Cd, |string| + |list|, "Optional. **-Cd**: A keyword that precedes the list. **$Cd**: A list of damage values for the compressive hardening-softening law. If not defined, no stiffness degradation will be considered. If not specified, $Cd will be computed automatically from $fc and $ft. If specified, $Cd will override $fc and $ft."
         -implex, |string|, "Optional. If defined, the IMPL-EX integration will be used, otherwise the standard implicit integration will be used (default)."
         -implexControl $implexErrorTolerance $implexTimeReductionLimit, |string| + 2 |float|, "Optional. **-implexControl**: Activates the control of the IMPL-EX error. **implexErrorTolerance**: Relative error tolerance. **implexTimeReductionLimit**: Minimum allowed relative reduction of the time-step. If the error introduced by the IMPL-EX algorithm is larger than **implexErrorTolerance** , the material will fail during the computation. The user can therfore use an adaptive time-step to reduce the time-step to keep the error under control. If the reduction of the time-step is smaller than **implexTimeReductionLimit** , the error control will be skipped. Suggested values: -implexControl 0.05 0.01."
         -implexAlpha $alpha, |string| + |float|, "Optional. Default = 1. The :math:`\alpha` coefficient for the explicit extrapolation of the internal variables in the IMPL-EX algorithm. It can range from 0 to 1."
         -crackPlanes $nct $ncc $smoothingAngle, |string| + 2 |integer| + |float|, "Optional. If defined, it activates the anisotropy of internal variables. Tensile internal variables are stored on crack-planes that are equally spaced every :math:`90/nc_t` degrees. Compressive internal variables are stored on crack-planes that are equally spaced every :math:`90/nc_c` degrees. The active crack-plane is chosen based on the current principal stress directions. **smoothingAngle**: Angle in degrees used to smooth the internal variables on crack-planes around the active crack-plane. Suggested values: -crackPlanes 4 4 45.0"
         -eta $eta, |string| + |float|, "Optional. If defined, the rate-dependent model is used (By default the model is rate-independent). **-eta**: Activates the rate-dependent model. **eta**: The viscosity parameter :math:`\eta`, representing the relaxation time of the viscoplastic system."
         -tangent, |string|, "Optional. If defined, the tangent constitutive matrix is used. By default, the secant stiffness is used."
         -autoRegularization $lch_ref, |string| + |float|, "Optional. If defined, and if the tensile and/or the compressive hardening-softening law has strain-softening, the area under the hardening-softening law is assumed to be a real fracture energy (:math:`G_f` with dimension = :math:`F/L`), and the specific fracture energy :math:`g_f` (with dimension = :math:`F/L^2`) is automatically computed as :math:`g_f=G_f/l_{ch}`, where :math:`l_{ch}` is the characteristic length of the Finite Element. In this case $lch_ref is 1. If, instead, the area is a specific fracture energy (:math:`g_{f,ref}` with dimension = :math:`F/L^2`), $lch_ref should be set equal to the experimental size used to obtain the strain from the displacement jump. In this case, the regularization will be performed as :math:`g_f=G_f/l_{ch} = g_{f,ref}*l_{ch,ref}/l_{ch}`"
         -Kc $Kc, |string| + |float|, "
         | Optional. **-Kc**: A keyword that precedes the float. **$Kc**: A coefficient that defines the shape of the failure surface in triaxial compression. It must be :math:`1/2 < K_c <= 1`, default = :math:`2/3`. The lower :math:`K_c`, the stronger is the material in triaxial compression:
         .. figure:: ASDConcrete3D_Kc.png
            :align: center
            :figclass: align-center

            Effect of :math:`K_c` on the triaxial-compression part of the failure surface.
         "
         -cdf $cdf, |string| + |float|, "Optional (default = 0). The Cross-Damage-Factor (cdf) control the dilatancy of the material. cdf should be >= 0. The larger cdf, the smaller the dilatancy. 0 is the optimal value for concrete."

Theory
------

In the following description, all variables without subscripts refer to the current time-step, while those with the :math:`n` and :math:`n-1` subscripts refer to the same variables at the two previous (known) time steps.
The trial effective stress tensor is computed from the previous effective stress :math:`\bar{\sigma}_{n}` and the trial elastic stress increment :math:`C_{0}:\left (\varepsilon - \varepsilon_{n}\right )`:

.. math::
   \tilde{\sigma} = \bar{\sigma}_{n} + C_{0}:\left (\varepsilon - \varepsilon_{n}\right )

It is then split into its positive (:math:`\tilde{\sigma}^{+}`) and negative (:math:`\tilde{\sigma}^{-}`) parts, using the positive principal stresses (:math:`\langle \tilde{\sigma}_{i} \rangle`) and their principal directions (:math:`p_{i}`):

.. math::
   \begin{align} \tilde{\sigma}^{+} = \sum_{i=1}^{3} \langle \tilde{\sigma}_{i} \rangle p_{i}\otimes p_{i} && \tilde{\sigma}^{-} = \tilde{\sigma} - \tilde{\sigma}^{+} \end{align}

Two equivalent scalar stress measures for the tensile (:math:`\tilde{\tau}^+`) and compressive (:math:`\tilde{\tau}^-`) behaviors are obtained from the trial effective stress tensor :math:`\tilde{\sigma}` (or from its negative part :math:`\tilde{\sigma}^{-}` for the compressive behavior) using the following damage surfaces [Lubliner1989]_:

.. math::
   \tilde{\tau}^+ = f\left(\tilde{\sigma} \right) = H\left (\tilde{\sigma}_{\mathrm{max}} \right )\left [\frac{1}{1-\alpha}\left(\alpha\tilde{I}_1+\sqrt[]{3\tilde{J}_2}+\beta\langle \tilde{\sigma}_{max} \rangle \right )\frac{1}{\phi} \right ]

.. math::
   \tilde{\tau}^- = f\left(\tilde{\sigma}^{-} \right) = H(-\tilde{\sigma}_{\mathrm{min}})\left [\frac{1}{1-\alpha}\left(\alpha\tilde{I}_1+\sqrt[]{3\tilde{J}_2}+\gamma\langle -\tilde{\sigma}_{max} \rangle \right ) \right ]

| where :math:`\tilde{I}_1` is the first invariant of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\tilde{J}_2` is the second invariant of the deviator of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\sigma_{max}` is the maximum principal stress of :math:`\tilde{\sigma}` (or :math:`\tilde{\sigma}^{-}`), :math:`\alpha = 4/33`, :math:`\beta = 23/3`, :math:`\phi = 10`, :math:`\gamma= 3(1 - K_c) / (2 K_c - 1)`.

The equivalent stress measures :math:`\tilde{\tau}^+` and :math:`\tilde{\tau}^-` are converted into their trial total-strain counter-parts :math:`\tilde{x}^+` and :math:`\tilde{x}^-` accounting for the equivalent plastic strain from the previous step:

.. math::
   \tilde{x}^{\pm} = \frac{\tilde{\tau}^{\pm}}{E} + x_{pl,n}

To impose the irreversibity of plasticity and damage, and to account for rate-dependency (if :math:`\eta \gt 0`), the current equivalent strain measures are updated as follows:

.. math::
   x^{\pm} = \begin{cases}    \frac{\eta}{\eta +\Delta t} x^{\pm}_n + \frac{\Delta t}{\eta +\Delta t} \tilde{x}^{\pm}, & \text{if } \tilde{x}^{\pm} > x^{\pm}_n\\ x^{\pm}_n, & \text{otherwise}           \end{cases}

The equivalent total-strain measures are then plugged into the hardening-softening laws to obtain the plastic and cracking damage variables :math:`d_{pl}^{\pm}` and :math:`d_{cr}^{\pm}`, and the effective (:math:`\bar{\sigma}`) and nominal (:math:`\sigma`) stress tensors are computed as:

.. math::
   \begin{align} \bar{\sigma}^+ = \left (1-d^{+}_{pl}\right ) \tilde{\sigma}^+, && \bar{\sigma}^- = \left (1-d^{-}_{pl}\right ) \tilde{\sigma}^-, && \bar{\sigma} = \bar{\sigma}^+ + \bar{\sigma}^- \end{align}

.. math::
   \sigma = \left (1-d^{+}_{cr}\right ) \bar{\sigma}^+ + \left (1-d^{-}_{cr}\right ) \bar{\sigma}^-


.. figure:: ASDConcrete3D_Theory_01.png
   :align: center
   :figclass: align-center

   A schematic representation of the elastic predictor followed by the plastic and damage correctors in a representative uniaxial case.

.. figure:: ASDConcrete3D_Kc.png
   :align: center
   :figclass: align-center

   Effect of :math:`K_c` on the triaxial-compression part of the failure surface.



Responses
---------

* All standard material responses: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.
* **damage**: 2 components (:math:`d^+`, :math:`d^-`). The cracking damage variables. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
* **damage -avg** or **Damage -avg**: 2 components (:math:`d^+`, :math:`d^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
* **equivalentPlasticStrain** or **EquivalentPlasticStrain**: 2 components (:math:`x_{pl}^+`, :math:`x_{pl}^-`). The equivalent plastic strains. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
* **equivalentPlasticStrain -avg** or **EquivalentPlasticStrain -avg**: 2 components (:math:`x_{pl}^+`, :math:`x_{pl}^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
* **equivalentTotalStrain** or **EquivalentTotalStrain**: 2 components (:math:`x^+`, :math:`x^-`). The equivalent total strains. If option **-crackPlanes** is used, it gives the maximum values among all crack-planes.
* **equivalentTotalStrain -avg** or **EquivalentTotalStrain -avg**: 2 components (:math:`x^+`, :math:`x^-`). Same as above. If option **-crackPlanes** is used, it gives the average values of the crack-planes.
* **cw** or **crackWidth** or **CrackWidth**: 1 component (:math:`cw`). The equivalent tensile total strain minus the equivalent strain at the onset of crack, times the characteristic length of the parent element. If option **-crackPlanes** is used, it gives the maximum value among all crack-planes.
* **cw -avg** or **crackWidth -avg** or **CrackWidth -avg**: 1 component (:math:`cw`). Same as above. If option **-crackPlanes** is used, it gives the average value of the crack-planes.
* **crackInfo $Nx $Ny $Nz**: 2 components (:math:`ID`, :math:`X`). Gives the 0-based index (ID) and the tensile equivalent total strain (X) of the crack-plane with the normal vector closest to (Nx, Ny, Nz).
* **crushInfo $Nx $Ny $Nz**: 2 components (:math:`ID`, :math:`X`). Same as above, but for the compressive response.

Examples
--------


.. ref-gallery::

   examples/material/solid-0203
   examples/material/material-0005


Damage Surface
==============

A Python example to draw the damage surface in the plane-stress case: :download:`ASDConcrete3D_Ex_Surface.py <ASDConcrete3D_Ex_Surface.py>`
   
.. image:: ASDConcrete3D_Ex_Surface_Output.gif
   :width: 30%
   :align: center


Hardening/Softening Laws
========================

A Python module to generate typical hardening-softening laws for normal concrete is provided here :download:`ASDConcrete3D_MakeLaws.py <ASDConcrete3D_MakeLaws.py>`
Simple example to test it under uniaxial conditions in tension and compression: :download:`ASDConcrete3D_Ex_CyclicUniaxialTension.py <ASDConcrete3D_Ex_CyclicUniaxialCompression.py>` and :download:`ASDConcrete3D_Ex_CyclicUniaxialCompression.py <ASDConcrete3D_Ex_CyclicUniaxialCompression.py>`

.. |asd_conc_pic_1| image:: ASDConcrete3D_Ex_CyclicUniaxialTension.gif
   :width: 30%

.. |asd_conc_pic_2| image:: ASDConcrete3D_Ex_CyclicUniaxialCompression.gif
   :width: 30%

|asd_conc_pic_1| |asd_conc_pic_2|


References
----------

.. [Lubliner1989] Lubliner, J., Oliver, J., Oller, S., & Onate, E. (1989). "A plastic-damage model for concrete" International Journal of Solids and Structures, 25(3), 299-326

.. [Petracca2022] Petracca, M., Camata, G., Spacone, E., & Pelà, L. (2022). "Efficient Constitutive Model for Continuous Micro-Modeling of Masonry Structures" International Journal of Architectural Heritage, 1-13 (`Link to article <https://www.researchgate.net/profile/Luca-Pela/publication/363656245_Efficient_Constitutive_Model_for_Continuous_Micro-Modeling_of_Masonry_Structures/links/6332e7f1165ca22787785134/Efficient-Constitutive-Model-for-Continuous-Micro-Modeling-of-Masonry-Structures.pdf>`__)

.. [Oliver2008] Oliver, J., Huespe, A. E., & Cante, J. C. (2008). "An implicit/explicit integration scheme to increase computability of non-linear material and contact/friction problems" Computer Methods in Applied Mechanics and Engineering, 197(21-24), 1865-1889 (`Link to article <https://core.ac.uk/download/pdf/325948712.pdf>`__)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
