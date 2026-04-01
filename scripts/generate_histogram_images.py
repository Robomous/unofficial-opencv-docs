"""
Generate example images for the histograms & contrast enhancement documentation page.

Usage:
    python scripts/generate_histogram_images.py

Requires: opencv-python, matplotlib, numpy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
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


def generate_histogram_examples(img_bgr: np.ndarray) -> None:
    """
    Generate a 2x2 grid where each cell contains a small image and its
    histogram below. Shows dark, bright, low-contrast, and good-exposure cases.
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # (a) Dark image — multiply by 0.3
    dark = np.clip(gray * 0.3, 0, 255).astype(np.uint8)
    # (b) Bright image — add 100 and clip
    bright = np.clip(gray.astype(np.int16) + 100, 0, 255).astype(np.uint8)
    # (c) Low contrast — scale to range 100-150
    low_contrast = np.clip(
        100 + (gray.astype(np.float32) / 255.0) * 50, 0, 255
    ).astype(np.uint8)
    # (d) Good exposure — original
    good = gray.copy()

    panels = [
        (dark, "(a) Dark Image"),
        (bright, "(b) Bright Image"),
        (low_contrast, "(c) Low Contrast"),
        (good, "(d) Good Exposure"),
    ]

    fig = plt.figure(figsize=(12, 10), facecolor="white")
    outer = gridspec.GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.25)

    for idx, (image, title) in enumerate(panels):
        inner = gridspec.GridSpecFromSubplotSpec(
            2, 1, subplot_spec=outer[idx], height_ratios=[3, 1.2], hspace=0.08
        )

        # Image
        ax_img = fig.add_subplot(inner[0])
        ax_img.imshow(image, cmap="gray", vmin=0, vmax=255)
        ax_img.set_title(title, fontsize=13, fontweight="bold", pad=8)
        ax_img.axis("off")

        # Histogram
        ax_hist = fig.add_subplot(inner[1])
        hist = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten()
        ax_hist.fill_between(range(256), hist, color="#777777", alpha=0.8)
        ax_hist.set_xlim([0, 255])
        ax_hist.set_yticks([])
        ax_hist.set_xlabel("Pixel value", fontsize=9)
        ax_hist.spines["top"].set_visible(False)
        ax_hist.spines["right"].set_visible(False)
        ax_hist.spines["left"].set_visible(False)

    output_path = OUTPUT_DIR / "histogram-examples.webp"
    fig.savefig(
        str(output_path), format="webp", dpi=150, bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Saved: {output_path}")


def generate_clahe_comparison(img_bgr: np.ndarray) -> None:
    """
    Generate a 3-panel horizontal strip comparing:
    (a) Dark original, (b) Histogram Equalization, (c) CLAHE.
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # (a) Darken
    dark = np.clip(gray * 0.4, 0, 255).astype(np.uint8)
    # (b) Histogram Equalization
    equalized = cv2.equalizeHist(dark)
    # (c) CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_result = clahe.apply(dark)

    panels = [
        (dark, "(a) Original (Dark)"),
        (equalized, "(b) Histogram Equalization"),
        (clahe_result, "(c) CLAHE"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), facecolor="white")

    for ax, (image, title) in zip(axes, panels):
        ax.imshow(image, cmap="gray", vmin=0, vmax=255)
        ax.set_title(title, fontsize=13, fontweight="bold", pad=10)
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "clahe-comparison.webp"
    fig.savefig(
        str(output_path), format="webp", dpi=150, bbox_inches="tight",
        facecolor="white",
    )
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    print(f"Loading image from: {INPUT_IMAGE}")
    img_bgr = load_image()
    print(f"Image shape: {img_bgr.shape}")

    print("\nGenerating histogram-examples.webp ...")
    generate_histogram_examples(img_bgr)

    print("\nGenerating clahe-comparison.webp ...")
    generate_clahe_comparison(img_bgr)

    print("\nDone.")


if __name__ == "__main__":
    main()
