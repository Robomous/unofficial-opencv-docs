"""
Generate example images for the geometric transformations documentation page.

Usage:
    python scripts/generate_geometric_images.py
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
SRC_IMAGE = Path(__file__).resolve().parent.parent / "src" / "assets" / "photos" / "lenna.jpg"
OUT_DIR = Path(__file__).resolve().parent.parent / "src" / "assets" / "images" / "preprocessing"

# Ensure output directory exists
OUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_resize_interpolation():
    """
    Crop a 50x50 region from the image, upscale it 8x with three different
    interpolation methods, and place them side by side with labels.
    """
    img = cv2.imread(str(SRC_IMAGE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Take a 50x50 crop from the centre of the image
    h, w = img.shape[:2]
    cy, cx = h // 2, w // 2
    crop = img[cy - 25 : cy + 25, cx - 25 : cx + 25]

    methods = [
        ("INTER_NEAREST", cv2.INTER_NEAREST),
        ("INTER_LINEAR", cv2.INTER_LINEAR),
        ("INTER_CUBIC", cv2.INTER_CUBIC),
    ]

    scale = 8
    panels = []
    for label, flag in methods:
        up = cv2.resize(crop, (crop.shape[1] * scale, crop.shape[0] * scale), interpolation=flag)
        panels.append((label, up))

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), facecolor="white")
    for ax, (label, panel) in zip(axes, panels):
        ax.imshow(panel)
        ax.set_title(label, fontsize=13, fontweight="bold", pad=8)
        ax.axis("off")

    fig.tight_layout()
    out_path = OUT_DIR / "resize-interpolation.webp"
    fig.savefig(str(out_path), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


def generate_perspective_transform():
    """
    Two-panel figure:
      (a) Original image warped to look tilted, with source points drawn.
      (b) The corrected (un-warped) image.
    """
    img = cv2.imread(str(SRC_IMAGE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]

    # Define a perspective distortion: map the rectangle to a trapezoid
    # to simulate a tilted document / photograph.
    src_pts = np.float32([
        [0, 0],
        [w, 0],
        [w, h],
        [0, h],
    ])
    dst_pts = np.float32([
        [w * 0.15, h * 0.10],
        [w * 0.85, h * 0.02],
        [w * 0.95, h * 0.90],
        [w * 0.05, h * 0.98],
    ])

    # Forward warp: create the "tilted" version
    M_forward = cv2.getPerspectiveTransform(src_pts, dst_pts)
    tilted = cv2.warpPerspective(img, M_forward, (w, h), borderValue=(255, 255, 255))

    # Draw the destination (source-for-correction) points on the tilted image
    tilted_annotated = tilted.copy()
    pts_int = dst_pts.astype(int)
    color = (0, 180, 255)  # orange
    for i in range(4):
        p1 = tuple(pts_int[i])
        p2 = tuple(pts_int[(i + 1) % 4])
        cv2.line(tilted_annotated, p1, p2, color, thickness=3, lineType=cv2.LINE_AA)
    for pt in pts_int:
        cv2.circle(tilted_annotated, tuple(pt), 10, (220, 40, 40), thickness=-1, lineType=cv2.LINE_AA)
        cv2.circle(tilted_annotated, tuple(pt), 10, (255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

    # Inverse warp: correct the perspective back to a rectangle
    M_inverse = cv2.getPerspectiveTransform(dst_pts, src_pts)
    corrected = cv2.warpPerspective(tilted, M_inverse, (w, h), borderValue=(255, 255, 255))

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor="white")

    axes[0].imshow(tilted_annotated)
    axes[0].set_title("(a) Tilted image with source points", fontsize=12, fontweight="bold", pad=8)
    axes[0].axis("off")

    axes[1].imshow(corrected)
    axes[1].set_title("(b) Perspective-corrected result", fontsize=12, fontweight="bold", pad=8)
    axes[1].axis("off")

    fig.tight_layout()
    out_path = OUT_DIR / "perspective-transform.webp"
    fig.savefig(str(out_path), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    print("Generating geometric transformation example images...")
    generate_resize_interpolation()
    generate_perspective_transform()
    print("Done.")
