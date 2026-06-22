.. _units:

Units
^^^^^

.. py:module:: xara.units
   :synopsis: Predefined constants for common unit systems.

xara does not assume or enforce any unit system.
All model inputs (coordinates, mass, forces, stiffness, etc.) are numeric values; the user must choose a consistent unit system and apply it throughout the model.
The *xara.units* submodule contains predefined constants that can help with keeping track of units, ensuring consistency.


Systems
=======

The following systems are implemented (see :ref:`UnitSymbols` below for definitions of the symbols):

.. raw:: html

   <table>
   <thead>
     <tr>
       <th></th>
       <th>si </th> <!-- si -->
       <th>sim</th> <!-- sinm -->
       <th>us(f)</th> <!-- fps  psf usfp -->
       <th>usi</th> <!-- ips  psi usip -->
     </tr>
   </thead>
   <tbody>
     <tr>
       <td>Length</td>
       <td>meter</td>
       <td>mm</td>
       <td>foot</td>
       <td>inch</td>
      </tr>
      <tr>
       <td>Force</td>
       <td>N</td>
       <td>N</td>
       <td>lbf</td>
       <td>lbf</td>
      </tr>
      <tr>
       <td>Mass</td>
       <td>kg</td>
       <td>tonne</td>
       <td>slug</td>
       <td>lbf s<sup>2</sup>/inch</td></tr>
      <tr><td>Stress</td>
       <td>Pa</td>
       <td>MPa</td>
       <td>lbf/ft<sup>2</sup></td>
       <td>psi (lbf/inch<sup>2</sup>)</td></tr>
      <tr><td>Energy</td>
       <td>J (N × m)</td>
       <td>mJ (10<sup>−3</sup> J)</td>
       <td>ft lbf</td>
       <td>in lbf</td></tr>
      <tr><td>Density</td>
       <td>kg/m<sup>3</sup></td>
       <td>tonne/mm<sup>3</sup></td>
       <td>slug/ft<sup>3</sup></td>
       <td>lbf s<sup>2</sup>/in<sup>4</sup></td></tr></tbody>
   </table>



The idiom for importing constants from a system takes the form:

.. code-block:: Python

   from xara.units.<system> import <symbols>...

where ``<system>`` is one of the implemented systems. 
For example, to import the symbols ``inch``, ``kip``, ``N`` and ``Pa`` from the ``us`` system,

.. code-block:: Python

   from xara.units.us import inch, kip, N, Pa

Occasionally it is convenient to import all symbols using a *star-import*

.. code-block:: Python

   from xara.units.us import *

Note, however, that this is generally considered bad programming style.


.. _UnitSymbols:

Symbols
=======

Each submodule exports the following symbols:


.. _LengthUnits:

Length 
------

.. csv-table::
   :header: "Symbols", "Description"
   :widths: 20, 40

   ``mm``    (also ``millimeter``)   ,  Milimeter
   ``cm``    (also ``centimeter``)   ,  Centimeter
   ``m``     (also ``meter``)        ,  Meter
   ``km``    (also ``kilometer``)    ,  Kilometer
   ``inch``                          , 
   ``ft``    (also ``foot``)         ,  International foot
   ``yd``    (also ``yard``)         ,  International yard
   ``mi``    (also ``mile``)         ,  Mile


Force 
-----

.. csv-table::
   :header: "Symbols", "Description"
   :widths: 20, 40

    ``N``    (also ``newton`` )      , Newton (force)
    ``dyn``  (also ``dyne``   )      , Dyne
    ``pdl``  (also ``poundal``)      , Poundal
    ``lbf``  (also ``poundf`` )      ,
    ``kip``  (also ``klbf``   )      ,


Stress 
-------

.. csv-table::

   Pa           , pascal       ,  "Pascal, N/m:sup:`2`"
   torr         ,              , 
   kPa          , kilopascal   ,  "Kilopascal, 10:sup:`3` Pa"
   MPa          , megapascals  ,  "Megapascal, N/mm:sup:`2` = 10:sup:`6` Pa"
   bar          ,              , 
   atm          , atmosphere   ,  Standard atmosphere
   MPa          , megapascal   , 
   GPa          , gigapascal   , 
   psi          ,              ,  Pound-square-inch
   ksi          ,              , 



Mass 
--------

.. csv-table::

   slug         ,              , 
   lbm          , lbm          ,  International avoirdupois pound
   gm           , gram         , 
   kg           , kilogram     ,  Kilogram
   tonne        ,              ,  "Metric tonne, 10 :sup:`3` kg"
   oz           , ounce        ,  International avoirdupois ounce


Density
-------

.. csv-table::

   ``pcf``          ,              ,  Pounds per cubic foot

.. note::

   The ``p`` in ``pcf`` represents the pound mass (``lbm``), not the pound force (``lbf``) as it does ``psi`` unit.


..
   Area 
   ----

   .. csv-table::

      mm2          ,              ,  Square millimeter
      m2           ,              ,  Square meter
      cm2          ,              ,  Square centimeter
      km2          ,              ,  Square kilometer
      in2          , inch2        ,  Square inch
      ft2          , feet2        ,  Square foot
      yd2          , yard2        ,  Square yard
      mi2          , mile2        ,  Square mile


   Volume 
   ------

   .. csv-table::

      mm3          ,              ,   
      m3           ,              ,   
      cm3          ,              ,   
      km3          ,              ,   
      in3          , inch3        ,   
      ft3          , foot3        ,   
      cyd          , yard3        ,   
      mi3          , mile3        ,   


   Velocity 
   ---------

   .. csv-table::

      mmps         ,              ,  Millimeter per second
      cps          , cmps         ,  Centimeter per second
      mps          ,              ,  Meter per second
      kps          ,              ,  Kilometer per second
      ips          , inchps       ,  Inch per second
      fps          , footps       ,  Foot per second
      yps          ,              ,  Yard per second
      mph          ,              ,  mile per hour


   Acceleration 
   ------------

   .. csv-table::

      mmps2        ,              , 
      cps2         , cmps2        , 
      mps2         ,              , 
      kps2         ,              , 
      ips2         , inchps2      , 
      fps2         , footps2      , 
      yps2         ,              , 
      mph2         ,              , 
      gravity      ,              ,  Standard gravity


Angular Velocity 
----------------

.. csv-table::

   rpm          , revpm        ,  Revolution per minute
   radps        ,              ,  Radian per second

