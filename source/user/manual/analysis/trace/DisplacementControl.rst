DisplacementControl
^^^^^^^^^^^^^^^^^^^

In an analysis step with Displacement Control, the objective is to
control the displacement of a particular degree-of-freedom at a node by a prescribed increment.
To this end, the Displacement Control integrator will solve for the load multiplier :math:`d \lambda` such that the displacement increment at the control DOF is equal to a prescribed value.

.. 
   determine the time step :math:`\Delta \lambda` that will result in a displacement increment for a particular degree-of-freedom at a node to be a prescribed value.

.. tabs::

   .. tab:: Python

      .. py:method:: Model.integrator("DisplacementControl", node, dof, incr [, numIter, dUmin, dUmax])
         :no-index: 

         Configure the *DisplacementControl* integrator.

         :param node: tag identifying the node whose response controls solution
         :type node: |integer|
         :param dof: tag identifying the degree of freedom at the node
         :type dof: |integer|
         :param incr: float value of the displacement increment
         :param numIter: integer value of the number of iterations the user would like to occur in the solution algorithm. Optional; default = 1.0.
         :param dUmin: float value of the min step size the user will allow. Optional; default :math:`\Delta U_{min} = \Delta U_0`
         :param dUmax: float value of the max step size the user will allow. Optional; default :math:`\Delta U_{max} = \Delta U_0`
   
   .. tab:: OpenSees

      .. function:: integrator DisplacementControl $node $dof $incr <$numIter $dUmin $dUmax >

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         ``node``, |integer|, node whose response controls solution
         ``dof``, |integer|, degree of freedom at the node; valid options: 1 through ndf at node.
         ``incr``, |float|, first displacement increment <math>\Delta U_{\text{dof}}</math>
         ``numIter``, |integer|, the number of iterations the user would like to occur in the solution algorithm. Optional; default = 1.0.
         ``dUmin``, |float|,   the min step size the user will allow. optional; default :math:`\Delta U_{min} = \Delta U_0`
         ``dUmax``, |float|, the max step size the user will allow. optional: default :math:`\Delta U_{max} = \Delta U_0`


Example
=======

The following example configures a displacement control algorithm to maintain a constant increment of 0.1 at node 1 in the direction of DOF 2.

.. tabs::

   .. tab:: Python

      model.integrator("DisplacementControl", 1, 2, 0.1)
   
   .. tab:: OpenSees

      .. code-block:: Tcl

         integrator DisplacementControl 1 2 0.1; 


Theory
======

If we write the governing finite element equation at :math:`t + \Delta t` as:

.. math::

   g(u_{t+\Delta t}, \lambda_{t+\Delta t}) = \lambda_{t+\Delta t} F^{ext} - F(u_{t+\Delta t})


where :math:`F(u_{t+\Delta t})` are the internal forces which are a function of the displacements :math:`U_{t+\Delta t}`, :math:`F^{ext}` is the set of reference loads and :math:`\lambda` is the load multiplier. Linearizing the equation results in:

.. math::

   K_{t+\Delta t}^{*i} \Delta U_{t+\Delta t}^{i+1} = \left ( \lambda^i_{t+\Delta t} + \Delta \lambda^i \right ) F^{ext} - F(U_{t+\Delta t})

This equation represents n equations in :math:`n+1` unknowns, and so an additional equation is needed to solve the equation. 
For displacement control, we introduce a new constraint equation in which in each analysis step we set to ensure that the displacement increment for the degree-of-freedom at the specified node is:

.. math::

   \Delta \boldsymbol{u}_\text{dof} = \text{incr}



In Displacement Control the :math:`\Delta u_{\text{dof}}` set to :math:`t + \lambda_{t+1}` where,

.. math::
   
   \Delta \boldsymbol{u}_{\text{dof}}^{t+1} = \max \left( \Delta \boldsymbol{u}_{\mathrm{min}}, \min \left( \Delta u_{\text{max}}, \frac{\text{numIter}}{\text{lastNumIter}} \Delta u_\text{dof}^{t} \right) \right)

