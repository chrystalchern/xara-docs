trace
^^^^^

.. toctree::
   :maxdepth: 1

   LoadControl
   DisplacementControl
   ArcLength
   MinimumUnbalancedDisplacementNorm


Theory 
------


In static nonlinear finite element problems we seek a solution
(:math:`\boldsymbol{u}`, :math:`\lambda`) to the nonlinear equation

.. math::

   \boldsymbol{r}(\boldsymbol{u}, \lambda) = \boldsymbol{0}
   \qquad\text{with}\qquad
   \boldsymbol{r}(\boldsymbol{u}, \lambda) \triangleq \lambda \boldsymbol{p}_f - \boldsymbol{p}_r(\boldsymbol{u})

where :math:`\boldsymbol{r}` is known as the *residual* and represents the equilibrium imbalance of a give *trial* state :math:`\boldsymbol{u}`.
In an incremental analysis, solutions to this
equation are sought at successive incremental steps:

.. math::

   \boldsymbol{r}(\boldsymbol{u}_{n}, \lambda_n) = \lambda_n \boldsymbol{p}_f - \boldsymbol{p}_{\sigma}(\boldsymbol{u}_{n})

The solution to this equation is typically obtained using an iterative
procedure, in which a sequence of approximations
(:math:`\boldsymbol{u}_{n}^{(i)}`, :math:`\lambda_n^{(i)}`),
:math:`i=1,2, ..` is obtained which converges to the solution
(:math:`\boldsymbol{u}_n`, :math:`\lambda_n)`. 
The most frequently used iterative schemes, such as Newton-Raphson, modified Newton, and quasi
Newton schemes, are based on the *linearization* of the residual :math:`\boldsymbol{r}` about a state (:math:`\boldsymbol{u}_{n}`, :math:`\lambda_n`):

.. math::

   \mathcal{L} \boldsymbol{r}(\boldsymbol{u}, \lambda)(\boldsymbol{u}_{n},\lambda_n) = \lambda_n^{(i)} \boldsymbol{p}_f 
    - \boldsymbol{p}_{\sigma}\left(\boldsymbol{u}_{n}^{(i)} \right) - \left[
   \begin{array}{cc}
   \boldsymbol{K}_n^{(i)} & -\boldsymbol{p}_f \\
   \end{array} \right] 
   \left(
   \begin{array}{c}
   \boldsymbol{u}_{n} - \boldsymbol{u}_{n}^{(i)}  \\ 
   \lambda_n - \lambda_n^{(i)} 
   \end{array} \right)

which a system of of :math:`N` equations with (:math:`N+1`) unknowns.
Two solve this, an additional equation is required, the constraint
equation. 
The constraint equation used depends on the static integration
scheme, of which there are a number, for example load control, arc
length, and displacement control.

