.. _TransientAnalysis:

Transient Analysis
^^^^^^^^^^^^^^^^^^

.. autoclass:: xara.TransientAnalysis
   :members:


.. toctree::
   :maxdepth: 1

   Newmark
   GeneralizedAlpha
   TRBDF2



Theory
------

In a nonlinear transient finite element analysis we seek a solution
(:math:`\boldsymbol{u}`, :math:`\dot{\boldsymbol{u}}`,
:math:`\ddot{\boldsymbol{u}}`) to the nonlinear residual equation

.. math:: 
   
   \boldsymbol{r}({\boldsymbol{u}},\dot{\boldsymbol{u}}, \ddot{\boldsymbol{u}}) = \boldsymbol{p}_f(t) - \boldsymbol{p}_{\mathrm{i}}(\ddot{\boldsymbol{u}}) - \boldsymbol{p}_{\sigma}({\boldsymbol{u}}, \dot{\boldsymbol{u}}) = \boldsymbol{0}

The most widely used technique for solving the transient non-linear
finite element equation is to use an incremental direct integration scheme. 
In the incremental formulation, a solution to the equation is sought at successive time
steps :math:`\Delta t` apart.

.. math::

   \boldsymbol{r}({\boldsymbol{u}}_{n \Delta t},\dot{\boldsymbol{u}}_{n \Delta t}, \ddot{\boldsymbol{u}}_{n \Delta t}) = \boldsymbol{p}_f(n \Delta t) -
   \boldsymbol{p}_{\mathrm{i}}(\ddot{\boldsymbol{u}}_{n \Delta t}) - \boldsymbol{p}_{\sigma}({\boldsymbol{u}}_{n \Delta t}, \dot{\boldsymbol{u}}_{n \Delta t})


For each time step, :math:`t`, the integration schemes provide two
operators, :math:`\operatorname{I}_1` and :math:`\operatorname{I}_2`, to
relate the velocity and accelerations at the time step as a function of
the displacement at the time step and the response at previous time
steps:

.. math::

   \dot {\boldsymbol{u}}_{t} = {\mathrm{I}}_1 ({\boldsymbol{u}}_t, {\boldsymbol{u}}_{t-\Delta t}, \dot {\boldsymbol{u}}_{t-\Delta t},
   \ddot {\boldsymbol{u}}_{t - \Delta t}, {\boldsymbol{u}}_{t - 2\Delta t}, \dot {\boldsymbol{u}}_{t - 2 \Delta t}. ..., )
   %\label{I1}

.. math::

   \ddot {\boldsymbol{u}}_{t} = {\mathrm{I}}_2 ({\boldsymbol{u}}_t, {\boldsymbol{u}}_{t-\Delta t}, \dot{\boldsymbol{u}}_{t-\Delta t},
   \ddot{\boldsymbol{u}}_{t - \Delta t}, {\boldsymbol{u}}_{t - 2\Delta t}, \dot{\boldsymbol{u}}_{t - 2 \Delta t}. ..., )
   %\label{I2}

These allow us to rewrite equation `fullTimeForm <#fullTimeForm>`__, in
terms of a single response quantity, typically the displacement:

.. math::


   \boldsymbol{r}({\boldsymbol{u}}_t) = \boldsymbol{p}_f(t) - \boldsymbol{p}_{\mathrm{i}}(\ddot{\boldsymbol{u}}_t) - \boldsymbol{p}_{\sigma}({\boldsymbol{u}}_t, \dot{\boldsymbol{u}}_t)
   %\label{genForm}

The solution of this equation is typically obtained using an iterative
procedure, i.e. making an initial prediction for
:math:`{\boldsymbol{u}}_{t}`, denoted :math:`{\boldsymbol{u}}_{t}^{(0)}`
a sequence of approximations :math:`{\boldsymbol{u}}_{t}^{(i)}`,
:math:`i=1,2, ..` is obtained which converges (we hope) to the solution
:math:`{\boldsymbol{u}}_{t}`. The most frequently used iterative
schemes, such as Newton-Raphson, modified Newton, and quasi Newton
schemes, are based on a Taylor expansion of
equation `genForm <#genForm>`__ about :math:`{\boldsymbol{u}}_{t}`:

.. math::

   \boldsymbol{r}({\boldsymbol{u}}_{t}) = 
   \boldsymbol{r}({\boldsymbol{u}}_{t}^{(i)}) +
   \left[ {\frac{\partial \boldsymbol{r}}{\partial {\boldsymbol{u}}_t} \vert}_{{\boldsymbol{u}}_{t}^{(i)}}\right]
   \left( {\boldsymbol{u}}_{t} - {\boldsymbol{u}}_{t}^{(i)} \right)

.. math::

   \boldsymbol{r}({\boldsymbol{u}}_{t}) = \boldsymbol{p}_f (t) - \boldsymbol{p}_{\mathrm{i}} \left( \ddot {\boldsymbol{u}}_{t}^{(i)} \right) - \boldsymbol{p}_{\sigma} \left( \dot {\boldsymbol{u}}_{t}^{(i)}, {\boldsymbol{u}}_{t}^{(i)} \right)- \left[
     \boldsymbol{M}^{(i)} {\mathrm{I}}_2'
   + \boldsymbol{C}^{(i)} {\mathrm{I}}_1'
   + \boldsymbol{K}^{(i)}  \right]
    \left( {\boldsymbol{u}}_{t} - {\boldsymbol{u}}_{t}^{(i)} \right)
   %\label{femGenFormTaylor}

To start the iteration scheme, trial values for
:math:`{\boldsymbol{u}}_{t}`, :math:`\dot
{\boldsymbol{u}}_{t}` and :math:`\ddot {\boldsymbol{u}}_{t}` are
required. These are obtained by assuming
:math:`{\boldsymbol{u}}_{t}^{(0)} = {\boldsymbol{u}}_{t-\Delta t}`. The
:math:`\dot {\boldsymbol{u}}_{t}^{(0)}` and
:math:`\ddot {\boldsymbol{u}}_{t}^{(0)}` can then be obtained from the
operators for the integration scheme.

