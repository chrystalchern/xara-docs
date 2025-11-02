Compile
=======

To compile Xara from source, follow these steps:

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


