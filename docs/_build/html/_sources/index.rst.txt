Bienvenido a la documentación de Campo Estático MDF
===================================================

.. image:: /_static/INDEX/INDEX.png
   :alt: Solver
   :align: center
   :width: 90%


.. toctree::
   :maxdepth: 2
   :caption: Contenidos:

   api
   tests
   GUI
   instalacion

Introducción Teórica
====================

Ecuación de Laplace
-------------------

La distribución del potencial eléctrico :math:`V` en una región sin cargas se describe por:

.. math::

   \nabla^2 V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} = 0

Método de Diferencias Finitas (MDF)
-----------------------------------

Para resolver esta ecuación numéricamente, discretizamos el dominio en una malla.

La segunda derivada puede aproximarse como:

.. math::

   \frac{\partial^2 V}{\partial x^2} \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{h^2}

Aplicando esta aproximación para ambas derivadas, obtenemos:

.. math::

   V_{i,j} = \frac{1}{4}\left( V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1} \right)

Algoritmo de Gauss-Seidel
-------------------------

Este método iterativo actualiza el valor del potencial en cada nodo usando los valores
más recientes disponibles hasta alcanzar una tolerancia deseada.

