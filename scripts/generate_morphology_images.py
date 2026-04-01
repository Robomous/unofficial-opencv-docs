"""Generate example images for morphological operations documentation."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "src" / "assets" / "images" / "preprocessing"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_noisy_binary_image(h=300, w=400, noise_ratio=0.02):
    """Create a binary image with shapes and salt-and-pepper noise."""
    img = np.zeros((h, w), dtype=np.uint8)

    # Draw some white shapes
    cv2.rectangle(img, (50, 50), (150, 150), 255, -1)
    cv2.rectangle(img, (220, 30), (350, 100), 255, -1)
    cv2.circle(img, (120, 230), 50, 255, -1)
    cv2.circle(img, (300, 210), 40, 255, -1)
    cv2.rectangle(img, (200, 160), (280, 270), 255, -1)

    # Add salt-and-pepper noise
    rng = np.random.default_rng(42)
    num_salt = int(h * w * noise_ratio)
    num_pepper = int(h * w * noise_ratio)

    # Salt (white pixels)
    coords = (rng.integers(0, h, num_salt), rng.integers(0, w, num_salt))
    img[coords] = 255

    # Pepper (black pixels)
    coords = (rng.integers(0, h, num_pepper), rng.integers(0, w, num_pepper))
    img[coords] = 0

    return img


def generate_morphology_comparison():
    """Generate a 2x3 grid comparing morphological operations."""
    img = create_noisy_binary_image()
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    erosion = cv2.erode(img, kernel)
    dilation = cv2.dilate(img, kernel)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    panels = [
        ("Original (Noisy)", img),
        ("Erosion", erosion),
        ("Dilation", dilation),
        ("Opening", opening),
        ("Closing", closing),
        ("Gradient", gradient),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(12, 7), facecolor="white")

    for ax, (title, image) in zip(axes.flat, panels):
        ax.imshow(image, cmap="gray", vmin=0, vmax=255)
        ax.set_title(title, fontsize=13, fontweight="bold", pad=8)
        ax.axis("off")

    plt.tight_layout()
    out_path = OUTPUT_DIR / "morphology-comparison.webp"
    fig.savefig(out_path, dpi=150, format="webp", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    generate_morphology_comparison()
