---
title: Installation
description: Different ways to install OpenCV for Python, depending on your operating system and workflow.
---

This page summarizes common installation options for OpenCV in Python:

## Installation with pip

The easiest way to install OpenCV is using pip:

```bash
pip install opencv-python
```

To install the version with additional contributions:

```bash
pip install opencv-contrib-python
```

## Installation with Conda

If you use Conda or Miniconda:

```bash
conda install -c conda-forge opencv
```

Or create a specific Conda environment:

```bash
conda create -n opencv-env python=3.10
conda activate opencv-env
conda install -c conda-forge opencv
```

## Platform-specific notes

### macOS

```bash
# Make sure you have Homebrew installed
brew install python3

# Then install OpenCV
pip3 install opencv-python
```

### Linux (Ubuntu/Debian)

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3-pip python3-dev

# Install OpenCV
pip3 install opencv-python
```

### Windows

```bash
# Use PowerShell or CMD
python -m pip install opencv-python
```

## Verify the installation

Create a verification script:

```python
import cv2
import sys

try:
    # Check version
    version = cv2.__version__
    print(f"✓ OpenCV {version} installed correctly")
    
    # Verify we can read an image
    img = cv2.imread("test.jpg") if len(sys.argv) > 1 else None
    if img is not None:
        print(f"✓ Image reading working")
        print(f"  Dimensions: {img.shape}")
    else:
        print("ℹ Create a 'test.jpg' image to test reading")
    
    # Verify basic operations
    test_img = cv2.imread("test.jpg") if len(sys.argv) > 1 else None
    if test_img is not None:
        gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        print("✓ Color conversion working")
    
except ImportError as e:
    print(f"✗ Error: {e}")
    print("  Make sure you've installed opencv-python")
except Exception as e:
    print(f"⚠ Warning: {e}")

print("\nInstallation verified!")
```

Run the script:

```bash
python verify_opencv.py
```

If this code runs without errors and prints a version, your installation is working.
