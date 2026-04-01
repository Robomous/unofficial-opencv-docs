"""
Generate example images for the color space conversions documentation page.

Usage:
    python scripts/generate_color_space_images.py

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


def generate_color_spaces_comparison(img_bgr: np.ndarray) -> None:
    """
    Generate a 4-panel horizontal strip showing the image in:
    Original (RGB), Grayscale, HSV, and LAB color spaces.
    """
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

    panels = [
        (img_rgb, "Original (RGB)", None),
        (img_gray, "Grayscale", "gray"),
        (img_hsv, "HSV", None),
        (img_lab, "LAB", None),
    ]

    fig, axes = plt.subplots(1, 4, figsize=(16, 4), facecolor="white")

    for ax, (image, title, cmap) in zip(axes, panels):
        if cmap:
            ax.imshow(image, cmap=cmap)
        else:
            ax.imshow(image)
        ax.set_title(title, fontsize=14, fontweight="bold", pad=10)
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "color-spaces-comparison.webp"
    fig.savefig(str(output_path), format="webp", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"Saved: {output_path}")


def generate_inrange_mask_pipeline(img_bgr: np.ndarray) -> None:
    """
    Generate a 3-panel strip showing:
    (a) Original image, (b) Binary mask from inRange, (c) Masked result.
    Targets the red/pink tones in lenna.jpg using HSV ranges.
    """
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # Red wraps around the hue wheel in HSV, so we need two ranges.
    # Lower red range
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    # Upper red range
    lower_red2 = np.array([160, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(img_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(img_hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    result = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)
    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    panels = [
        (img_rgb, "Original"),
        (mask, "Binary Mask (cv2.inRange)"),
        (result_rgb, "Masked Result (cv2.bitwise_and)"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), facecolor="white")

    for ax, (image, title) in zip(axes, panels):
        if image.ndim == 2:
            ax.imshow(image, cmap="gray")
        else:
            ax.imshow(image)
        ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "inrange-mask-pipeline.webp"
    fig.savefig(str(output_path), format="webp", dpi=150, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    print(f"Loading image from: {INPUT_IMAGE}")
    img_bgr = load_image()
    print(f"Image shape: {img_bgr.shape}")

    print("\nGenerating color-spaces-comparison.webp ...")
    generate_color_spaces_comparison(img_bgr)

    print("\nGenerating inrange-mask-pipeline.webp ...")
    generate_inrange_mask_pipeline(img_bgr)

    print("\nDone.")


if __name__ == "__main__":
    main()
