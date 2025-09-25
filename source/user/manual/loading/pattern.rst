.. _pattern:

Pattern
^^^^^^^

.. tabs::

   .. tab:: Python 

      .. py:method:: Model.pattern(type, tag, *args)

         Create a pattern of a given type and add it to the :class:`Model`.

         :param |string| type: pattern type
         :param |integer| tag: unique pattern tag.
         :param |list| args: a sequence of args
   
   .. tab:: Tcl

      .. function:: pattern type args ...

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $type, |string|, pattern type
         $eleTag,  |integer|,  unique epattern tag.
         $args, |list|,  a list of args


Each LoadPattern has a TimeSeries associated with it. 
The TimeSeries is used to determine the load factor applied to the loads in the pattern. 
The load factor is a function of time in the domain. 
The load factor is obtained from the associated TimeSeries as a function of the time in the domain.

The following pattern types are available:

.. toctree::
   :maxdepth: 2

   pattern/plainPattern
   pattern/uniformExcitationPattern
   pattern/multiSupportPattern
   pattern/DRM
   pattern/H5DRM
   timeSeries

