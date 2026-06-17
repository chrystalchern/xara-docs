.. _CentralDifference:

Central Difference
------------------

.. tabs::

   .. tab:: Python (RT)

      .. py:method:: Model.integrator("CentralDifference")
         :no-index:

   .. tab:: Tcl

      .. function:: integrator CentralDifference


.. note::

    * The calculation of :math:`u_{t+\Delta t}`, as shown below, is based on using the equilibrium equation at time :math:`t`. For this reason the method is called an explicit integration method.
    * If there is no Rayleigh damping and the C matrix is 0, for a diagonal mass matrix a diagonal solver may and should be used.
    * For stability, :math:`\frac{\Delta t}{T_n} < \frac{1}{\pi}` 


Theory
^^^^^^

The Central difference approximations for velocity and acceleration:

.. math::

    v_n = \frac{u_{n+1} - u_{n-1}}{2 \Delta t}

.. math::

    a_n = \frac{u_{n+1} - 2 u_n + u_{n-1}}{\Delta t^2}

In the Central Difference method we determine the displacement solution at time :math:`t+\delta t` by considering the the eqilibrium equation for the finite element system in motion at time t:

.. math::
   M \ddot u_t + C \dot u_t + K u_t = R_t

which when using the above two expressions of becomes:

.. math::
    \left ( \frac{1}{\Delta t^2} M + \frac{1}{2 \Delta t} C \right ) u_{t+\Delta t} = R_t - \left (K - \frac{2}{\Delta t^2}M \right )u_t - \left (\frac{1}{\Delta t^2}M - \frac{1}{2 \Delta t} C \right) u_{t-\Delta t}

