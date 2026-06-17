.. _InitStrain:

InitStrain
^^^^^^^^^^

.. tabs::
   .. tab:: Python
      .. py:method:: Model.nDMaterial("InitialStrain", tag, otherTag, eps0_11, eps0_22=0.0, eps0_33=0.0, eps0_12=0.0, eps0_23=0.0, eps0_13=0.0)
         :no-index:

         Construct an InitialStrain material wrapper.

         :param tag: integer tag identifying this init-strain material wrapper
         :param otherTag: integer tag identifying the previously defined nD material
         :param eps0_11: initial strain value in the 11 direction
         :param eps0_22: initial strain value in the 22 direction (optional, default = 0.0)
         :param eps0_33: initial strain value in the 33 direction (optional, default = 0.0)
         :param eps0_12: initial strain value in the 12 direction (optional, default = 0.0)
         :param eps0_23: initial strain value in the 23 direction (optional, default = 0.0)
         :param eps0_13: initial strain value in the 13 direction (optional, default = 0.0)


   .. tab:: Tcl

      .. function:: nDMaterial InitStrain $matTag $otherTag $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $matTag, |integer|, "unique tag identifying this init-strain material wrapper"
         $otherTag, |integer|, "unique tag identifying the previously defined nD material"
         $eps0_11 <$eps0_22 $eps0_33 $eps0_12 $eps0_23 $eps0_13>, 1 or 6 |float|, "initial strain values. If only one is given, a volumetric strain = eps0_11 is imposed."


Notes
-----

This material imposes an inital-strain to another material such that :math:`\sigma = f\left (\varepsilon + \varepsilon_{0}\right )`.


Parameters
""""""""""

* ``initial_strain``

Examples
--------

The following example shows how to use the *InitialStrain* wrapper to apply an initial strain of 0.1 in the :math:`x`-direction and 0.0 in the :math:`y` and :math:`z` directions.
The script should print the value -0.1. This is the opposite of the imposed strain in the :math:`z` direction since the tetrahedron has :math:`h=1`.

.. tabs::
   .. tab:: Python

      .. code-block:: Python

         import xara
         ops = xara.Model(ndm=3, ndf=3)
         ops.node(1, (0,0,0))
         ops.node(2, (1,0,0))
         ops.node(3, (0,1,0))
         ops.node(4, (0,0,1))
         ops.fixZ(0.0,  (1,1,1))
         # Create the material to be wrapped
         ops.nDMaterial("ElasticIsotropic", 100, 1000.0, 0.0)
         # Create the wrapper
         ops.nDMaterial("InitStrain", 300,  100, 0.0,0.0,0.1,0.0,0.0,0.0)

         # Create an element and run the analysis
         ops.element("FourNodeTetrahedron", 1,  1,2,3,4,  300)
         ops.timeSeries("Constant", 1)
         ops.pattern("Plain", 1, 1)
         ops.constraints("Transformation")
         ops.numberer("RCM")
         ops.system("FullGeneral")
         ops.test("NormDispIncr", 1.0e-5, 100, 0)
         ops.algorithm("Newton")
         ops.integrator("LoadControl", 1.0)
         ops.analysis("Static")
         ops.analyze(1)
         uz = ops.nodeDisp(4, 3)
         print(uz)

   .. tab:: Tcl 

      .. code-block:: Tcl

         model BasicBuilder -ndm 3 -ndf 3
         node  1  0 0 0 
         node  2  1 0 0 
         node  3  0 1 0 
         node  4  0 0 1
         fixZ 0.0 1 1 1 

         nDMaterial ElasticIsotropic 100 1000.0 0.0

         # Create the wrapper
         nDMaterial InitStrain 300 100 0.0 0.0 0.1 0.0 0.0 0.0

         element FourNodeTetrahedron 1 1 2 3 4 300 
   
         pattern Plain 1 Constant
         constraints Transformation 
         numberer RCM 
         system FullGeneral 
         test NormDispIncr 1e-05 100 0 
         algorithm Newton 
         integrator LoadControl 1.0 
         analysis Static 
         analyze 1 
         set uz [nodeDisp 4 3]




Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
