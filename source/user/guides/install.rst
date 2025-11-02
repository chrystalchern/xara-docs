.. _install:

Install
^^^^^^^

*xara* is built on the |OpenSeesRT| distribution of OpenSees, which is developed and maintained at UC Berkeley. 


To install *xara* on Linux and new Macs, run the following command from your shell:

.. code-block:: bash

   python -m pip install xara


On Windows and Macs with Intel processors, it is best to install from source. This takes only two additional steps:

1. Download the source repository to your computer by running:

   .. code-block:: bash
      
      git clone https://github.com/peer-open-source/xara
      cd xara

2. Create an `Anaconda environment <https://www.anaconda.com/>`__ and install the following packages:

   .. tabs::
      .. tab:: MacOS / Linux

         .. code-block:: bash
            
            conda install -c conda-forge fortran-compiler cxx-compiler c-compiler openblas openmpi

      .. tab:: Windows

         .. code-block:: bash

            conda install -c conda-forge cmake ninja ifx_win-64 mkl-devel conda-forge/label/mkl_rc::blas
         
         .. note::
            
            On Windows, make sure to install Visual Studio with the *"Desktop development with C++"* workload.


3. Finally, with this environment activated, install the package with ``pip`` from inside the *xara/* directory created in step 1:

   .. code-block:: bash
      
      python -m pip install -e .

