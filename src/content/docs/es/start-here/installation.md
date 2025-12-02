---
title: Instalación
description: Distintas formas de instalar OpenCV para Python según tu sistema operativo y flujo de trabajo.
---

Esta página resume opciones comunes para instalar OpenCV en Python:

## Instalación con pip

La forma más sencilla de instalar OpenCV es usando pip:

```bash
pip install opencv-python
```

Para instalar la versión con contribuciones adicionales:

```bash
pip install opencv-contrib-python
```

## Instalación con Conda

Si usas Conda o Miniconda:

```bash
conda install -c conda-forge opencv
```

O crea un entorno Conda específico:

```bash
conda create -n opencv-env python=3.10
conda activate opencv-env
conda install -c conda-forge opencv
```

## Notas específicas por sistema

### macOS

```bash
# Asegúrate de tener Homebrew instalado
brew install python3

# Luego instala OpenCV
pip3 install opencv-python
```

### Linux (Ubuntu/Debian)

```bash
# Instalar dependencias del sistema
sudo apt-get update
sudo apt-get install python3-pip python3-dev

# Instalar OpenCV
pip3 install opencv-python
```

### Windows

```bash
# Usa PowerShell o CMD
python -m pip install opencv-python
```

## Verificar la instalación

Crea un script de verificación:

```python
import cv2
import sys

try:
    # Verificar la versión
    version = cv2.__version__
    print(f"✓ OpenCV {version} instalado correctamente")
    
    # Verificar que podemos crear una imagen
    img = cv2.imread("test.jpg") if len(sys.argv) > 1 else None
    if img is not None:
        print(f"✓ Lectura de imágenes funcionando")
        print(f"  Dimensiones: {img.shape}")
    else:
        print("ℹ Crea una imagen 'test.jpg' para probar la lectura")
    
    # Verificar operaciones básicas
    test_img = cv2.imread("test.jpg") if len(sys.argv) > 1 else None
    if test_img is not None:
        gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        print("✓ Conversión de color funcionando")
    
except ImportError as e:
    print(f"✗ Error: {e}")
    print("  Asegúrate de haber instalado opencv-python")
except Exception as e:
    print(f"⚠ Advertencia: {e}")

print("\n¡Instalación verificada!")
```

Ejecuta el script:

```bash
python verificar_opencv.py
```

Si este código se ejecuta sin errores y muestra una versión, la instalación es correcta.
