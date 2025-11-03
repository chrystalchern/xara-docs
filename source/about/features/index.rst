Features
^^^^^^^^

A strong feature of xara is its backwards compatibility with OpenSeesPy and Tcl scripts. 
This compatibility is described in `Compatibility <CompatibilityLayer>`_.
..
   Xara offers several advanced features that make it a powerful tool for nonlinear finite element analysis:
   - **Mixed Formulations**: It supports mixed formulations for beams and solids, enabling accurate modeling of complex structural systems.
   - **Extensive Material Models**: With over 200 material models, Xara provides flexibility for simulating various materials and their nonlinear behaviors.
   - **Performance Optimization**: Built on the OpenSeesRT framework, Xara delivers substantial performance improvements over traditional interpreters.
   - **Continuation Algorithms**: These algorithms are designed to solve highly nonlinear problems efficiently, making Xara suitable for challenging engineering scenarios.
   - **Stateless Modeling**: Xara introduces a `Model` class for true stateless modeling, allowing users to work without relying on a single global program state.
   - `Compatibility Layer <CompatibilityLayer>`: Although *xara* in includes a completely rewritten interpreter architecture, compatibility layers allow legacy OpenSeesPy and Tcl scripts to run with minimal modifications.


.. toctree::
   :hidden:
   :maxdepth: 1

   compatibility
   improvements
   deprecated
   suspended
   dropped

