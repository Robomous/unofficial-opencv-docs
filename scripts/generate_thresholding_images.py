"""
Generate example images for the thresholding documentation page.

Usage:
    python scripts/generate_thresholding_images.py

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


def generate_thresholding_comparison(img_bgr: np.ndarray) -> None:
    """
    Generate a 2x2 grid showing:
    (a) Original grayscale with uneven lighting (gradient overlay)
    (b) Simple binary threshold (THRESH_BINARY, value=127)
    (c) Adaptive threshold (ADAPTIVE_THRESH_GAUSSIAN_C, blockSize=11, C=2)
    (d) Otsu's threshold (THRESH_BINARY + THRESH_OTSU)
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Create a horizontal gradient to simulate uneven lighting.
    # Left side darker, right side brighter.
    h, w = gray.shape
    gradient = np.linspace(-80, 80, w, dtype=np.float32)
    gradient = np.tile(gradient, (h, 1))

    # Blend the gradient with the grayscale image.
    uneven = np.clip(gray.astype(np.float32) + gradient, 0, 255).astype(np.uint8)

    # (b) Simple binary threshold
    _, binary = cv2.threshold(uneven, 127, 255, cv2.THRESH_BINARY)

    # (c) Adaptive threshold (Gaussian)
    adaptive = cv2.adaptiveThreshold(
        uneven, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, blockSize=11, C=2,
    )

    # (d) Otsu's threshold
    _, otsu = cv2.threshold(uneven, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    panels = [
        (uneven, "(a) Grayscale with Uneven Lighting"),
        (binary, "(b) Binary Threshold (value=127)"),
        (adaptive, "(c) Adaptive Threshold (Gaussian)"),
        (otsu, "(d) Otsu's Threshold"),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(10, 10), facecolor="white")

    for ax, (image, title) in zip(axes.flat, panels):
        ax.imshow(image, cmap="gray")
        ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "thresholding-comparison.webp"
    fig.savefig(str(output_path), format="webp", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    print(f"Loading image from: {INPUT_IMAGE}")
    img_bgr = load_image()
    print(f"Image shape: {img_bgr.shape}")

    print("\nGenerating thresholding-comparison.webp ...")
    generate_thresholding_comparison(img_bgr)

    print("\nDone.")


if __name__ == "__main__":
    main()
