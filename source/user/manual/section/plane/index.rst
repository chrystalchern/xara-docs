.. _PlaneSection:

PlaneSection
^^^^^^^^^^^^

.. tabs::

   .. tab:: Python
      
      .. py:method:: xara.PlaneSection(type, material, thickness)
         :no-index:

         :param type: string identifying the plane section type. Valid options are "PlaneStrain" and "PlaneStress".
         :type type: |string|
         :param material: integer tag identifying a :ref:`material <nDMaterial>`
         :type material: |integer|
         :param thickness: section thickness
         :type thickness: float



Examples
--------


.. ref-gallery::
   :tooltip:

   examples/plane/plane-0002
