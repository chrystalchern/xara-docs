
.. _recorder:

Recorders
*********

Recorders are used to monitor what is happening during the analysis and generate output for the user. 
The output may go to the screen, files, databases, or to remote processes through the TCP/IP options.

.. function:: recorder $type $arg1 $arg2 ...

The type of recorder created and the additional arguments required depends on the ``type`` provided in the command.

.. toctree::
   :caption: Node Information
   :maxdepth: 1

   NodeRecorder
   EnvelopeNodeRecorder

.. toctree::
   :caption: Element Information
   :maxdepth: 1

   ElementRecorder



.. toctree::
   :caption: Model Information
   :maxdepth: 1

   PVDRecorder
   MPCORecorder
   GmshRecorder


.. note::

   The function returns a value:
   
   ``-1`` indicates that the recorder command failed.

   An integer tag that can be used as a handle on the recorder for the remove a recorder in the :ref:`remove`.


Code Developed by: |fmk|

