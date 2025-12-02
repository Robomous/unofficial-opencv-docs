---
title: Preprocesamiento de Imágenes
description: Aprende los pasos básicos de preprocesamiento que reutilizarás en la mayoría de tus flujos de trabajo con OpenCV.
---

El preprocesamiento de imágenes generalmente incluye:

- **Lectura de imágenes** desde disco.
- **Conversión de espacios de color** (por ejemplo, BGR a escala de grises).
- **Cambio de tamaño** de imágenes a una resolución consistente.
- **Aplicación de filtros simples** (desenfoque, umbralización, etc.).

## Ejemplo completo de preprocesamiento

Aquí tienes un ejemplo completo que muestra los pasos básicos:

```python
import cv2
import numpy as np

# 1. Leer una imagen desde disco
img = cv2.imread("imagen_original.jpg")

# Verificar que la imagen se cargó correctamente
if img is None:
    print("Error: No se pudo cargar la imagen")
    exit()

print(f"Imagen original: {img.shape}")  # (alto, ancho, canales)

# 2. Convertir de BGR a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Escala de grises: {gray.shape}")  # (alto, ancho)

# 3. Redimensionar la imagen a un tamaño consistente
target_size = (640, 480)  # (ancho, alto)
resized = cv2.resize(gray, target_size)
print(f"Redimensionada: {resized.shape}")

# 4. Aplicar un filtro de desenfoque (blur)
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

# 5. Aplicar umbralización (threshold)
_, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# 6. Guardar la imagen procesada
cv2.imwrite("imagen_procesada.jpg", thresholded)

print("¡Preprocesamiento completado!")
```

## Explicación paso a paso

1. **Lectura**: `cv2.imread()` carga la imagen en formato BGR (Blue, Green, Red), que es el formato estándar de OpenCV.

2. **Conversión de color**: `cv2.cvtColor()` convierte entre espacios de color. La conversión a escala de grises es común para reducir la complejidad.

3. **Redimensionamiento**: `cv2.resize()` cambia el tamaño de la imagen. Es útil para normalizar el tamaño de entrada para algoritmos de procesamiento.

4. **Filtros**: Los filtros como `GaussianBlur` ayudan a reducir el ruido y suavizar la imagen.

5. **Umbralización**: `cv2.threshold()` convierte una imagen en escala de grises a una imagen binaria (blanco y negro).

Este flujo básico es el fundamento de muchos proyectos de visión por computadora.
