.. _Umfpack:

Umfpack
^^^^^^^

This command is used to construct a sparse system of equations which uses the `UmfPack <https://people.sc.fsu.edu/~jburkardt/cpp_src/umfpack/umfpack.html>`__  solver. 

.. function:: system Umfpack <-lvalueFact $LVALUE>

``LVALUE*Nnz`` is the amount of additional memory set aside for fill in during the matrix solution where ``Nnz`` is the number of nonzero entries. 
By default the ``LVALUE`` factor is 10. 
You only need to experiment with this if you get error messages back about LVALUE being too small.

The number of threads used by this system can be altered by setting the `OMP_NUM_THREADS` environment variable.

Example 
-------

The following example shows how to construct a Umfpack system

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         system Umfpack


   .. tab:: Python

      .. code-block:: python

         model.system("Umfpack")



References
----------

1. A column pre-ordering strategy for the unsymmetric-pattern multifrontal method, T. A. Davis, ACM Transactions on Mathematical Software, vol 30, no. 2, June 2004, pp. 165-195.

2. Algorithm 832: UMFPACK, an unsymmetric-pattern multifrontal method, T. A. Davis, ACM Transactions on Mathematical Software, vol 30, no. 2, June 2004, pp. 196-199.

3. A combined unifrontal/multifrontal method for unsymmetric sparse matrices, T. A. Davis and I. S. Duff, ACM Transactions on Mathematical Software, vol. 25, no. 1, pp. 1-19, March 1999.

4. An unsymmetric-pattern multifrontal method for sparse LU factorization, T. A. Davis and I. S. Duff, SIAM Journal on Matrix Analysis and Applications, vol 18, no. 1, pp. 140-158, Jan. 1997.
 
Code developed by: |fmk|

