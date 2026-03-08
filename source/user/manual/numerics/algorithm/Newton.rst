.. _Newton:

Newton
^^^^^^

The Newton-Raphson method is the most widely used and most robust method for solving nonlinear equations. 


.. tabs::
   .. tab:: xara 
      .. autoclass:: xara.algorithm.Newton

   .. tab:: Python

      .. py:method:: Model.algorithm("Newton" [, initial=False, initialThenCurrent=False])
         :no-index: 

         Configure a Newton-Raphson algorithm to solve the current residual equation.

         :param initial: optional flag to indicate to use initial stiffness
         :param initialThenCurrent: optional flag to indicate to use initial stiffness on first step and then current on subsequent steps
         

   .. tab:: Tcl

      .. function:: algorithm Newton <-initial> <-initialThenCurrent>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         -initial, |string|,  optional flag to indicate to use initial stiffness
         -initialThenCurrent, |string|, optional flag to indicate to use initial stiffness on first step and then current on subsequent steps



The Newton-Raphson method is a root-finding algorithm that uses the first few terms of the Taylor series of a function :math:`f(x)` in the vicinity of a suspected root :math:`x_n` to find the root :math:`x^*`. 

The Taylor series of a function :math:`f(x)` about a point :math:`x_n` is given by

.. math::
   
   f(x_n+\Delta x) = f(x_n)+f'(x_n)\Delta x + 1/2f''(x_n) \Delta x^2+....

Keeping terms only to first order,

.. math::
   
   f(x_n+\Delta x) \approx f(x_n)+ f'(x_n)\Delta x

and since at the root we wish to find :math:`x_n + \Delta x`, the function equates to 0, i.e. :math:`f(x_n+\Delta x) = 0`, we can solve for an approximate :math:`\Delta x`

.. math::

   \Delta x \approx -\frac{f(x_n)}{f^{'}(x_n)} = - \frac{df(x_n)}{dx}^{-1}f(x_n)

The Newmark method is thus an iterative method in which, starting at a good initial guess :math:`x_0` we keep iterating until our convergence criteria is met with the following:

.. math::
   
   \Delta x = - \frac{df(x_n)}{dx}^{-1}f(x_n)

.. math::
   
   x_{n+1} = x_n + \Delta x

The method is generalized to :math:`n` unknowns by replacing the above scalar equations with matrix ones.

.. math::
   
   g(U_n+\Delta x) = g(U_n)+\frac{\partial g(U_n)}{\partial U} \Delta U + O(\Delta U^2)

The matrix :math:`\frac{\partial g(U_n)}{\partial U}` is called the system Jacobian matrix and will be denoted :math:`\boldsymbol{K}`:

.. math::

   `\boldsymbol{K} = \frac{\partial g(U_n)}{\partial U}

resulting in our iterative procedure where starting from a good initial guess we iterate until our convergence criteria is met with the following:

.. math::

   \Delta U = - K^{-1}g(U_n)

.. math::

   U_{n+1} = U_n + \Delta U

Example
-------

The following examples demonstrate the command to create a Linear solution algorithm.

.. tabs::

   .. tab:: Tcl

      .. code-block:: tcl

         algorithm Newton

   .. tab:: Python

      .. code-block:: python

         model.algorithm('Newton')

Code Developed by: |fmk|
