.. _FrameSection:

Frame
^^^^^


.. py:class:: xara.Section(type, shape)
    
    Construct a frame section object.

    :param type: string identifying the section type. Standard options are "Elastic", "UniaxialFiber", and "MultiaxialFiber". Legacy options are "Fiber" and "NDFiber".
    :type type: |string|
    :param shape: :ref:`Shape <FrameShape>` object defining the geometry and material composition of the section.
    :gparam Fibers fibers: Coarse fiber layout, optional. If not provided, a default layout will be generated based on the section shape and material properties.


.. toctree::
   :hidden:

   shapes

