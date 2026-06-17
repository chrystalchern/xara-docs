.. _section:

Section
^^^^^^^

This command configures a Section, which represents a constitutive model between stress and strain *resultants*.

.. py:currentmodule:: xara

.. tabs::

   .. tab:: Python

      .. py:method:: Model.section(object)

         :param object: section object
         :type object: |string|

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
   Frame <section/frame/index>
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
