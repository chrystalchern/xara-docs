Additions
^^^^^^^^^

Unlike other Python packages which merely wrap the broken OpenSeesPy package, *xara* employs a completely new interface layer that is implemented in C++.

- No global state. It is well know that software should not exhibit global state. 

  - https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html
  - https://testing.googleblog.com/2008/08/root-cause-of-singletons.html
  - https://embeddedartistry.com/fieldatlas/the-problems-with-global-variables/?utm_source=chatgpt.com
  - https://betterembsw.blogspot.com/2014/06/minimize-use-of-global-variables.html
  - https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#Ri-global
  - https://isocpp.org/wiki/faq/coding-standards#global-vars
  - https://www.learncpp.com/cpp-tutorial/why-non-const-global-variables-are-evil/

- Improved :ref:`printA <printA>` for obtaining structural matrices:

  - does not require `FullGen` solver; now all one needs
    to do is call `model.getTangent()`. This is possible due to the
    new consolidated memory ownership model.

  - `-mck` options


- Improved `print` command

  - new `-registry` option.
  - more reliable JSON printing
  - includes `MP_Constraint` information

- Add `-det` option to static integrators:

  - :ref:`ArcLength <ArcLengthControl>`

- add `-det` capability to solvers:

  - `FullGenLapack`, :ref:`Umfpack`, `BandGenLapack`

- Verbosity control

- new `export` command in Python and Tcl, when run through Python
- new `invoke` Tcl command and Python constructs
- new `progress` command in Tcl
- new `=` command, fixes vexing operator precedence in `expr`

- Minimized use of ``exit()`` syscalls.


Diagnostics
---------------

*xara* features several small "quality of life" improvements. These include

* Improved error messages and tracebacks. Error messages have been extensively reworked to allow for colorful and informative error tracebacks. 
  For example, instead of:

  .. figure:: figures/upstream-output.png
     :width: 100%
     :align: center

  one now has:

  .. figure:: figures/xara-output.png
     :width: 100%
     :align: center

..
  * Improved log messages (TODO: Example 5)


