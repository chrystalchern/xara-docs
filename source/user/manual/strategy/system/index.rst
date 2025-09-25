.. _system:

system
******

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.system(type, *args)

         Set the system to be used by the :class:`Model`.

         :param |string| type: The system type.
         :param args: A sequence of arguments specific to *type*.
   
   .. tab:: Tcl

      .. function:: system type? args? ...

This command configures the linear system of equations and solver which store and solve the linearized residual, :math:`\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}`.

The following types are available:

.. toctree::
   :maxdepth: 1

   BandGeneral
   BandSPD
   ProfileSPD
   SuperLU
   Umfpack
   FullGeneral
   SparseSYM
   Mumps

