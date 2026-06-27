.. _nodeResponse:

nodeResponse
^^^^^^^^^^^^

.. tabs::

   .. tab:: Python

      .. py:method:: Model.nodeResponse(node, dof, response)

         Return the response at a specified node and degree of freedom.

         :param |integer| node: The tag of the :ref:`node` whose response is sought.
         :param |integer| dof: The degree of freedom at the node (between 1 and :py:attr:`Model.ndf`, inclusive).
         :param str response: The type of response to return, such as "displacement", "velocity", "acceleration", etc.
         :returns: A |float| representing the requested response at the specified node and degree of freedom.

   .. tab:: Tcl

      .. function:: nodeResponse node? dof? response?

The following table lists the available responses that can be requested:

.. csv-table:: 
    :header: "Name", "Description"
    :widths: 10, 40

    **displacement**, "Translational part of the displacement field"
    **rotation**, "Rotational part of the displacement field"
    **velocity**, "Translational part of the velocity field"
    **angularVelocity**, "Rotational part of the velocity field"
    **acceleration**, "Translational part of the acceleration field"
    **angularAcceleration**, "Rotational part of the acceleration field"
    **reactionForce**, "Translational part of the reaction field"
    **reactionMoment**, "Rotational part of the reaction field"
    **reactionForceIncludingInertia**, "Translational part of the reaction field with inertia terms"
    **reactionMomentIncludingInertia**, "Rotational part of the reaction field with inertia terms"
    **rayleighForce**, "Translational part of the damping force field"
    **rayleighMoment**, "Rotational part of the damping force field"
    **unbalancedForce**, "Translational part of the unbalanced force field"
    **unbalancedForceIncludingInertia**, "Translational part of the unbalanced force field with inertia terms"
    **unbalancedMoment**, "Rotational part of the unbalanced force field"
    **unbalancedMomentIncludingInertia**, "Rotational part of the unbalanced force field with inertia terms"
    **pressure**, "Pore pressure field"
    **modesOfVibration**, "Translational part of the eigenvector fields (all modes are recorded)"
    **modesOfVibrationRotational**, "Rotational part of the eigenvector fields (all modes are recorded)"

