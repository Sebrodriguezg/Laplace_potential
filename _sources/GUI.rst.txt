====================================
Interfaz Gráfica (Streamlit)
====================================

Este módulo proporciona una interfaz gráfica desarrollada con 
**Streamlit** para interactuar con el solucionador numérico de la 
ecuación de Laplace. Permite modificar parámetros, visualizar los 
resultados y ejecutar simulaciones sin necesidad de escribir código.

.. contents::
   :local:
   :depth: 2

Descripción General
====================

La interfaz ofrece:

- Configuración del tamaño de la malla.
- Selección de tolerancia de convergencia.
- Ajuste de voltajes en cada frontera.
- Ejecución del método de Gauss–Seidel.
- Visualización del mapa de potencial.
- Gráfica del campo eléctrico.
- Evolución del error de convergencia.

Pantalla de Inicio
====================

A continuación se muestra la pantalla principal de la aplicación, donde 
el usuario ingresa los parámetros de la simulación.

.. image:: /_static/gui/inicio.png
   :alt: Pantalla de inicio del solucionador 2D
   :align: center
   :width: 90%

Resultados de la Simulación
=============================

Mapa de Potencial y Campo Eléctrico
------------------------------------

Una vez ejecutado el método iterativo, se presentan dos visualizaciones:

1. El mapa de potencial eléctrico V(x,y).
2. El campo eléctrico obtenido mediante gradiente numérico.

.. image:: /_static/gui/resultados_potencial.png
   :alt: Resultados: potencial y campo eléctrico
   :align: center
   :width: 95%

Evolución del Error
--------------------

También se grafica el error máximo por iteración, útil para analizar la 
convergencia del método.

.. image:: /_static/gui/resultados_error.png
   :alt: Error de convergencia por iteración
   :align: center
   :width: 90%

Ejecución desde la Terminal
=============================

La interfaz puede ejecutarse desde la raíz del proyecto:

.. code-block:: bash

   streamlit run app.py

Esto inicia un servidor local accesible usualmente en:

::

   http://localhost:8501

Integración con el Solucionador
===============================

La interfaz hace uso del módulo:

``campo_estatico_mdf.solver.LaplaceSolver2D``

El cual resuelve la ecuación de Laplace mediante Gauss–Seidel y calcula el 
campo eléctrico derivado del potencial.

``GUI.rst`` está diseñado para complementar la documentación del API e 
ilustrar su uso práctico.

Ejecutar la Aplicación desde la Documentación
==============================================

La documentación puede consultarse en diferentes contextos (local o en línea).  
A continuación se explica cómo ejecutar la interfaz gráfica según el caso.

.. note::

   GitHub Pages y otros hospedajes estáticos **no permiten ejecutar Streamlit**.  
   Solo es posible iniciar la aplicación en un entorno local o en un servicio
   de despliegue interactivo como *Streamlit Community Cloud*.

Ejecución Local (recomendada)
------------------------------

Si has clonado el repositorio e instalado las dependencias, puedes iniciar la
interfaz directamente con:

.. code-block:: bash

   streamlit run app.py

Una vez iniciada, puedes abrir el siguiente enlace en tu navegador:

`Abrir aplicación local <http://localhost:8501>`_

