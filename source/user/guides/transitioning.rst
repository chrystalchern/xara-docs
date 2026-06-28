

Transitioning
^^^^^^^^^^^^^

The only step required to transition from OpenSeesPy to |xara| is to 
switch import statements from ``openseespy.opensees`` to ``opensees.openseespy``. 

With this change, most scripts should work without any other modifications. 
Once the switch is made, some simple changes to make scripts more readable are:

* Change string flags to Python keywords. For example, change

  .. code-block:: python

     import openseespy.opensees as ops
     ops.model("BasicBuilder", "-ndm", 2, "-ndf", 3)
  
  to:

  .. code-block:: python

     import opensees.openseespy as ops
     ops.model("BasicBuilder", ndm=2, ndf=3)

* Group related arguments into tuples. For example, change

  .. code-block:: python

     ops.node(1, 0.0, 0.0)
  
  to:

  .. code-block:: python

     ops.node(1, (0.0, 0.0))

  Both forms above are equivalent in |xara|, but the second form is more readable and easier to maintain. 

* Prefer keyword arguments over positional arguments in supported commands. For example, change

  .. code-block:: python

     ops.uniaxialMaterial("Steel01", 1, 29000, 0.02)
  
  to:

  .. code-block:: python

     ops.uniaxialMaterial("Steel01", tag, E=29000, b=0.02)
  
  .. note::

     In general, a ``tag`` argument cannot be specified as a keyword argument.





* Change ``ops`` to a :py:class:`xara.Model` instance for model building commands. For example, change

  .. code-block:: python

     ops.model("BasicBuilder", "-ndm", 2, "-ndf", 3)
     ops.node(1, 0.0, 0.0)
  
  to:

  .. code-block:: python

     model = xara.Model("BasicBuilder", ndm=2, ndf=3)
     model.node(1, 0.0, 0.0)
