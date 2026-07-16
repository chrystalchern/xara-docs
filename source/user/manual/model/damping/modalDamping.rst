.. _modalDamping:

Modal Damping
^^^^^^^^^^^^^

.. function:: modalDamping $factor

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $factor, |float|,  damping factor.


.. note::

   In Xara the tangent stiffness will always be formed to consistently incorporate modal damping effects, regardless of the matrix storage scheme that was selected. 
   

Example
-------


1. **Tcl Code**

   .. code-block:: tcl

        set N 2 ; # Number of modes for modal damping
        eigen $N

        modalDamping 0.05 0.02 ;# 5% in mode 1, 2% in mode 2


Resources that discuss modal damping include [ChopraMcKenna2015]_


