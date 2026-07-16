Interpreters
^^^^^^^^^^^^

.. toctree::
   :maxdepth: 3
   :hidden:

   python
   openseespy
   tcl
   parallel



There are several ways to use the `xara` package:

- To execute Tcl procedures from a Python script, just create an instance
  of the `xara.Model` class and call its `eval()` method:

  .. code-block:: Python
     
     model = xara.Model()
     model.eval("model Basic -ndm 2")
     model.eval("node 1 0.0 0.0")


- To start an interactive interpreter run the shell command:

  .. code-block:: bash
     
     python -m xara


  To quit the interpreter, just run `exit`:

  .. code-block:: bash
            
     opensees > exit


- The `xara` package exposes a compatibility layer that exactly reproduces
  the *OpenSeesPy* functions, but does so without mandating a single
  global program state. To run OpenSeesPy scripts, just change the import:

  .. code-block:: Python
     
     import openseespy.opensees

  to

  .. code-block:: Python
        
     import opensees.openseespy
