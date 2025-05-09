===============================================
冬季試験(2025年2月)
===============================================

問題は以下である。

* 数学・物理学 I (3問,135分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Wcover_mpI_rev.pdf
* 物理学 II (2問,50分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Wcover_pII_rev.pdf


数学
===============================================

問1
-----------------------------------------------

TBD


問2
-----------------------------------------------

TBD


問3
-----------------------------------------------

:math:`u = \tan (x/2)` と置くことから、 :math:`\sin x` についても :math:`u` で表せるとよい。
:math:`\sin x` を次のように変形する。

.. math::
    \sin x = \sin 2 \frac{x}{2} &= \sin {\frac{x}{2}} \cos {\frac{x}{2}} + \cos {\frac{x}{2}} \sin {\frac{x}{2}} \\
    &= 2 \sin {\frac{x}{2}} \cos {\frac{x}{2}} \\
    &= 2 \frac{\sin {\frac{x}{2}}}{\cos {\frac{x}{2}}} \cos^2 {\frac{x}{2}} \\
    &= 2 \tan {\frac{x}{2}} \frac{1}{1 + \tan^2 {\frac{x}{2}}} \\
    &= 2 u \frac{1}{1 + u^2} \\
    &= \frac{2u}{1 + u^2}

次に微分を求める。 :math:`u = \tan {\frac{x}{2}}` より

.. math::
    du &= \frac{1}{\cos^2 {\frac{x}{2}}} \frac{1}{2} dx \\
    \therefore dx &= 2 \cos^2 {\frac{x}{2}} du = 2 \frac{1}{1 + u^2} du \quad (\because 1 + \tan^2 x = \frac{1}{\cos^2 x})

よって、与えられた式は次のように表される。

.. math::
    \int \frac{dx}{\sin x} &= \int \frac{1 + u^2}{2u} 2 \frac{1}{1 + u^2} du \\
    &= \int \frac{du}{u} \\
    &= \log |u| + C \quad (C は積分定数) \\
    &= \log |\tan \frac{x}{2}| + C


