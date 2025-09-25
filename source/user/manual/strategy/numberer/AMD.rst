AMD
^^^^^^^^^^^^^^^^^^^^^^

An *AMD* numberer uses the *approximate minimum degree* [1]_ scheme to order the matrix equations. 

.. tabs::

   .. tab:: Python

      .. py:method:: Model.numberer("AMD")
         :no-index:

   .. tab:: Tcl

      .. function:: numberer AMD


Example
-------

The following example shows how to define an alternative min-degree numberer.

1. **Tcl Code**

   .. code-block:: tcl

      numberer AMD


2. **Python Code**

   .. code-block:: python

      model.numberer("AMD")




References
----------

.. [1]  Algorithm 837: AMD, An approximate minimum degree ordering algorithm, P. Amestoy, T. A. Davis, and I. S. Duff, ACM Transactions on Mathematical Software, vol 30, no. 3, Sept. 2004, pp. 381-388.

*  An approximate minimum degree ordering algorithm, P. Amestoy, T. A. Davis, and I. S. Duff, SIAM Journal on Matrix Analysis and Applications, vol 17, no. 4, pp. 886-905, Dec. 1996.
      
*  Direct Methods for Sparse Linear Systems, T. A. Davis, SIAM, Philadelphia, Sept. 2006. Part of the SIAM Book Series on the Fundamentals of Algorithms.

Code developed by: |fmk|
