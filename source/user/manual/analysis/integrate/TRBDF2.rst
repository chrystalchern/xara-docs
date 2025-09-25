.. _TRBDF2:

TRBDF2
^^^^^^

This command is used to construct a TRBDF2 integrator. 
The TRBDF2 integrator is a composite scheme that alternates between the Trapezoidal scheme and a 3 point backward Euler scheme. 
It does this in an attempt to conserve energy and momentum, something :ref:`Newmark` does not always do. 

.. function:: integrator TRBDF2  


.. note:: 

    * As opposed to dividing the time-step in 2 as outlined in the papers, we just switch alternate between the 2 integration strategies,i.e. the time step in our implementation is double that described in the papers.


References
----------

- Bank, R.E., Coughran W.M., Fichter W., Grosse E.H., Rose, D.J., and
  Smith R.K. “Transient Simulations of Silicon Devices and Circuits”, IEE
  Trans CAD, Vol(4), 436-451, 1985.

- Bathe, K.J. “Conserving Energy and Momentum in Nonlinear Dynamics: A
  Simple Impicit Time Integration Scheme”, Computers and Structures,
  Vol(85), 437-445, 2007. doi:10.1016/j.compstruc.2006.09.004

