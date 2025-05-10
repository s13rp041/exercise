=======================================
解析力学
=======================================


ばねの運動
=======================================

次のばねとおもりの運動を考える。

---------------------------------------

天井からつるされたばね定数 :math:`k` の先に質量 :math:`m` のおもりをつける。
おもりのついていないときのばねの自然長を :math:`l` とし、ばね自体の質量は考えないとする。
天井から垂直下向きを :math:`x` 軸の正の方向とし、おもりを初期位置 :math:`x = l` 、
初速度ゼロで手を離したとする。手を離した時刻を :math:`t = 0` とし、その後の単振動の
振幅と初期位相、および振動数を求めることを考える。

---------------------------------------

天井の位置を :math:`x = 0` とし、時刻 :math:`t` での運動しているおもりの位置を :math:`x(t)` とする。
このときばねの伸びは :math:`x(t) - l` であるから、運動方程式は次のようになる。

.. math::
    m \frac{d^2x}{dt^2} &= mg -k(x - l) \\
    &= -kx + kl + mg \\
    &= -k(x - l - \frac{mg}{k}) \\
    m \frac{d^2}{dt^2} (x - l -\frac{mg}{k}) &= -k(x - l - \frac{mg}{k}) \\
    m \ddot{X} &= -kX

ここで :math:`X(t) = x(t) - l - \frac{mg}{k}` とおいた。
すると

.. math::
    \ddot{X} = - \frac{k}{m} X = - \omega^2 X \quad (\omega = \sqrt{\frac{k}{m}} とした)

:math:`X(t) = \sin \omega t, X(t) = \cos \omega t` は上式を満たすから、
この微分方程式の特解である。よって、これらの線形結合も解（一般解）であるから、

.. math::
    X(t) = A \sin \omega t + B \cos \omega t = C \cos (\omega t + \phi)

とおける。但し、 :math:`0 \leq \phi < 2 \pi` とする。

初期位置 :math:`x = l` から、 :math:`x(0) = l` であるので、
:math:`X(0) = x(0) - l - \frac{mg}{k} = - \frac{mg}{k}` となる。
また、初速度ゼロであるから :math:`\dot{x(0)} = 0` なので、
:math:`\dot{X(0)} = \dot{x(0)} = 0` より、

.. math::
    X(0) &= B = C \cos(\phi) = - \frac{mg}{k} \\
    \dot{X(0)} &= \omega A = - \omega C \sin (\phi) = 0

となる。下の式から :math:`A = 0` であり、 :math:`\phi = 0, \pi` である。

:math:`\phi = 0` のとき、 :math:`\cos \phi = 1` であるから :math:`X(0) = B = C = - \frac{mg}{k}` となる。
よって、

.. math::
    X(t) &= - \frac{mg}{k} \cos (\omega t) \\
    x(t) - l - \frac{mg}{k} &= - \frac{mg}{k} \cos (\omega t) \\
    \therefore x(t) &= l + \frac{mg}{k} - \frac{mg}{k} \cos (\omega t)

となる。 :math:`\phi = \pi` のときは、 :math:`\cos \phi = -1` であるから
:math:`X(0) = B = -C = - \frac{mg}{k}` となるので、

.. math::
    X(t) &= \frac{mg}{k} \cos (\omega t + \pi) \\
    \therefore x(t) &= l + \frac{mg}{k} + \frac{mg}{k} \cos (\omega t + \pi)

