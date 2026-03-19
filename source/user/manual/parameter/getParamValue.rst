.. _getParamValue:

getParamValue
^^^^^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.getParamValue(tag)

         Return the value of a parameter.

         :param |integer| tag: Tag of the :ref:`Parameter <parameter>`.
         :returns: |float| — Current value of the parameter.

   .. tab:: Tcl

      .. function:: getParamValue $paramTag

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $paramTag, |integer|, tag of the parameter whose value is sought
