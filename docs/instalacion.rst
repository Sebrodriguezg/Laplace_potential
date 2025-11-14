Instalación
===========

Este documento describe los métodos recomendados para instalar la librería
``campo_estatico_mdf-DS``, un paquete en Python para resolver el campo electrostático
bidimensional mediante el Método de Diferencias Finitas (MDF).

Requisitos previos
------------------

Antes de instalar el paquete, asegúrese de contar con:

- Python 3.8 o superior.
- pip actualizado:

  .. code-block:: bash

     python3 -m pip install --upgrade pip

Dependencias del paquete
------------------------

El paquete requiere las siguientes librerías, las cuales se instalarán
automáticamente:

- numpy
- scipy
- matplotlib
- pytest

Estas dependencias están definidas en el archivo ``pyproject.toml``.

Instalación desde PyPI
----------------------

Cuando el paquete esté publicado en PyPI, se podrá instalar directamente con:

.. code-block:: bash

   pip install campo_estatico_mdf-DS

Instalación desde GitHub
------------------------

Si desea instalar la última versión disponible directamente desde el repositorio:

.. code-block:: bash

   pip install git+https://github.com/USUARIO/REPO.git

Reemplace ``USUARIO`` y ``REPO`` por los valores correspondientes a su proyecto.

Instalación desde el código fuente
----------------------------------

Si ha descargado o clonado el repositorio de manera local:

1. Entre al directorio raíz del proyecto:

   .. code-block:: bash

      cd campo_estatico_mdf-DS

2. Instale el paquete utilizando ``pip``:

   .. code-block:: bash

      pip install .

   También puede instalarse en modo editable durante el desarrollo:

   .. code-block:: bash

      pip install -e .

Verificación de instalación
---------------------------

Para verificar que la instalación fue exitosa, abra una terminal o consola Python y ejecute:

.. code-block:: python

   import campo_estatico_mdf
   print("Paquete cargado correctamente. Versión:", campo_estatico_mdf.__version__)

Si no aparece ningún error, la instalación se realizó correctamente.

Estructura del proyecto
-----------------------

La configuración del paquete se encuentra definida en el archivo
``pyproject.toml`` e incluye:

- Sistema de compilación: ``setuptools>=61.0``.
- Nombre del proyecto: ``campo_estatico_mdf-DS``.
- Versión: ``0.1.0``.
- Autores y metadatos.
- Dependencias requeridas.
- Paquetes incluidos (``campo_estatico_mdf``).
- Descripción y archivo ``README.md`` asociado.

Esto garantiza que la instalación mediante ``pip`` funcione de manera estándar
en cualquier entorno compatible con Python 3.8 o superior.

