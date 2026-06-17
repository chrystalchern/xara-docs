.. _PlaneStrain:

PlaneStrain
^^^^^^^^^^^

A *PlaneStrain* section maintains a condition of plane strain in a 2D solid element.

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.section("PlaneStrain", tag, material, thickness)
         :no-index:

         :param tag: integer tag identifying the section
         :type tag: |integer|
         :param material: integer tag identifying a :ref:`nDMaterial`
         :type material: |integer|
         :param thickness: section thickness
         :type thickness: float

The plane strain condition is characterized by the constraints:

.. math::

   \mathbf{g}_n \cdot \boldsymbol{E}\mathbf{g}_n = 0

Example
=======


.. ref-gallery::
    :tooltip:

    examples/plane/plane-0002


.. tabs::

   .. tab:: Python

      .. code-block:: Python

         import xara
         model = xara.Model(ndm=2, ndf=2)

         model.material("ElasticIsotropic", 1, E=29e3, nu=0.3)
         # Create the PlaneStrain section referencing material 1
         # and with a thickness of 2.5
         model.section("PlaneStrain", 1, 2.5, material=1)

   .. tab:: OpenSees (Tcl)
      
      .. code-block:: Tcl
         
         model BasicBuilder -ndm 2 -ndf 2
         nDMaterial ElasticIsotropic 1 -E 29000 -nu 0.3
         section PlaneStrain 1 2.5 -material 1

A complete example is available at the STAIRLab `gallery <https://gallery.stairlab.io/examples/example6/>`_.


