.. _CubicFrame:

``CubicFrame``
^^^^^^^^^^^^^^

Two-node frame finite element with cubic displacement formulation.

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.element("CubicFrame", tag, nodes, *, section, transform, integration=None, *args)
         :no-index:

         :param tag: unique :ref:`element` tag
         :type tag: |integer|
         :param nodes: tuple of *two* :ref:`node` tags
         :type nodes: tuple
         :param section: integer tag identifying a :ref:`section`.
         :type section: |integer|
         :param transform: identifier for previously-defined :ref:`frame transformation <geomTransf>`
         :type transform: |integer|
         :param integration: identifier for previously-defined integration rule.


This formulation supports higher order strain measures and shear deformations.

The valid :ref:`eleResponse` queries to this element are ``"force"``.

References
----------


Code developed by: |cmp|, |fcf|, |mhs|, |fmk|

