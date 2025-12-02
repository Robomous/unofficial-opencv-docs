---
title: Image Preprocessing
description: Learn the basic preprocessing steps you will reuse in most OpenCV workflows.
---

Image preprocessing usually includes:

- **Reading images** from disk.
- **Converting color spaces** (e.g., BGR to grayscale).
- **Resizing images** to a consistent resolution.
- **Applying simple filters** (blur, threshold, etc.).

## Complete preprocessing example

Here's a complete example showing the basic steps:

```python
import cv2
import numpy as np

# 1. Read an image from disk
img = cv2.imread("original_image.jpg")

# Verify the image loaded correctly
if img is None:
    print("Error: Could not load the image")
    exit()

print(f"Original image: {img.shape}")  # (height, width, channels)

# 2. Convert from BGR to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"Grayscale: {gray.shape}")  # (height, width)

# 3. Resize the image to a consistent size
target_size = (640, 480)  # (width, height)
resized = cv2.resize(gray, target_size)
print(f"Resized: {resized.shape}")

# 4. Apply a blur filter
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

# 5. Apply thresholding
_, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# 6. Save the processed image
cv2.imwrite("processed_image.jpg", thresholded)

print("Preprocessing completed!")
```

## Step-by-step explanation

1. **Reading**: `cv2.imread()` loads the image in BGR (Blue, Green, Red) format, which is OpenCV's standard format.

2. **Color conversion**: `cv2.cvtColor()` converts between color spaces. Converting to grayscale is common to reduce complexity.

3. **Resizing**: `cv2.resize()` changes the image size. This is useful for normalizing input size for processing algorithms.

4. **Filters**: Filters like `GaussianBlur` help reduce noise and smooth the image.

5. **Thresholding**: `cv2.threshold()` converts a grayscale image to a binary (black and white) image.

This basic workflow is the foundation of many computer vision projects.
