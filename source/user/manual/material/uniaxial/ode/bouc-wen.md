# Bouc-Wen



```{eval-rst}

.. figure:: figures/bouc-beta.png
   :width: 50%
   :align: center

.. py:method:: xara.UniaxialMaterial("BWBF", E, Fy, alpha, n, **options)
   :no-index:

   Construct a uniaxial Bouc-Wen material with optional pinching and degradation.

   :param E: initial stiffness, :math:`E` [1]_
   :type  E: float
   :param Fy: yield force, :math:`F_y` [1]_
   :type  Fy: float
   :param alpha: ratio of post-yield stiffness to the initial elastic stiffenss, :math:`0 \leq \alpha \leq 1` [1]_
   :type  alpha: float
   :param n: sharpness of yield, :math:`n` [1]_
   :type  n: float
   :param beta: hysteretic hardening shape parameter :math:`\beta`, defaults to :math:`\beta=0.5` [1]_
   :type  beta: float, optional
   :param strength_rate: strength degradation rate, :math:`\delta_{\nu}` 
   :type  strength_rate: float
   :param stiffness_rate: stiffness degradation rate, :math:`\delta_{\eta}`
   :type  stiffness_rate: float
   :param pinch_slope: pinching slope, :math:`p`
   :type  pinch_slope: float
   :param pinch_start: pinching initiation, :math:`q`
   :type  pinch_start: float
   :param pinch_slip: measure of total slip, :math:`\zeta`
   :type  pinch_slip: float
   :param pinch_rate: pinching rate, :math:`\delta_{\psi}`
   :type  pinch_rate: float
   :param pinch_size: pinching magnitude, :math:`\psi_0`
   :type  pinch_size: float
   :param lamda: pinching severity, :math:`\lambda`
   :type  lamda: float

```

## Parameters

```{eval-rst}
.. py:class:: BoucWen

   .. py:attribute:: E
      :type: float

      Initial stiffness :math:`E`

   .. py:attribute:: Fy
      :type: float
   
      Yield stress of the hysteretic curve :math:`F_y`. Analogous to :py:attr:`Steel02.Fy`.
   
   .. py:attribute:: beta
      :type: float
      :value: 0.5
   
      Hysteretic shape parameter :math:`\beta`.

   .. py:attribute:: pinch_slope
      :type: float
      :value: 0.0

      Optional pinching parameter :math:`p` introduced by Baber and Noori (1986).

   .. py:attribute:: pinch_start
      :type: float
      :value: 0.0
      
      Optional pinching parameter :math:`q` introduced by Foliente (1995). When :math:`q = 0` the pinching formulation of Baber and Noori (1986) is recovered.


.. [1] This argument is supported by the :ref:`parameter <parameter>` commands.

..
  .. py:method:: Model.uniaxialMaterial("FullBoucWen", tag, E, Fy, alpha [, beta, gamma, n] [, detla_v, delta_n, lamda, p, q, zeta, detla_w, po])


```


## OpenSees Compatibility

This material superceeds the following materials, which are supported for legacy purposes:

```{eval-rst}

.. tabs::

   .. tab:: BoucWen

      Bouc-Wen-Baber, written by Terje Haukaas and described by Haukaas and Der Kiureghian (2003).
      
      .. code-block:: Tcl

         uniaxialMaterial BoucWen $tag $b $E $n $gamma $beta $Ao \
                                  $delta_a $delta_v $delta_n

      Note that this version does not expose an :math:`F_y` parameter.


   .. tab:: BoucWenOriginal
      
      Bouc-Wen without pinching or degradation, implemented by A. Schellenberg.

      .. code-block:: Tcl

         uniaxialMaterial BoucWenOriginal tag E? Fy? alphaL? < alphaNL? mu? n? beta? gamma? >

      In order to capture hardening effects that may occur in various hysteretic systems, this material appends a Duffing-like nonlinear term to the stress, parameterized by the exponent :math:`\mu`:

      .. math::
         
         \sigma = \alpha_L E \varepsilon + \alpha_{NL} E \operatorname{sgn}(\varepsilon)\|\varepsilon\|^{\mu} + \bar{F}_y z
      
      where 

      .. math::
         
         \bar{F}_y \triangleq F_y - \alpha_{L} F_y - \alpha_{NL}E\, \left( \frac{F_y}{E}\right)^{\mu}

      An example with :math:`\beta = \gamma = 0.5`, :math:`\mu = 2`, :math:`n = 1`:

      .. code-block:: Tcl
         
         uniaxialMaterial BoucWenOriginal 1 $E $Fy $alphaL $alphaNL 2.0 1.0 0.5 0.5

      References:

      * Hybrid Simulation of Seismic Isolation Systems Applied to an APR-1400 Nuclear Power Plant


   .. tab:: BWBN

      Bouc-Wen with Foliente pinching, but no degradation. Implemented by Raquib Hossain

      .. code-block:: Tcl

         uniaxialMaterial BWBN tag \
                          alpha E n $gamma $beta $Ao \
                          $q $zetas $p $Shi $deltaShi $lambda $tol $maxIter

      
      `Raquib Hossain <http://scholar.google.com.au/citations?user=I_li3qkAAAAJ&hl=en&oi=ao>`__, 
      `The University of Queensland (UQ), Australia <http://www.uq.edu.au/>`__ 
      and
      `Bangladesh University of Engineering and Technology (BUET) <http://www.buet.ac.bd/>`__
   
   .. tab:: BoucWenInfill
      
      See `this <./BoucWenInfill.html>`__ page.

```


<hr />


## Theory

This material model is an extension of the
original Bouc-Wen model that includes pinching (Baber and Noori (1986) and Foliente (1995)).

$$
\begin{aligned} 
\dot{z}&=\frac{h}{\eta}\left[A-|z|^n(\gamma+\beta \operatorname{sgn}(\dot{\varepsilon} z)) \nu\right] \frac{k_0}{F_y}  \dot{\varepsilon}\\ 
\dot{e}&=(1-\alpha) F_y z \dot{\varepsilon}
\end{aligned}
$$

When parameterized with $F_y$, the additional constraint $\beta+\gamma=1$ is introduced to assure $F_y$ as the yield strength of the structure.

| Parameter | Description |
| :--- | :--- |
| $E \geq 0$ | Initial stiffness |
| $F_y$ | Yield point |
| $\alpha$ | Post-yield stiffness ratio |
| $\beta$ | Basic hysteretic shape control |
| $n$ | Sharpness of yield |

- Parameter $\gamma$ is usually in the range
  from -1 to 1 and parameter $\beta$ is usually in
  the range from 0 to 1.

- The hysteresis loop will exhibit *softening* for the following cases:

  1. $\beta + \gamma \gt 0$ and $\beta - \gamma \gt 0$, 
  2. $\beta + \gamma \gt 0$ and $\beta - \gamma \lt 0$, and 
  3. $\beta + \gamma \gt 0$ and $\beta - \gamma = 0$. 
  
- The hysteresis loop will exhibit *hardening* if $\beta + \gamma \lt 0$ and $\beta - \gamma \gt 0$, 

-  *quasi-linearity* is exhibited if $\beta + \gamma = 0$ and $\beta - \gamma \gt 0$.



```{eval-rst}
.. figure:: figures/bouc-beta.png
   :width: 50%
   :align: center
```

### Degradation

The parameters that control degradation are:

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $\delta_{\nu} \geq 0$ | Strength degradation rate | $0 \leq \delta_v \leq 0.36$ |
| $\delta_{\eta} \geq 0$ | Stiffness degradation rate | $0 \leq \delta_\eta \leq 0.39$ |


### Pinching

$$
h(z)=1-\varsigma_1(\varepsilon) \exp \left(-\frac{\left(z(t) \operatorname{sign}(\dot{u})-q z_u\right)^2}{\left(\varsigma_2(\varepsilon)\right)^2}\right)
$$

$$
\begin{aligned}
&\zeta_1(\varepsilon)=\zeta_0(1-\exp (-p \varepsilon))\\
&\zeta_2(\varepsilon)=\left(\psi+\delta_\psi \varepsilon\right)\left(\lambda+\zeta_1(\varepsilon)\right)
\end{aligned}
$$

The following parameters control pinching in the model:

| Parameter | Description | Bounds |
| :--- | :--- | :--- |
| $\zeta_0$ | Measure of total slip | $0 \leq \zeta_0 \leq 1$ |
| $p$ | Pinching slope | $0 \leq p \leq 1.38$ |
| $q$ | Pinching initiation | $0.01 \leq q \leq 0.43$ |
| $\psi$ | Pinching magnitude | $0.1 \leq \psi \leq 0.85$ |
| $\delta_\psi$ | Pinching rate | $0 \leq \delta_\psi \leq 0.09$ |
| $\lambda$ | Pinching severity | $0.01 \leq \lambda \leq 0.8$ |
| $c_{\varepsilon}$ | Hysteretic energy amplification factor | $50 \leq c_{\varepsilon} \leq 500$ |
| $c_h$ | Crack closure coefficient | $0.01 \leq c_h \leq 1.5$ |


$\delta_\nu, \delta_\psi$, and $\lambda$ are rather insensitive parameters.


## Examples

```{eval-rst}
.. ref-gallery::
   
   examples/material/material-0004
```

## References

- Kim, Taeyong, Oh‐Sung Kwon, and Junho Song. “Deep Learning Based Seismic Response Prediction of Hysteretic Systems Having Degradation and Pinching.” Earthquake Engineering & Structural Dynamics 52, no. 8 (July 2023): 2384–2406. [doi: 10.1002/eqe.3796](https://doi.org/10.1002/eqe.3796).

- Oh, Sebin, Taeyong Kim, and Junho Song. “Bouc–Wen Class Models Considering Hysteresis Mechanism of RC Columns in Nonlinear Dynamic Analysis.” International Journal of Non-Linear Mechanics 148 (January 2023): 104263. [doi: 10.1016/j.ijnonlinmec.2022.104263](https://doi.org/10.1016/j.ijnonlinmec.2022.104263).
- Oh, Sebin "Hysteresis Modeling Framework Using Bouc-Wen Model Considering Cracking Effects" [link](https://www.google.com/url?sa=i&url=https%3A%2F%2Fs-space.snu.ac.kr%2Fbitstream%2F10371%2F188999%2F1%2FMaster%2527s%2520Thesis_Sebin%2520Oh_submitted.pdf&psig=AOvVaw3cADUJYyciiRK_CJRkU770&ust=1747809408919000&source=images&cd=vfe&opi=89978449&ved=0CAYQrpoMahcKEwjw0crNt7GNAxUAAAAAHQAAAAAQBA)

- Bouc–Wen class models considering hysteresis mechanism of RC columns in nonlinear dynamic analysis [doi: 10.1016/j.ijnonlinmec.2022.104263](https://doi.org/10.1016/j.ijnonlinmec.2022.104263)

- Haukaas, T. and Der Kiureghian, A. (2003). "Finite element
  reliability and sensitivity methods for performance-based earthquake
  engineering." REER report, PEER-2003/14 <a href="https://peer.berkeley.edu/sites/default/files/0314_t._haukaas_a._der_kiureghian.pdf">link</a>.

- Baber, T. T. and Noori, M. N. (1985). "Random vibration of degrading, pinching systems." 
  Journal of Engineering Mechanics, 111(8), 1010-1026.
- Bouc, R. (1971). "Mathematical model for hysteresis." 
  Report to the Centre de Recherches Physiques, pp16-25, Marseille, France.
- Wen, Y.-K. (1976). Method for random vibration of hysteretic systems." 
  Journal of Engineering Mechanics Division, 102(EM2), 249-263.
- Baber, T. T., &amp; Noori, M. N. (1986). "Modeling general hysteresis
  behavior and random vibration application." Journal of Vibration
  Acoustics Stress and Reliability in Design, 108, 411.
- Foliente, G. C. (1995). Hysteresis modeling of wood joints and
  structural systems. Journal of Structural Engineering, 121(6), 1013-1022.

-  Hossain, M. R., Ashraf, M., &amp; Padgett, J. E. (2013). "Risk-based seismic
   performance assessment of Yielding Shear Panel Device." Engineering
   Structures, 56, 1570-1579. <a href="http://www.sciencedirect.com/science/article/pii/S0141029613003568">doi</a>

-  Hossain, M. R., &amp; Ashraf, M. (2012). "Mathematical modelling of yielding
   shear panel device." Thin-Walled Structures, 59, 153-161. <a href="http://www.sciencedirect.com/science/article/pii/S0263823112001206">doi</a>


<hr />

