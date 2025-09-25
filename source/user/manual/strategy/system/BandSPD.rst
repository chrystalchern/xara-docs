BandSPD
^^^^^^^

This class is used for symmetric positive definite (SPD) matrix systems which have a banded profile. 
The matrix is stored as shown below in a 1 dimensional array of size equal to the (bandwidth/2) times the number of unknowns. 
When a solution is required, the Lapack routines ``DPBSV`` and ``DPBTRS`` are used. 

.. function:: system BandSPD

An :math:`n\times n` matrix :math:`\boldsymbol{A}` is a *symmetric positive definite banded* matrix if:

1. :math:`A_{ij}=0 \quad\mbox{if}\quad j<i-k \quad\mbox{ or }\quad j>i+k; \quad k \ge 0.`
2. :math:`A_{ij} = A_{ji}`
3. :math:`y \cdot A y \ne 0` for all non-zero vectors y with real entries (:math:`y \in \mathbb{R}^n`),

The bandwidth of the matrix is :math:`k + k + 1`.
For example, a symmetric 6-by-6 matrix with a right bandwidth of 2:

.. math::
   \begin{bmatrix}
   A_{11} & A_{12} & A_{13} &   0  & \cdots & 0 \\
   & A_{22} & A_{23} & A_{24} & \ddots & \vdots \\
   &        & A_{33} & A_{34} & A_{35} & 0 \\
   &        &        & A_{44} & A_{45} & A_{46} \\
   & sym    &        &        & A_{55} & A_{56} \\
   &        &        &        &        & A_{66}
   \end{bmatrix}

is stored as follows:

.. math::
   \begin{bmatrix}
   A_{11} & A_{12} & A_{13} \\
   A_{22} & A_{23} & A_{24} \\
   A_{33} & A_{34} & A_{35} \\
   A_{44} & A_{45} & A_{46} \\
   A_{55} & A_{56} & 0 \\
   A_{66} & 0 & 0
   \end{bmatrix}

Example
-------

The following example shows how to construct a *BandSPD* system

1. **Tcl Code**

   .. code-block:: tcl

      system BandSPD

2. **Python Code**

   .. code-block:: python

      model.system('BandSPD')

Code developed by: |fmk|
