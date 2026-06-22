.. _Orthotropic:

Orthotropic Wrapper
^^^^^^^^^^^^^^^^^^^

This command is used to construct an Orthotropic material. 
It is a wrapper that can convert any 3D (Linear or Nonlinear) constitutive model to an orthotropic one. [Oller2003]_


.. tabs::
    
    .. tab:: Python

        .. py:class:: xara.MultiaxialMaterial("Orthotropic", material, Ex, Ey, Ez, Gxy, Gyz, Gzx, vxy, vyz, vzx, Asigmaxx, Asigmayy, Asigmazz, Asigmaxyxy, Asigmayzyz, Asigmaxzxz)

          :param material: An instance of a previously defined isotropic :py:class:`xara.MultiaxialMaterial`

    
    .. tab:: Tcl

        .. function:: nDMaterial Orthotropic $matTag $theIsoMatTag $Ex $Ey $Ez $Gxy $Gyz $Gzx $vxy $vyz $vzx $Asigmaxx $Asigmayy $Asigmazz $Asigmaxyxy $Asigmayzyz $Asigmaxzxz

        .. csv-table:: 
            :header: "Argument", "Type", "Description"
            :widths: 10, 10, 40

            $matTag, |integer|, unique tag identifying this orthotropic material wrapper
            $theIsoMatTag, |integer|, unique tag identifying a previously defined isotropic material
            $Ex $Ey $Ez, 3 |float|, Elastic moduli in three mutually perpendicular directions
            $Gxy $Gyz $Gzx, 3 |float|, Shear moduli
            $vxy $vyz $vzx, 3 |float|, Poisson's ratios
            $Asigmaxx, |float|, Ratio of the isotropic to the orthotropic strength along the X direction (Fxx_iso / Fxx_ortho)
            $Asigmayy, |float|, Ratio of the isotropic to the orthotropic strength along the Y direction (Fyy_iso / Fyy_ortho)
            $Asigmazz, |float|, Ratio of the isotropic to the orthotropic strength along the Z direction (Fzz_iso / Fzz_ortho)
            $Asigmaxyxy, |float|, Ratio of the isotropic to the orthotropic shear strength in the XY plane (Fxy_iso / Fxy_ortho)
            $Asigmayzyz, |float|, Ratio of the isotropic to the orthotropic shear strength in the YZ plane (Fyz_iso / Fyz_ortho)
            $Asigmaxzxz, |float|, Ratio of the isotropic to the orthotropic shear strength in the XZ plane (Fxz_iso / Fxz_ortho)


Examples
--------

.. ref-gallery::
   
   examples/material/material-0012


References
----------

.. [Oller2003] | Oller, S., Car, E., & Lubliner, J. (2003). Definition of a general implicit orthotropic yield criterion. Computer methods in applied mechanics and engineering, 192(7-8), 895-912. (`Link to article <https://core.ac.uk/download/pdf/296535134.pdf>`__)

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.

