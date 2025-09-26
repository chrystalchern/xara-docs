FullGeneral
^^^^^^^^^^^

This command is used to construct a Full General linear system of equation. 
The class utilizes *no* space saving techniques to cut down on the amount of memory used. 
If the matrix is of size, :math:`n \times n`, then storage for an :math:`n \times n` array is sought from memory when the program runs. 
When a solution is required, the *Lapack* routines *DGESV* and *DGETRS* are used. 

.. function:: system FullGeneral

.. warning::
   
   This type of system should almost never be used in production. This is because it requires a lot more memory than every other solver and takes more time in the actual solving operation than any other solver. 

Example
-------

The following example shows how to construct a *FullGeneral* system

1. **Tcl Code**

   .. code-block:: tcl

      system FullGeneral


2. **Python Code**

   .. code-block:: python

      model.system('FullGeneral')

Code Developed by: |fmk|