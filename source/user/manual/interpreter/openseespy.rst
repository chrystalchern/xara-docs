.. _OpenSeesPy:

OpenSeesPy
^^^^^^^^^^

.. warning::

    Due to the design of OpenSeesPy, scripts built with this approach will be extremely brittle. 
    The best practice is to transition to the standard Python workflow. See the :ref:`Transitioning Guide <transitioning_to_xara>`.



The `xara` package exposes a compatibility layer that exactly reproduces
the *OpenSeesPy* functions, but does so without mandating a single
global program state. To run OpenSeesPy scripts, just change the import:

.. code-block:: Python
    
    import openseespy.opensees

to

.. code-block:: Python
    
    import opensees.openseespy
