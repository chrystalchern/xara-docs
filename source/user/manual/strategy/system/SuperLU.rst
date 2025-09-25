SuperLU
^^^^^^^

This command is used to construct a SparseGEN linear system of equation. 
As the name implies, this class is used for sparse matrix systems. 
The solution of the sparse matrix is carried out using `SuperLU <https://portal.nersc.gov/project/sparse/superlu/>`_. 

.. function:: system SuperLU

   Configure the model to use the *SuperLU* linear solver.

.. note::

  1. When using the *SuperLU* system, the software will renumber the equations to ensure a fast solve. As a consequence it is a waste of time specifying anything but a *Plain* :ref:`numberer`.
  2. The original and still working command was ``system SparseGEN``


Example
-------

The following example shows how to construct a *SuperLU* system

1. **Tcl Code**

   .. code-block:: tcl

      system SuperLU

2. **Python Code**

   .. code-block:: python

      model.system('SuperLU')



References
----------

- James W. Demmel and Stanley C. Eisenstat and John R. Gilbert and Xiaoye S. Li and Joseph W. H. Liu, "A supernodal approach to sparse partial pivoting", SIAM J. Matrix Analysis and Applications, 20(3), 720-755, 1999. `link <https://portal.nersc.gov/project/sparse/xiaoye-web/simax-29176.pdf>`__ doi: `10.1137/S0895479895291765 <https://doi.org/10.1137/S0895479895291765>`__


Code developed by: |fmk|


