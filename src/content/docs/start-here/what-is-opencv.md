---
title: What is OpenCV?
description: A high-level overview of OpenCV and how it fits into computer vision projects.
---

OpenCV is an open-source library for computer vision and image processing.

<img src="/assets/opencv_logo.svg" alt="OpenCV Logo" class="dark:sl-hidden" />
<img src="/assets/opencv_logo_white.svg" alt="OpenCV Logo" class="light:sl-hidden" />

In this page, we briefly explain:

- **Core idea**: manipulating images, video, and camera input.
- **Typical tasks**: filtering, edge detection, object detection, feature extraction, etc.
- **Why we focus** on the **Python** API in this unofficial documentation.

Keep it high-level and friendly. The goal is to motivate the reader, not to list every single feature.

## Basic example

Here's a simple example of how OpenCV can load and display an image:

```python
import cv2

# Load an image from disk
img = cv2.imread("image.jpg")

# Verify the image loaded correctly
if img is not None:
    # Display the image in a window
    cv2.imshow("My Image", img)
    
    # Wait for the user to press a key
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image")
```

This basic example demonstrates one of the most common operations: loading and displaying an image. OpenCV offers many more capabilities for processing and analyzing images.
