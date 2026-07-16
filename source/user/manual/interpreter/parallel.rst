Parallel
^^^^^^^^

The following forms of parallelism are supported in |xara|:

* Domain decomposition with distributed memory parallelism is supported on 
  :ref:`locally compiled installations <user-guides-compile>` 
  and is expected to be included in an upcoming release.
  The implementation mirrors that of OpenSeesMP.
* Multithreading with shared memory parallelism is supported on all platforms, 
  and is enabled by default. 
* The `threading <https://docs.python.org/3/library/threading.html>`__ and `multiprocessing <https://docs.python.org/3/library/multiprocessing.html>`__ modules in Python can be used to run multiple |xara| models in parallel, 
  and is supported on all platforms. This is ideal for running multiple simulations with different parameters.
