---
title: Comenzando con OpenCV
description: Configura tu entorno e instala OpenCV para comenzar a trabajar con imágenes.
---

En esta guía podrás:

- Instalar Python y crear un entorno virtual.
- Instalar OpenCV para Python (`opencv-python`).
- Verificar que todo funciona cargando y mostrando una imagen sencilla.

## Requisitos previos

- Conocimientos básicos de Python.
- Una versión reciente de Python (se recomienda 3.10+).

## Crear un entorno virtual

Primero, crea un entorno virtual para aislar las dependencias de tu proyecto:

```bash
# Crear un entorno virtual
python3 -m venv opencv-env

# Activar el entorno virtual
# En macOS/Linux:
source opencv-env/bin/activate

# En Windows:
# opencv-env\Scripts\activate
```

## Instalar OpenCV

Una vez activado el entorno virtual, instala OpenCV:

```bash
pip install opencv-python
```

## Verificar la instalación

Crea un archivo `test_opencv.py` con el siguiente código:

```python
import cv2
import numpy as np

# Verificar la versión de OpenCV
print(f"OpenCV versión: {cv2.__version__}")

# Crear una imagen simple para probar
# Crear una imagen negra de 200x200 píxeles
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Dibujar un círculo blanco en el centro
cv2.circle(img, (100, 100), 50, (255, 255, 255), -1)

# Mostrar la imagen
cv2.imshow("Test OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("¡OpenCV está funcionando correctamente!")
```

Ejecuta el script:

```bash
python test_opencv.py
```

Si ves una ventana con un círculo blanco y el mensaje de confirmación, ¡todo está funcionando!

## Pasos siguientes

Una vez que tu entorno esté listo, continúa con la página de **Instalación** para más detalles o ve a **¿Qué es OpenCV?** para entender la librería a un nivel general.
