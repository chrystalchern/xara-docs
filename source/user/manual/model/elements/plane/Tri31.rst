
.. _Tri31:

Triangle
^^^^^^^^

``Tri31`` is a constant strain triangular element which uses three nodes and one integration points.

.. py:method:: Model.element("Triangle", tag, nodes, section, [pressure, rho, b1, b2])
   :no-index:

   :param tag: unique :ref:`Element` tag
   :param nodes: a list of three element nodes in counter-clockwise order
   :param section: tuple or int. If int, it is the tag of a previously defined :ref:`Section`. If tuple, it is a tuple of the form (``thick``, ``type``, ``material``) where 
     
         ===================================   ==============================================================================================================
         ``thick`` |float|                     element thickness
         ``type`` |str|                        string representing material behavior. The type parameter can be either ``"PlaneStrain"`` or ``"PlaneStress"``
         ``material`` |integer|                tag of a :ref:`MultiaxialMaterial <nDMaterial>`
         ===================================   ==============================================================================================================
   
   :param pressure: surface pressure (optional, default = 0.0)
   :param rho: element mass density (per unit volume) from which a lumped element mass matrix is computed (optional, default=0.0)
   :param b1: constant body forces defined in the domain (optional, default=0.0)
   :type b1: |float|, optional
   :param b2: constant body forces defined in the domain (optional, default=0.0)
   :type b2: |float|, optional

The valid queries to a Tri31 element through :ref:`eleResponse` are 

#. ``"forces"``, 
#. ``"stresses"``, and 
#. ``"material $mat args..."`` 

Where ``$mat`` refers to the material object at the integration point corresponding to the node numbers in the domain.

