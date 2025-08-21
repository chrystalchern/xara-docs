.. _eigen:

eigen
^^^^^


.. tabs::

   .. tab:: Python 

      .. py:method:: Model.eigen(n, solver="GenBandArpack")

         Perform an eigenvalue analysis and return a list of eigenvalues.

         :param n: number of eigenvalues required.
         :type n: |integer|
         :param solver: optional string detailing type of solver: ``GenBandArpack``, ``SymmBandLapack``, ``FullGenLapack`` (default: ``GenBandArpack``).
         :type solver: |string|
         :returns: A |list| containing ``n`` eigenvalues
   
   .. tab:: Tcl

      .. function:: eigen <$solver> $n

      .. csv-table::
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40
         
         ``n``, |integer|, number of eigenvalues required.
         ``solver``, |string|, "optional string detailing type of solver: -genBandArpack, -symmBandLapack, -fullGenLapack (default: -genBandArpack)."

.. note::

   1.  The eigenvectors are stored at the nodes and can be printed out using a Node Recorder, or the :ref:`nodeEigenvector` method.
   2.  The default eigensolver is able to solve only for :math:`N-1` eigenvalues, where :math:`N` is the number of *inertial* degrees-of-freedom. When running into this limitation the ``-fullGenLapack`` solver can be used instead of the default ``Arpack`` solver.


Theory
------

The *generalized eigenvalue problem* for two symmetric matrices :math:`\boldsymbol{K}` and :math:`M` of size :math:`n \times n` is given by:

.. math::

   \left( \boldsymbol{K} - \lambda \boldsymbol{M} \right) \Phi = 0

where:

*  :math:`\boldsymbol{K}` is the stiffness matrix
*  :math:`\boldsymbol{M}` is the mass matrix
*  :math:`\lambda` is the eigenvalue
*  and :math:`\Phi` is the associated eigenvector

Examples
--------
   
The following example shows how to use the *eigen* method to obtain a list of eigenvalues.

1. **Tcl Code**

   .. code:: tcl

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      set eigenvalues [eigen 10]
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      set eigenvalues [eigen -fullGenLapack 10]

2. **Python Code**

   .. code:: python

      # obtain 10 eigenvalues using the default solver (-genBandArpack)
      eigenvalues = model.eigen(10)
      
      # or, obtain 10 eigenvalues explicitly specifying the solver
      eigenvalues = model.eigen("-fullGenLapack", 10)

Code Developed by: |fmk|
