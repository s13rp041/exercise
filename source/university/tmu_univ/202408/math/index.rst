===============================================
数学
===============================================


問1
===============================================

オイラーの公式から次が成り立つ。

.. math::
    e^{i \theta} = \cos \theta + i \sin \theta , \quad e^{-i \theta} = \cos \theta - i \sin \theta \\

    \therefore \cos \theta &= \frac{e^{i \theta} + e^{-i \theta}}{2} = \frac{z + z^{^-1}}{2} \\
    \therefore \sin \theta &= \frac{e^{i \theta} - e^{-i \theta}}{2} = \frac{z - z^{^-1}}{2}


問2
===============================================

:math:`z = e^{i \theta}` であるから :math:`dz = i e^{i \theta} d \theta = iz d \theta` となる。
よって、与えられた式は次のように変形できる。

.. math::
    \int_0^{2 \pi} \frac{e^{i 3 \theta}}{2 - \sin \theta} d \theta &= \int_C \frac{z^3}{2 - \frac{1}{2i} (z - \frac{1}{z})} \frac{dz}{iz} \\
    &= \int_C \frac{-2 z^3}{z^2 - 4iz - 1} dz

したがって、 :math:`f(z)` は以下となる。

.. math::
    f(z) = \int_C \frac{-2 z^3}{z^2 - 4iz - 1} dz


問3
===============================================

問2 の結果から、 :math:`f(z)` の分母は次のように変形できる。

.. math::
    z^2 - 4iz -1 = (z - 2i)^2 + 3

いま :math:`C` は :math:`|z|^2 = 1` で定義される閉曲線であるから、
この中に含まれる :math:`f(z)` の極は :math:`z = i(2 - \sqrt 3)` のみである（これは1位の極）。


問4
===============================================

:math:`\sin 3 \theta = \frac{e^{i 3 \theta} - e^{-i 3 \theta}}{2i} = \frac{z^3 - z^{-3}}{2i}` であるから、
与えられた式は次のように変形できる。

.. math::
    \int_0^{2 \pi} \frac{\sin 3 \theta}{2 - \sin \theta} d \theta 
    &= \frac{1}{2i} \int_0^{2 \pi} \frac{e^{i 3 \theta} + e^{-i 3 \theta}}{2 - \sin \theta} d \theta \\
    &= \frac{1}{2i} \{ \int_0^{2 \pi} \frac{e^{i 3 \theta}}{2 - \sin \theta} d \theta - \int_0^{2 \pi} \frac{e^{-i 3 \theta}}{2 - \sin \theta} d \theta \} \\
    &\triangleq \frac{1}{2i} \{ \int_C f_1(z) dz - \int_C f_2(z) dz \}

右辺の第一項は問2で計算した結果が利用できる。第二項も同様にして次のように計算できる。

.. math::
    \int_C f_2(z) dz &= \int_0^{2 \pi} \frac{e^{-i 3 \theta}}{2 - \sin \theta} d \theta
    = \int_C \frac{-2 z^{-3}}{z^2 -4iz - 1} dz \\
    &= \int_C \frac{-2}{z^3 (z^2 -4iz - 1)} dz

よって、 :math:`f_2(z)` は :math:`C` の中に :math:`z = 0` に3位の極、:math:`z = i(2 - \sqrt 3)` に1位の極を持つ。

以上の結果から、留数定理を用いて与えられた積分を求める。
留数定理によると次の式が成り立つ。

.. math::
    \int_C f_1(z) dz &= 2 \pi i (Res(z = i(2 - \sqrt 3))) \\
    \int_C f_2(z) dz &= 2 \pi i (Res(z = 0) + Res(z = i(2 - \sqrt 3))) \\

但し :math:`Res(z = z_0)` は :math:`z = z_0` での留数を表す。
:math:`f_1(z)` は1位の極であるから、

