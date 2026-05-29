.. _axialFiber:

Fiber (*AxialFiber*)
^^^^^^^^^^^^^^^^^^^^


.. tabs::

   .. tab:: Python
    
      .. py:method:: Model.fiber((y, z), A, tag, section)
         :noindex:

         :param y: :math:`y`-coordinate of the fiber
         :type y: float
         :param z: :math:`z`-coordinate of the fiber. This coordinate is discarded in 2D models.
         :type z: float
         :param A: area of the fiber
         :type A: float
         :param material: tag of a pre-existing material created with the :py:meth:`Model.uniaxialMaterial` method.
         :type material: |integer|
         :param section: tag of the section to which the fiber belongs. This argument must be passed by keyword.
         :type section: |integer|


.. note::

   This behavior of this method changes depending on the type of the ``section`` argument.
   The documentation on this page describes the behavior when ``section`` is an :ref:`AxialFiberSection`.

