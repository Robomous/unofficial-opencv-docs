"""
Generate example images for the edge detection & gradients documentation page.

Usage:
    python scripts/generate_edge_detection_images.py

Requires: opencv-python, matplotlib, numpy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_IMAGE = BASE_DIR / "src" / "assets" / "photos" / "lenna.jpg"
OUTPUT_DIR = BASE_DIR / "src" / "assets" / "images" / "preprocessing"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_image():
    """Load the base image and return it in BGR format."""
    img = cv2.imread(str(INPUT_IMAGE))
    if img is None:
        raise FileNotFoundError(f"Could not load image: {INPUT_IMAGE}")
    return img


def generate_edge_detection_comparison(img_bgr: np.ndarray) -> None:
    """
    Generate a 2x3 grid showing:
      Row 1: (a) Original grayscale, (b) Sobel X, (c) Sobel Y
      Row 2: (d) Sobel Combined, (e) Laplacian, (f) Canny
    """
    # Convert to grayscale and blur
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Sobel X
    sobel_x_64f = cv2.Sobel(blurred, cv2.CV_64F, 1, 0)
    sobel_x = cv2.convertScaleAbs(sobel_x_64f)

    # Sobel Y
    sobel_y_64f = cv2.Sobel(blurred, cv2.CV_64F, 0, 1)
    sobel_y = cv2.convertScaleAbs(sobel_y_64f)

    # Sobel Combined
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

    # Laplacian
    laplacian_64f = cv2.Laplacian(blurred, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian_64f)

    # Canny
    canny = cv2.Canny(blurred, 50, 150)

    panels = [
        # Row 1
        (gray, "(a) Original Grayscale"),
        (sobel_x, "(b) Sobel X (Horizontal Edges)"),
        (sobel_y, "(c) Sobel Y (Vertical Edges)"),
        # Row 2
        (sobel_combined, "(d) Sobel Combined"),
        (laplacian, "(e) Laplacian"),
        (canny, "(f) Canny (50, 150)"),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(14, 9), facecolor="white")

    for ax, (image, title) in zip(axes.flat, panels):
        ax.imshow(image, cmap="gray")
        ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "edge-detection-comparison.webp"
    fig.savefig(str(output_path), format="webp", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    print(f"Loading image from: {INPUT_IMAGE}")
    img_bgr = load_image()
    print(f"Image shape: {img_bgr.shape}")

    print("\nGenerating edge-detection-comparison.webp ...")
    generate_edge_detection_comparison(img_bgr)

    print("\nDone.")


if __name__ == "__main__":
    main()
