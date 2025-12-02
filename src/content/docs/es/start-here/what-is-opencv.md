---
title: ¿Qué es OpenCV?
description: Una visión general de OpenCV y su papel en proyectos de visión por computadora.
---

OpenCV es una librería de código abierto para visión por computadora y procesamiento de imágenes.

<img src="/assets/opencv_logo.svg" alt="OpenCV Logo" class="dark:sl-hidden" />
<img src="/assets/opencv_logo_white.svg" alt="OpenCV Logo" class="light:sl-hidden" />

En esta página, explicamos brevemente:

- **Idea central**: manipulación de imágenes, video y entrada de cámara.
- **Tareas típicas**: filtrado, detección de bordes, detección de objetos, extracción de características, etc.
- **Por qué nos enfocamos** únicamente en la API de **Python** en esta documentación no oficial.

Mantén el tono introductorio y motivador. El objetivo es motivar al lector, no listar cada característica.

## Ejemplo básico

Aquí tienes un ejemplo simple de cómo OpenCV puede cargar y mostrar una imagen:

```python
import cv2

# Cargar una imagen desde disco
img = cv2.imread("imagen.jpg")

# Verificar que la imagen se cargó correctamente
if img is not None:
    # Mostrar la imagen en una ventana
    cv2.imshow("Mi Imagen", img)
    
    # Esperar a que el usuario presione una tecla
    cv2.waitKey(0)
    
    # Cerrar todas las ventanas
    cv2.destroyAllWindows()
else:
    print("Error: No se pudo cargar la imagen")
```

Este ejemplo básico demuestra una de las operaciones más comunes: cargar y visualizar una imagen. OpenCV ofrece muchas más capacidades para procesar y analizar imágenes.
