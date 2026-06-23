.. _wipe:

wipe
^^^^

This command is used to clear the domain objects, the recorders, and any analysis objects. 
It resets the :ref:`time <getTime>` in the :class:`Model` to *0.0*.

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.wipe()

         Remove all objects in the model.
   
   .. tab:: Tcl

      .. function:: wipe;

         Remove all objects in the model.

It causes all elements, nodes, constraints, loads to be removed from the domain. 
In addition it deletes all recorders, analysis objects and all material objects created by the model builder. 

.. note::

   Unlike older |OpenSees| distributions, |OpenSeesRT| does not maintain model state with a global varible.
   Consequently, the wipe command is no longer necessary when multiple models are created from a single process.
   In general it is more convenient (and preferable) to create a new :class:`Model` object rather than using the wipe method.


Examples
--------

The following example demonstrates the use of the wipe command.

1. **Tcl Code**

   .. code-block:: none

      wipe

2. **Python Code**

   .. code-block:: python

      model.wipe()


Code Developed by: |fmk|
