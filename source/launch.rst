Overview
=========

|xara| (pronouced *Kar-ah*, like the Gaelic word for "friend") is a free and open source tool for simulating the nonlinear response of structural and geotechnical systems. 
|xara| is developed by PEER as an alternative front-end to the simulation framework proposed by :ref:`McKenna (1997) <references>`.
The design of the interface was guided by the demands of the |BRACE2| project, for which a suitably *reliable* and *performant* solution was not available.


.. grid:: 2 2 3 3 
   :gutter: 3

   .. grid-item-card:: :fab:`python;sd-text-primary` Python
      :link: user/manual/interpreter/python
      :link-type: doc

      Build and analyze models securely in Python. 
   
   .. grid-item-card:: :fab:`python;sd-text-warning` OpenSeesPy
      :link: OpenSeesPy
      :link-type: ref

      Use the older OpenSeesPy functions to analyze a globally scoped model.

   .. grid-item-card:: :fas:`feather;sd-text-primary` Tcl
      :link: user/manual/interpreter/tcl
      :link-type: doc

      Run old Tcl models or export from Python for faster runs.

   .. :fas:
   .. .. grid-item-card:: Examples
   ..    :img-top: _static/images/xara.png


All three approaches above require only a standard :ref:`install <install>` of |xara|.

.. py:module:: xara
   :synopsis: A Python interface to the OpenSees finite element framework.


.. toctree::
   :hidden:

   self

.. _user-manual:


.. toctree::
   :caption: Documentation
   :maxdepth: 1
   :hidden:

   user/manual/interpreter/index
   user/manual/modeling
   user/manual/meshing/index
   user/manual/loading/index
   user/manual/analysis/index
   user/manual/output/index
   user/manual/numerics/index
   user/manual/modules/index
   gallery

.. 
   gallery/index


.. toctree::
   :caption: About
   :maxdepth: 1
   :hidden:

   user/guides/index
   about/features/index
   about/license
   changelog
   cite


