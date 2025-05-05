===============================================
夏季試験(2024年8月)
===============================================

問題は以下である。

* 数学・物理学 I (3問,135分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Scover_new_FV_tot.pdf
* 物理学 II (2問,100分): https://www.phys.se.tmu.ac.jp/wp-content/uploads/2025/02/2025Scover_new_FV_totdown.pdf


準備
===============================================

複素関数のイメージ
------------------------------------

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

.. hint:: 楕円の式
    
    楕円とは、2定点からの距離の和が一定となるような平面上の点の軌跡である。
    この定点のことを焦点という。
    楕円の中心を原点としたデカルト座標 :math:`X, Y` では楕円は次のように表される。

    .. math::
        \frac{X^2}{a^2} + \frac{Y^2}{b^2} = 1
    
    これは以下のようにして導かれる。
    まず、2つの焦点を :math:`X` 軸上におき、:math:`F(c, 0), F'(-c, 0) \quad c > 0` とする。
    点 :math:`P` の座標を :math:`(X, Y)` とすると

    .. math::
        PF + PF' &= const. = 2a \\
        \sqrt{(X -c)^2 + Y^2} + \sqrt{(X + c)^2 + Y^2} &= 2a \\
        (X + c)^2 + Y^2 &= \{2a - \sqrt{(X + c)^2 + Y^2}\}^2 \\
        &= 4a^2 -4a \sqrt{(X + c)^2 + Y^2} + (X + c)^2 + Y^2 \\
        \sqrt{(X - c)^2 + Y^2} &= a - \frac{c}{a} X \\
        (X - c)^2 + Y^2 &= a^2 -2cX + \frac{c^2}{a^2} X^2 \\
        (1 - \frac{c^2}{a^2}) X^2 + Y^2 &= a^2 - c^2 \\
        \frac{X^2}{a^2} + \frac{Y^2}{a^2 - c^2} &= 1
    
    ここで :math:`b^2 = a^2 - c^2` とおけば

    .. math::
        \frac{X^2}{a^2} + \frac{Y^2}{b^2} = 1
    
    を得る。


.. hint:: :math:`\epsilon - \delta` 論法

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
    &= \frac{u(x_0 + \varDelta x, y_0) - u(x_0, y_0)}{\varDelta x}
    + i \frac{v(x_0 + \varDelta x, y_0) - v(x_0, y_0)}{\varDelta x} \\
    &= u_x(x_0, y_0) + i v_x(x_0, y_0)

同様に :math:`\varDelta x = 0` と置くことで、二つ目の式も導くことができる。

極形式のコーシー・リーマンの方程式は次のように表される。

.. math::
    u_r = \frac{1}{r} v_\theta, \quad \frac{1}{r} u_\theta = - v_r


.. hint:: 合成関数の微分

    はじめに1変数関数の連鎖律を見る。
    :math:`z = f(x, y)` が全微分可能で :math:`x = x(t), y = y(t)` が微分可能であるとき、
    合成関数 :math:`z = f(x(t), y(t))` は :math:`t` の関数として微分可能で次が成り立つ。

    .. math::
        \frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}

    2変数関数も同様に考えることができる。 :math:`z = f(x, y), x = x(u, v), y = y(u, v)` のとき、
    
    .. math::
        \frac{\partial z}{\partial u} &= \frac{\partial f}{\partial x} \frac{\partial x}{\partial u}
        + \frac{\partial f}{\partial y} \frac{\partial y}{\partial u} \\
        \frac{\partial z}{\partial v} &= \frac{\partial f}{\partial x} \frac{\partial x}{\partial v}
        + \frac{\partial f}{\partial y} \frac{\partial y}{\partial v}

    （参考）https://www2.math.kyushu-u.ac.jp/~hara/lectures/12/biseki1213b.pdf

正則関数
------------------------------------

点 :math:`z_0` のみならず :math:`z_0` のある近傍の各点において :math:`f(z)` が **微分可能** であるとき、
:math:`f(z)` は :math:`z_0` で **正則** であるという。


.. note:: 内点、外点、境界と開集合、閉集合

    * 点 :math:`z_0` を中心として半径 :math:`\varepsilon` の円の内部の点全体 :math:`|z - z_0| < \varepsilon` を :math:`z_0` の :math:`\varepsilon` 近傍という。
    * 点 :math:`z_0` のある近傍が集合 :math:`S` の点のみを含むとき、 :math:`z_0` は :math:`S` の **内点** という。
    * 点 :math:`z_0` の近傍で :math:`S` の点を含まないものがある場合、 :math:`z_0` を :math:`S` の **外点** という。
    * 点 :math:`z_0` が :math:`S` の内点でも外点でもない場合、 :math:`z_0` は :math:`S` の **境界点** という。
    * :math:`S` の境界点全体を :math:`S` の **境界** という。

    .. image:: ./images/interior-summary.png
        :scale: 30%
        :align: center

    * 境界点を含まない集合を **開集合** という。
    * 境界点をすべて含む集合を **閉集合** という。


複素積分
------------------------------------

複素数 :math:`z` の複素数値関数 :math:`f(z)` の積分について考える。
積分路を表す曲線 :math:`C` を次の関数で定める。

.. math::
    C: z(t) = x(t) + i y(t) \quad (a \leq t \leq b)

このとき、:math:`C` に沿う :math:`f(z)` の線積分を次で定義する。

.. math::
    \int_C f(z) dz &= \int_a^b f(z(t)) z'(t) dt \\
    z'(t) dt &= \frac{dz}{dt} dt = dz

上式の右辺は次のように展開できる。

.. math::
    \text{右辺} &= \int_a^b (u + iv)(x' + iy') dt \\
    &= \int_a^b (ux' - vy') dt + i \int_a^b (vx' + uy') dt \\
    &= \int_C udx - vdy + i \int_C vdx + udy = \int_C f(z) dz

これは :math:`f(z) = u + iv, dz = dx + idy` とおいて、
形式的な計算を行ったものと同じ形をしている。

次の例を考える。
:math:`C_1` が2点 :math:`z=0` と :math:`z=2+i` を結ぶ線分であるとき、
積分 :math:`I_1 = \int_{C_1} z^2 dz` の値を求める。

:math:`C_1` は直線 :math:`y = x/2` 上にあるから、 :math:`y = t` とおくと
:math:`x = 2t` だから

.. math::
    C_1: z &= z(t) = 2t + it \quad (0 \leq t \leq 1) \\
    z'(t) &= 2 + i

:math:`C_1` 上における :math:`z^2` の値は

.. math::
    z^2 &= (x + iy)^2 = (2t + it)^2 = (2 + i)^2 t^2 = (3 + 4i) t^2 \\
    I_1 &= \int_0^1 (3 + 4i) t^2 (2 + i) dt = (3 + 4i) (2 + i) \int_0^1 t^2 dt \\
        &= \frac{2}{3} + \frac{11}{3} i

コーシーの積分定理
------------------------------------

.. hint:: グリーンの定理

    :math:`xy` 平面で単一閉曲線（ジョルダン曲線） :math:`C` で囲まれた領域を :math:`R` とする。
    二つの関数 :math:`M(x, y), N(x, y)` が :math:`C` と :math:`R` を含む領域で連続な偏導関数
    をもっているとする。また、閉曲線 :math:`C` には図のような向きがついているとする。
    このとき次の等式が成り立つ。

    .. math::
        \int_C (M dx + N dy) = \int \int_R (\frac{\partial N}{\partial x} - \frac{\partial M}{\partial y}) dx dy
    
    .. image:: ./images/green_theorem.png
        :scale: 60%
        :align: center

    次のように示すことができる。
    まず、閉曲線 :math:`C` を二つの部分 :math:`C_1, C_2` に分け、
    これらの曲線（弧）の方程式をそれぞれ :math:`y = Y_1(x), \quad y =Y_2(x)` とする。
    まず次の計算をする。

    .. math::
        \int \int_R \frac{\partial M}{\partial y} dx dy &= \int_a^b \int_{Y_1(x)}^{Y_2(x)} \frac{\partial M}{\partial y} dy dx \\
        &= \int_a^b [M(x, y)]_{y = Y_1(x)}^{y = Y_2(x)} dx \\
        &= \int_a^b M(x, Y_2(x)) dx - \int_a^b M(x, Y_1(x)) dx \\
        &= - \int_{BFA} M dx - \int_{AEB} M dx \\
        &= \int_C M dx
    
    同様にして、:math:`\int \int_R \frac{\partial N}{\partial x} dx dy = \int_C N dy` となる。
    それぞれ足し合わせることでグリーンの定理の式となる。

:math:`R` 全体で正則な関数 :math:`f(z) = u(x, y) + iv(x, y)` に対する :math:`C` に沿う線積分は、次式となる。

.. math::
    \int_C f(z) dz = \int_C udx - vdy + i \int_C vdx + udy

これは :math:`dz = dx + idy` と形式的に計算することで得られる。
:math:`f(z)` が :math:`R` で連続ならば :math:`u, v` は :math:`R` で連続であり、
また、:math:`f'(z)` が :math:`R` で連続ならば :math:`u, v` の1階偏導関数は連続である。
よって、グリーンの定理を使用することができ、上式は次のようになる。

.. math::
    \int_C f(z) dz = \int \int_R (-v_x - u_y) dx dy + i \int \int_R (u_x - v_y) dx dy

ところで、 :math:`f(z)` は正則なので、コーシー・リーマンの方程式 :math:`u_x = v_y, u_y = -v_x` が成り立つので、
右辺の値は 0 となる。

したがって、次の重要な定理 コーシーの積分定理 を得る。

区分的に滑らかなジョルダン曲線 :math:`C` の上と内部で

.. math::
    f(z) \text{ が正則}, f'(z) \text{ が連続ならば }
    \int_C f(z) dz = 0

:math:`f(z)` が正則でなければコーシー・リーマンの定理が成り立たず、
また、:math:`f'(z)` が連続でなければグリーンの定理が成り立たないので、
いずれも必要である。

:math:`\int_C f(z) dz = 0` であるとき :math:`\int_{-C} f(z) dz = - \int_C f(z) = 0` であるから、
コーシーの積分定理における :math:`C` の向きは本質的ではなくなる。
すなわち、正の向きでも負の向きでも無関係に積分の値は 0 である。




