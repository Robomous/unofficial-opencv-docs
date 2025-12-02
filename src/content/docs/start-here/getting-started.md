---
title: Getting Started with OpenCV
description: Set up your environment and install OpenCV to start working with images.
---

This guide will help you:

- Install Python and create a virtual environment.
- Install OpenCV for Python (`opencv-python`).
- Verify that everything works by loading and displaying a simple image.

## Prerequisites

- Basic Python knowledge.
- A recent version of Python (3.10+ recommended).

## Create a virtual environment

First, create a virtual environment to isolate your project dependencies:

```bash
# Create a virtual environment
python3 -m venv opencv-env

# Activate the virtual environment
# On macOS/Linux:
source opencv-env/bin/activate

# On Windows:
# opencv-env\Scripts\activate
```

## Install OpenCV

Once the virtual environment is activated, install OpenCV:

```bash
pip install opencv-python
```

## Verify the installation

Create a file `test_opencv.py` with the following code:

```python
import cv2
import numpy as np

# Verify OpenCV version
print(f"OpenCV version: {cv2.__version__}")

# Create a simple test image
# Create a black image of 200x200 pixels
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Draw a white circle in the center
cv2.circle(img, (100, 100), 50, (255, 255, 255), -1)

# Display the image
cv2.imshow("Test OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("OpenCV is working correctly!")
```

Run the script:

```bash
python test_opencv.py
```

If you see a window with a white circle and the confirmation message, everything is working!

## Next steps

Once your environment is ready, continue with the **Installation** page for more details or jump directly to **What is OpenCV?** to understand the library at a high level.
