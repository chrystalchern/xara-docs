Surface
^^^^^^^

.. currentmodule:: xara

.. py:method:: Model.surface(split, element, args, points=None, name=None, **kwds)

        Create a surface mesh of elements in the current model.

        :param split: The number of elements in the local :math:`x` and :math:`y` directions.
        :type split: tuple of integers
        :param element: The name of the element type to use.
        :type element: str
        :param args: The arguments to pass to the element constructor.
        :type args: tuple or dict
        :param points: The coordinates of the points in the mesh.
        :type points: dict
        :param kwds: The keyword arguments to pass to the element constructor.
        :type kwds: dict
        :param order: The order of the elements to use. Default is 1 for linear elements.
        :type order: int
        :param shape: The shape of the elements to use. Can be "Q" for quadrilateral or "T" for triangular.
        :type shape: str
        :return: Surface


This method is analogous to the `Create_Block <https://fedeas.net/Functions/latest/Utilities/PreProcessing/Structure/Create_Block/>`__ utility of *FEDEASLab*.


Examples
--------


.. ref-gallery::

   examples/plane/plane-0002
   examples/plane/plane-0101


The following snippet creates a :math:`8 \times 4` mesh of linear (``order = 1``)
quadrilateral elements.

.. code-block:: python

    import xara 
    model = xara.Model(ndm=2, ndf=2)
    mesh = model.surface((8, 4),
                  element="Quad",
                  args={"section": 1},
                  order=1,
                  points={
                    1: [  0.0,   0.0],
                    2: [   L,    0.0],
                    3: [   L,     d ],
                    4: [  0.0,    d ]
            })


