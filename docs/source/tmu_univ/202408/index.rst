===============================================
夏季試験(2024年8月)
===============================================

問題は以下である。

* 数学・物理学 I (3問,135分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Scover_new_FV_tot.pdf
* 物理学 II (2問,100分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Scover_new_FV_totdown.pdf


準備
===============================================

正則関数
------------------------------------

複素関数のイメージ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

実数値の関数と異なり、複素変数の複素数値関数はグラフ上に表すことはできない。
しかし :math:`z` 平面上の特定の図形や集合が :math:`w` 平面上でどのような図形となるかを
調べることで、関数についてうかがい知ることができる。

次の関数（変換）を考える。

.. math::
    w = z + \frac{1}{z}

そして :math:`z` 平面上で半径1の円、半径 :math:`r` の円、および :math:`x` 軸上の線分が、
それぞれ :math:`w` 平面上のどの位置に移るかを考える。

まず、 :math:`x` 軸上の線分について考える。
:math:`z` 平面上の :math:`x` 軸上の点 (1, 0) を考える。
これは :math:`z = 1` なので :math:`w` は :math:`w = 1 + \frac{1}{1} = 2` となる。
なので、:math:`w` 平面上では点 (2, 0) に移ることとなる。

次に :math:`x` 軸上で :math:`x > 1` の半直線を考える。
このとき :math:`z = x` なので :math:`w = x + \frac{1}{x}` に移る。
:math:`x > 1` を考えているので :math:`w > 2` である。
微分すると :math:`\frac{dw}{dx} = 1 - \frac{1}{x^2} > 0 (x > 1)` なので、
:math:`z` 平面上で :math:`x` が大きくなる方向へ移動すると、
:math:`w` 平面上でも :math:`u` が大きくなる方向へ移動する。

次に半径1の半円を考える。
半径1の円は :math:`z = e^{i \theta}, (0 \leq \theta \leq \pi)` と表せる。
なので :math:`w = e^{i \theta} + e^{-i \theta} = 2 \cos \theta` となり、
取りうる値の範囲は :math:`-2 \leq w(= 2 \cos \theta) \leq 2` である。
したがって、 :math:`z` 平面上での半円は :math:`w` 平面上では :math:`x` 軸上の線分に移る。
:math:`z` 平面上で :math:`\theta` が 0 のとき :math:`w` 平面上では :math:`x` が最大となり、
:math:`\theta` が大きくなるにつれて :math:`x` は小さくなる方向に移動していく。

最後に半径 :math:`r_0` の半円がどのように移るかを考える。
この半円は :math:`z = r_0 e^{i \theta}` と表せるので、
:math:`w = r_0 e^{i \theta} + \frac{1}{r_0 e^{i \theta}}` となる。
これは次のように変形できる。

.. math::
    w &= r_0 e^{i \theta} + r_0^{-1} e^{-i \theta} \\
      &= (r_0 + r_0^{-1}) \cos \theta + i(r_0 - r_0^{-1}) \sin \theta \\
      &= a \cos \theta + i b \sin \theta, a = r_0 + r_0^{-1}, b = r_0 - r_0^{-1} \\
    (\frac{u}{a})^2 + (\frac{v}{b})^2 = 1

これは焦点が :math:`w = \pm \sqrt{a^2 - b^2} = \pm 2` の楕円である。


:math:`\epsilon - \delta` 論法
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

（TBD）


コーシー・リーマンの方程式
------------------------------------

関数

.. math::
    f(z) = u(x, y) + i v(x, y)

が :math:`z_0 = x_0 + i y_0` で微分可能、つまり、極限

.. math::
    f'(z_0) = \lim_{\varDelta z \to 0} \frac{f(z_0 + \varDelta z) - f(z_0)}{\varDelta z}

が存在すると仮定するとき、 :math:`f'(z_0)` が :math:`u` と :math:`v` の偏導関数で

.. math::
    f'(z_0) = u_x (x_0, y_0) + i v_x (x_0, y_0) \\
    f'(z_0) = v_y (x_0, y_0) - i u_y (x_0, y_0)

と表される。そして、次の **コーシー・リーマンの方程式** を満たす。

.. math::
    u_x (x_0, y_0) = v_y (x_0, y_0) \\
    u_y (x_0, y_0) = -v_x (x_0, y_0)

コーシー・リーマンの方程式の一つ目の式を次のとおり導出する。

極限の式が成り立つとき、複素関数の極限は実部と虚部それぞれで極限をとったものに等しいから、

.. math::
    \text{Re} f'(z_0) = \lim_{(\varDelta x, \varDelta y) \to (0, 0)} \text{Re} \frac{f(z_0 + \varDelta z) - f(z_0)}{\varDelta z} \\
    \text{Im} f'(z_0) = \lim_{(\varDelta x, \varDelta y) \to (0, 0)} \text{Im} \frac{f(z_0 + \varDelta z) - f(z_0)}{\varDelta z}

が成り立つ。

また、次のように計算できる。

.. math::
    \frac{f(z_0 + \varDelta z) - f(z_0)}{\varDelta z}
    = \frac{\{u(x_0 + \varDelta x, y_0 + \varDelta y) - u(x_0, y_0)\} + i \{v(x_0 + \varDelta x, y_0 + \varDelta y) - v(x_0, y_0)\}}
    {\varDelta x + i \varDelta y}


いま、極限 :math:`f'(z_0)` が存在すると仮定すると、
いかなる向きから0に近づけても常に一つの値が定まり、それが :math:`f'(z_0)` なので、
上式の :math:`(\varDelta x, \varDelta y) \to (0, 0)` としても常に一つの値が定まる（経路に依らない）。

よって、 :math:`\varDelta y = 0` としてもよいので、上式は次のようになる。

.. math::
    \frac{f(z_0 + \varDelta z) - f(z_0)}{\varDelta z}
    = \frac{u(x_0 + \varDelta x, y_0) - u(x_0, y_0)}{\varDelta x}
    + i \frac{v(x_0 + \varDelta x, y_0) - v(x_0, y_0)}{\varDelta x} \\
    = u_x(x_0, y_0) + i v_x(x_0, y_0)

同様に :math:`\varDelta x = 0` と置くことで、二つ目の式も導くことができる。


複素積分
------------------------------------



