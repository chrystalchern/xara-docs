.. _about-features-deprecated:

Deprecations
^^^^^^^^^^^^

The following features of OpenSeesPy are currently supported, but are highly discouraged:

* Section subcommands (``fiber``, ``patch`` and ``layer``) without an explicit ``section`` argument.

* All hard-coded section integrations and shapes like ``WSection2d`` are removed. These classes do not add any functionality to the platform and introduce a burden for maintainers.

* Pattern subcommands (:meth:`Model.load`, :meth:`Model.eleLoad`) without an explicit ``pattern`` argument.

* All thermal elements, materials and elements are deprecated. The implementation introduced unnecessary code duplication. 

