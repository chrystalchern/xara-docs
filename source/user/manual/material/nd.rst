.. _nDMaterial:

Multiaxial
^^^^^^^^^^


.. tabs::
   
   .. tab:: Python 

      .. py:method:: Model.material(type, tag, *args)

         Define a material.

         :param type: material type
         :type type: |string|
         :param tag: unique material tag.
         :type tag: |integer|
         :param args: additional arguments dependent on material ``type``


   .. tab:: Tcl

      .. function:: material $type $tag {*}$args

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $type, |string|,      material type
         $tag,  |integer|,     unique material tag.
         $args, |list|,        a list of material arguments with number dependent on material type


A material represents the constitutive (stress-strain) relationship at a gauss-point of an element. 

.. note::

   All materials will respond to ``"strain"``, and ``"stress"`` through :ref:`eleResponse`. 
   Some materials have additional queries to which they will respond. These are documented in the *notes* section for those materials.


The following materials are available:

.. toctree::
   :maxdepth: 1

   ndMaterials/ElasticIsotropic
   ndMaterials/ElasticOrthotropic
   plastic/J2Plasticity
   plastic/DruckerPrager
   ndMaterials/ManzariDafalias

.. toctree::
   :maxdepth: 1

   damage/FariaPlasticDamage

.. toctree::
   :maxdepth: 1

   wrapper/Series3D
   wrapper/Parallel3D
   wrapper/InitialStrain
   wrapper/Orthotropic

..
   BoundingCamClay
   PM4Sand
   PM4Silt
   PressureIndependentMultiYield
   PressureDependentMultiYield
   PressureDependentMultiYield02
   J2CyclicBoundingSurface
   SAniSandMS

   ndMaterials/ASDConcrete3D
   ndMaterials/ASDPlasticMaterial
   ndMaterials/OrthotropicRAConcrete
   ndMaterials/SmearedSteelDoubleLayer


..
    Concrete Damage Model
    Plane Stress Material
    Plane Strain Material
    Multi Axial Cyclic Plasticity
    Plate Fiber Material
    Plane Stress Concrete Materials
    FSAM - 2D RC Panel Constitutive Behavior
    Tsinghua Sand Models
    CycLiqCP Material (Cyclic ElasticPlasticity)
    CycLiqCPSP Material
    Stress Density Material
    Materials for Modeling Concrete Walls
    PlaneStressUserMaterial
    PlateFromPlaneStress
    PlateRebar
    LayeredShell
    Contact Materials for 2D and 3D
    ContactMaterial2D
    ContactMaterial3D
    Wrapper material for Initial State Analysis
    InitialStateAnalysisWrapper
    UC San Diego soil models (Linear/Nonlinear, dry/drained/undrained soil response under general 2D/3D static/cyclic loading conditions (please visit UCSD for examples)
    PressureIndependMultiYield Material
    PressureDependMultiYield Material
    PressureDependMultiYield02 Material
    PressureDependMultiYield03 Material
    UC San Diego Saturated Undrained soil
    FluidSolidPorousMaterial
    Misc.
    AcousticMedium
    Steel & Reinforcing-Steel Materials
    UVCmultiaxial (Updated Voce-Chaboche)
    UVCplanestress (Updated Voce-Chaboche)


