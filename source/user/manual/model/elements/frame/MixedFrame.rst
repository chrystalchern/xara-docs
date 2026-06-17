
``MixedFrame``: Frame with force-interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two-node mixed finite element formulation for 3D frames.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.element("MixedFrame", tag, nodes, section=None, transform=None, integration=None, *args)
         :no-index:

         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of *two* :ref:`node` tags
         :type nodes: tuple
         :param section: Section object to be created at the element Gauss points. 
         :type section: :py:class:`xara.Section`
         :param transform: identifier for previously-defined :ref:`frame transformation <geomTransf>`
         :type transform: |integer|
         :param integration: identifier for previously-defined integration rule.


This formulation supports higher order strain measures and shear deformations.

The valid :ref:`eleResponse` queries to this element are ``"force"``.

References
----------


Code developed by: |cmp|, |fcf|, |mhs|, |fmk|

