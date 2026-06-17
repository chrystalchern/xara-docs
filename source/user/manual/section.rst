.. _section:

Section
^^^^^^^

This command configures a Section, which represents a constitutive model between stress and strain *resultants*.

.. py:currentmodule:: xara

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.section(type, tag, *args)

         :param type: section type
         :type type: |string|
         :param tag: unique section tag
         :type tag: |integer|
         :param args: additional arguments dependent on section ``type``

   .. tab:: Tcl

      .. function:: section type? tag? args? ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $type,    |string|,      section type
         $tag,     |integer|,     unique section tag.
         $args, |list|,        a list of material arguments with number dependent on section type


Library
-------


The following section types are valid for :ref:`frame` elements:

.. toctree::
   :maxdepth: 1

   section/Truss
   section/ElasticFrame
   section/axial/index
   section/ShearFiber

.. _PlaneSection:

For :ref:`PlaneElements` elements, the following section types are available:

.. toctree::
   :maxdepth: 1

   section/plane/index


The following section types are valid for :ref:`shells`:

.. toctree::
   :maxdepth: 1

   section/ElasticShell
   section/ShellFiber


..
   .. toctree::
      :maxdepth: 1
   
      section/PlateFiberSection
      section/Isolator2springSection
      section/ReinforcedConcreteLayeredMembraneSection
      section/LayeredMembraneSection
      section/ASDCoupledHinge3D
      section/ParallelSection
      section/SectionAggregator
      section/UniaxialSection
