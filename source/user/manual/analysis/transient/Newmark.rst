.. _Newmark:

Newmark
^^^^^^^

This command is used to construct a Newmark integrator, based on  [Newmark1959]_.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.integrator("Newmark", gamma, beta)
         :no-index:

         :param gamma: float, :math:`\gamma` factor
         :param beta: float, :math:`\beta` factor


   .. tab:: Tcl

      .. function:: integrator Newmark $gamma $beta

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $gamma, |float|,  :math:`\gamma` factor
         $beta, |float|, :math:`\beta` factor

.. note::

   1. If the accelerations are chosen as the unknowns and :math:`\beta` is chosen as 0, the formulation results in the fast but conditionally stable explicit Central Difference method. Otherwise the method is implicit and requires an iterative solution process.
   
   2. Two common sets of choices are:

      Average Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{4}`)
      
      Linear Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{6}`)
   
   3. :math:`\gamma > \frac{1}{2}` results in numerical damping proportional to :math:`\gamma - \frac{1}{2}`
   
   4. The method is second order accurate if and only if :math:`\gamma = \frac{1}{2}`
   
   5. The method is conditionally stable for :math:`\beta \ge \frac{\gamma}{2} \ge \frac{1}{4}`


Theory
------

The Newmark method is a one step implicit method for solving the transient problem, represented by the residual for the momentum equation:

.. math::

   R_{t + \Delta t} = F_{t+\Delta t}^{ext} - M \ddot{\boldsymbol{u}}_{t + \Delta t} - C \dot{\boldsymbol{u}}_{t + \Delta t} + F(\boldsymbol{u}_{t + \Delta t})^{int}

Using the Taylor series approximation of :math:`\boldsymbol{u}_{t+\Delta t}` and :math:`\dot{\boldsymbol{u}}_{t+\Delta t}`:

.. math::

   \boldsymbol{u}_{t+\Delta t} = \boldsymbol{u}_t + \Delta t \dot{\boldsymbol{u}}_t + \frac{\Delta t^2}{2} \ddot{\boldsymbol{u}}_t + \frac{\Delta t^3}{6} \ddot{\boldsymbol{u}}_t + \cdots

   \dot{\boldsymbol{u}}_{t+\Delta t} = \dot{\boldsymbol{u}}_t + \Delta t \ddot{\boldsymbol{u}}_t + \frac{\Delta t^2}{2} \ddot{\boldsymbol{u}}_t + \cdots

Newmark truncated these using the following:

.. math::
   
   \boldsymbol{u}_{t+\Delta t} = u_t + \Delta t \dot{\boldsymbol{u}} + \frac{\Delta t^2}{2} \ddot{\boldsymbol{u}} + \beta {\Delta t^3} \ddot{\boldsymbol{u}}

.. math::

   \dot{\boldsymbol{u}}_{t + \Delta t} = \dot{\boldsymbol{u}}_t + \Delta t \ddot{\boldsymbol{u}}_t + \gamma \Delta t^2 \ddot{\boldsymbol{u}}_t

in which he assumed linear acceleration within a time step, i.e.,

.. math::

   \ddot{\boldsymbol{u}} = \frac{{\ddot{\boldsymbol{u}}_{t+\Delta t}} - \ddot{\boldsymbol{u}}_t}{\Delta t}

which results in the following expressions:

.. math::

   \boldsymbol{u}_{t+\Delta t} = \boldsymbol{u}_t + \Delta t \dot{\boldsymbol{u}}_t + (0.5 - \beta) \Delta t^2 \ddot{\boldsymbol{u}}_t + [\beta \Delta t^2] \ddot{\boldsymbol{u}}_{t+\Delta t}

.. math::

   \dot{\boldsymbol{u}}_{t+\Delta t} = \dot{\boldsymbol{u}}_t + [(1-\gamma)\Delta t] \ddot{\boldsymbol{u}}_t + [\gamma \Delta t ] \ddot{\boldsymbol{u}}_{t+\Delta t}

The variables :math:`\beta` and :math:`\gamma` are numerical parameters that control both the stability of the method and the amount of numerical damping introduced into the system by the method. For :math:`\gamma=\frac{1}{2}` there is no numerical damping; for :math:`\gamma>=\frac{1}{2}` numerical damping is introduced. Two well known and commonly used cases are:

   1. Average Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{4}`)

   2. Constant Acceleration Method (:math:`\gamma=\frac{1}{2}, \beta = \frac{1}{6}`)

The linearization of the Newmark equations gives:

.. math::

   d\boldsymbol{u}_{t+\Delta t}^{i+1} = \beta \Delta t^2 d \ddot{\boldsymbol{u}}_{t+\Delta t}^{i+1}

.. math::

   d \dot{\boldsymbol{u}}_{t+\Delta t}^{i+1} = \gamma \Delta t \ddot{\boldsymbol{u}}_{t+\Delta t}^{i+1}

which gives the update formula when displacement increment is used as unknown in the linearized system as:

.. math::

   \boldsymbol{u}_{t+\Delta t}^{i+1} = \boldsymbol{u}_{t+\Delta t}^i + d\boldsymbol{u}_{t+\Delta t}^{i+1}

   \dot{\boldsymbol{u}}_{t+\Delta t}^{i+1} = \dot{\boldsymbol{u}}_{t+\Delta t}^i + \frac{\gamma}{\beta \Delta t}d\boldsymbol{u}_{t+\Delta t}^{i+1}

   \ddot{\boldsymbol{u}}_{t+\Delta t}^{i+1} = \ddot{\boldsymbol{u}}_{t+\Delta t}^i + \frac{1}{\beta \Delta t^2}d\boldsymbol{u}_{t+\Delta t}^{i+1}

The linearization of the momentum equation using the displacements as the unknowns leads to the following linear equation:

.. math::

   K_{t+\Delta t}^{*i} \Delta \boldsymbol{u}_{t+\Delta t}^{i+1} = R_{t+\Delta t}^i

where,

.. math::
   
   K_{t+\Delta t}^{*i} = K_t + \frac{\gamma}{\beta \Delta t} C_t + \frac{1}{\beta \Delta t^2} M

and

.. math::

   R_{t+\Delta t}^i = F_{t + \Delta t}^{ext} - F (\boldsymbol{u}_{t + \Delta t}^{i-1})^{int} - C \dot{\boldsymbol{u}}_{t+\Delta t}^{i-1} - M \ddot{\boldsymbol{u}}_{t+ \Delta t}^{i-1}


Example 
-------

The following example shows how to construct a *Newmark* Integrator.

.. tabs::

   .. tab:: xara

      .. code-block:: python

         import xara

         model = xara.Model()

         dynam = xara.DynamicAnalysis(integrator=xara.Newmark(0.5, 0.25))

   .. tab:: Python

      .. code-block:: python

         model.integrator("Newmark", 0.5, 0.25)
   
   .. tab:: Tcl

      .. code-block:: tcl

         integrator Newmark 0.5 0.25



References
----------

.. [Newmark1959] Newmark, N.M. "A Method of Computation for Structural Dynamics" ASCE Journal of Engineering Mechanics Division, Vol 85. No EM3, 1959.


Code Developed by: |fmk|