.. _pathTimeSeries:

Path TimeSeries
^^^^^^^^^^^^^^^

In a *Path* time series, the relationship between load factor and time is defined as a series of discrete points in the 2d space (load factor, time). 
When the time specified does not match any of the input points, linear interpolation is used between points. 
There are many ways to specify the load path:

For a load path where the factors are specified in a tcl list with a constant time interval between points:

.. tabs::
   .. tab:: Python
      .. py:method:: Model.timeSeries("Path", tag, dt=dt, values=values, [factor, useLast, prependZero, startTime])
         :no-index:

         :param integer tag: integer tag identifying time series.
         :param float dt: time interval between specified points.
         :param list values: list of load factors.
         :param float factor: optional, a factor to multiply load factors by (default = 1.0).
         :param bool useLast: optional, to use last value after the end of the series (default = 0.0).
         :param bool prependZero: optional, to prepend a zero value to the series of load factors (default = false).
         :param float tStart: optional, to provide a start time for provided load factors (default = 0.0).
   
   .. tab:: Tcl

      .. function:: timeSeries Path $tag -dt $dt -values {list_of_values} <-factor $cFactor> <-useLast> <-prependZero> <-startTime $tStart>

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

            $tag, |integer|,	   unique tag among TimeSeries objects.
            $filePath, |string|, file containing the load factors values
            $fileTime, |string|,  file containing the time values for corresponding load factors
            $dt, |float|,	   time interval between specified points.
            {list_of_times}	 time values in a list
            {list_of_values}	 load factor values in a list
            $cFactor, |float|, "optional, a factor to multiply load factors by (default = 1.0)"
            -useLast, |string|, "optional, to use last value after the end of the series (default = 0.0)"
            -prependZero, |string|, "optional, to prepend a zero value to the series of load factors (default = false)."
            $tStart, |float|,  "optional, to provide a start time for provided load factors (default = 0.0)"
         

For a load path where the factors are specified in a file for a constant time interval between points:

.. tabs::

   .. tab:: Tcl

      .. function:: timeSeries Path $tag -dt $dt -filePath $filePath <-factor $cFactor> <-useLast> <-prependZero> <-startTime $tStart>


         :param integer tag: integer tag identifying time series.
         :param float dt: time interval between specified points.
         :param string filePath: file containing the load factors values.
         :param float factor: optional, a factor to multiply load factors by (default = 1.0).
         :param bool useLast: optional, to use last value after the end of the series (default = 0.0).
         :param bool prependZero: optional, to prepend a zero value to the series of load factors (default = false).
         :param float tStart: optional, to provide a start time for provided load factors (default = 0.0).



For a load path where both time and values are specified in files


.. function:: timeSeries Path $tag -fileTime $fileTime -filePath $filePath <-factor $cFactor> <-useLast>

.. note::

   * Linear interpolation is performed between points.

   * If the specified time is beyond last point (AND WATCH FOR NUMERICAL ROUNDOFF), 0.0 is returned. 
     Specify ``useLast`` to use the last data point instead of 0.0.

   * The transient integration methods generally assume zero initial conditions, so it is important that any timeSeries that is being used in a transient analysis starts from zero (first data point in the timeSeries = 0.0). 
     To guarantee that this is the case the optional parameter ``prependZero`` can be specified to prepend a zero value to the provided timeSeries.


Examples
--------

For a load path where the values are specified at non-constant time intervals:

.. tabs::

   .. tab:: Python

      .. code-block:: Python

         model.timeSeries("Path", 2, time=[0.0, 0.2, 0.4, 1.0], values=[0.0, 1.0, 2.0, 0.0])

   .. tab:: Tcl
      .. code-block:: Tcl

         timeSeries Path 2 -time {0.0 0.2 0.4 1.0} -values {0.0 1.0 2.0 0.0}




Code developed by: |fmk|
