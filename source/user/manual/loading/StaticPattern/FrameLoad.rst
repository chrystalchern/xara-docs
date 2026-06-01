FrameLoad
^^^^^^^^^

.. py:method:: Model.eleLoad("FrameLoad", distr, n, [r, m], /, basis, shape)
   :no-index:

   :param distr: key defining the distribution of the load. Options are ``"Dirac"`` and ``"Heaviside"``
   :type distr: str 
   :param n: force values 
   :param basis: string defining the coordinate basis of the load arguments ``n`` and ``m``. Options are ``"local"``, ``"global"``, and ``"director"``

.. note::
   
   This loading is intended to supesede the preexisting beam loads. Currently it is only supported by :ref:`ExactFrame`

Theory
------


Distributions 
~~~~~~~~~~~~~

.. math::

   \boldsymbol{p}_{In} = - \int  N_I(x) \boldsymbol{p}_{n}(x) \, d x

and

.. math::

   \boldsymbol{p}_{Im} = - \int  N_I(x) \boldsymbol{p}_{m}(x) \, d x

where

.. math::

   \boldsymbol{p}_{n}(x) = \sum Q_i(x) \boldsymbol{n}_{i}


``Dirac``
*********

:math:`P_i = \delta(x - x_i)` so that :math:`\boldsymbol{p}_I = N_I(x_i) \boldsymbol{p}_i`


``Heaviside``
*************



Tangents
~~~~~~~~

- Follower, Concentric

  .. math::
     -\begin{bmatrix}
     \boldsymbol{0} & N_I N_J \boldsymbol{p}^{\times} \\
     \boldsymbol{0} & \boldsymbol{0}
     \end{bmatrix}

- Reference, Eccentric

  .. math::
     \begin{bmatrix}
     \boldsymbol{0} &  \boldsymbol{0} \\
     \boldsymbol{0} & \boldsymbol{r}^{\times} \boldsymbol{p}^{\times}
     \end{bmatrix}

- Follower, Eccentric

  .. math::
     \begin{bmatrix}
     \boldsymbol{0} & N_I N_J \boldsymbol{p}^{\times} \\
     \boldsymbol{0} & \boldsymbol{r}^{\times} \boldsymbol{p}^{\times}
     \end{bmatrix}

- Reference, Concentric

  .. math::
      \begin{bmatrix}
      \boldsymbol{0} &  \boldsymbol{0} \\
      \boldsymbol{0} & \boldsymbol{0}
      \end{bmatrix}