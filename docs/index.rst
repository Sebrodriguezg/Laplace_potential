.. Campo Estatico MDF documentation master file, created by
   sphinx-quickstart on Tue Nov 12 10:18:10 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

¡Bienvenido a la documentación de Campo Estatico MDF!
===================================================

Este proyecto proporciona una solución para calcular y visualizar el campo electrostático en 2D utilizando el Método de Diferencias Finitas.

.. toctree::
   :maxdepth: 2
   :caption: Contenidos:

Introducción Teórica
--------------------

### Ecuación de Laplace

La distribución del potencial eléctrico :math:`V` en una región sin cargas se describe por la Ecuación de Laplace:

.. math::

   \\nabla^2 V = \\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2} = 0

### Método de Diferencias Finitas (MDF)

Para resolver esta ecuación numéricamente, discretizamos el dominio en una malla. La segunda derivada se puede aproximar como:

.. math::

   \\frac{\\partial^2 V}{\\partial x^2} \\approx \\frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{h^2}

Aplicando esta aproximación para ambas derivadas (x e y) y sustituyendo en la ecuación de Laplace, obtenemos que el potencial en un punto es el promedio de sus cuatro vecinos más cercanos:

.. math::

   V_{i,j} = \\frac{1}{4} (V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1})

### Algoritmo de Gauss-Seidel

Este es un método iterativo para resolver el sistema de ecuaciones lineales resultante. En cada iteración, se actualiza el valor de cada punto de la malla usando los valores más recientes de sus vecinos. El proceso se repite hasta que la diferencia máxima entre el potencial actual y el anterior es menor que una tolerancia definida.

Referencia de la API
--------------------

Aquí se documenta la clase principal del backend.

.. automodule:: campo_estatico_mdf.solver
   :members:
   :undoc-members:
   :show-inheritance:

Índices y tablas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
