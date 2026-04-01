"""
Generate example images for the Image Filtering & Smoothing documentation page.

Usage:
    python scripts/generate_filtering_images.py

Requires:
    opencv-python, numpy, matplotlib
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_IMAGE = BASE_DIR / "src" / "assets" / "photos" / "lenna.jpg"
OUT_DIR = BASE_DIR / "src" / "assets" / "images" / "preprocessing"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Shared style helpers
# ---------------------------------------------------------------------------
FONT_LABEL = {"fontsize": 11, "fontweight": "bold", "fontfamily": "sans-serif"}
DPI = 150


def _read_rgb(path: Path) -> np.ndarray:
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def _add_gaussian_noise(img: np.ndarray, sigma: float = 25.0) -> np.ndarray:
    rng = np.random.default_rng(42)
    noise = rng.normal(0, sigma, img.shape)
    noisy = np.clip(img.astype(np.float64) + noise, 0, 255).astype(np.uint8)
    return noisy


# ===================================================================
# 1. blur-comparison.webp
# ===================================================================
def generate_blur_comparison() -> None:
    img = _read_rgb(SRC_IMAGE)
    noisy = _add_gaussian_noise(img, sigma=25)

    # Convert to BGR for OpenCV processing, then back to RGB for display
    noisy_bgr = cv2.cvtColor(noisy, cv2.COLOR_RGB2BGR)

    results = [
        ("Original + Noise", noisy),
        ("cv2.blur()\n(7x7)", cv2.cvtColor(cv2.blur(noisy_bgr, (7, 7)), cv2.COLOR_BGR2RGB)),
        ("cv2.GaussianBlur()\n(7x7, σ=0)", cv2.cvtColor(cv2.GaussianBlur(noisy_bgr, (7, 7), 0), cv2.COLOR_BGR2RGB)),
        ("cv2.medianBlur()\n(ksize=7)", cv2.cvtColor(cv2.medianBlur(noisy_bgr, 7), cv2.COLOR_BGR2RGB)),
        ("cv2.bilateralFilter()\n(d=9, σColor=75, σSpace=75)",
         cv2.cvtColor(cv2.bilateralFilter(noisy_bgr, 9, 75, 75), cv2.COLOR_BGR2RGB)),
    ]

    fig, axes = plt.subplots(1, 5, figsize=(18, 4), facecolor="white")
    for ax, (label, image) in zip(axes, results):
        ax.imshow(image)
        ax.set_title(label, fontsize=10, fontweight="bold", fontfamily="sans-serif", pad=8)
        ax.axis("off")

    fig.tight_layout(pad=1.0)
    out_path = OUT_DIR / "blur-comparison.webp"
    fig.savefig(str(out_path), format="webp", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  Saved {out_path}")


# ===================================================================
# 2. kernel-convolution.webp
# ===================================================================
def generate_kernel_convolution() -> None:
    # --- Data ---
    pixel_grid = np.array(
        [
            [120, 130, 125, 140, 135],
            [110, 100, 115, 120, 130],
            [105, 112, 108, 118, 125],
            [100, 105, 110, 115, 120],
            [95,  102, 107, 112, 118],
        ],
        dtype=float,
    )
    kernel = np.ones((3, 3), dtype=float) / 9.0

    # The kernel is centred on row=2, col=2 of the pixel grid
    kr, kc = 2, 2  # anchor position
    region = pixel_grid[kr - 1 : kr + 2, kc - 1 : kc + 2]
    output_val = np.sum(region * kernel)

    # --- Figure layout ---
    fig = plt.figure(figsize=(14, 5.5), facecolor="white")

    # Three logical sections: Input Grid | Kernel | Output
    gs = fig.add_gridspec(1, 3, width_ratios=[2.2, 1.2, 1.6], wspace=0.35)

    # --- Helper to draw a numeric grid ---
    def draw_grid(ax, data, title, highlight=None, highlight_color="#4A90D9",
                  cell_size=1.0, fmt=".0f", show_frac=False):
        rows, cols = data.shape
        ax.set_xlim(-0.5, cols - 0.5)
        ax.set_ylim(rows - 0.5, -0.5)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=13, fontweight="bold", fontfamily="sans-serif", pad=12)
        ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

        for spine in ax.spines.values():
            spine.set_visible(False)

        for r in range(rows):
            for c in range(cols):
                is_highlighted = (
                    highlight is not None
                    and highlight[0] <= r <= highlight[2]
                    and highlight[1] <= c <= highlight[3]
                )
                bg = highlight_color if is_highlighted else "#F0F0F0"
                text_color = "white" if is_highlighted else "#333333"

                rect = patches.FancyBboxPatch(
                    (c - 0.45, r - 0.45),
                    0.9,
                    0.9,
                    boxstyle="round,pad=0.04",
                    facecolor=bg,
                    edgecolor="#999999",
                    linewidth=1.0,
                )
                ax.add_patch(rect)

                if show_frac:
                    label = "1/9"
                else:
                    label = f"{data[r, c]:{fmt}}"

                ax.text(
                    c,
                    r,
                    label,
                    ha="center",
                    va="center",
                    fontsize=12,
                    fontweight="bold",
                    color=text_color,
                    fontfamily="monospace",
                )

    # --- Panel 1: Input pixel grid ---
    ax1 = fig.add_subplot(gs[0])
    draw_grid(
        ax1,
        pixel_grid,
        "Input Pixel Grid",
        highlight=(kr - 1, kc - 1, kr + 1, kc + 1),
        highlight_color="#4A90D9",
    )
    # Add annotation arrow pointing to highlighted region
    ax1.annotate(
        "Region under\nthe kernel",
        xy=(kc, kr),
        xytext=(kc + 1.8, kr + 1.8),
        fontsize=9,
        fontweight="bold",
        color="#4A90D9",
        arrowprops=dict(arrowstyle="->", color="#4A90D9", lw=1.5),
        ha="center",
    )

    # --- Panel 2: 3x3 averaging kernel ---
    ax2 = fig.add_subplot(gs[1])
    draw_grid(
        ax2,
        kernel,
        "3×3 Averaging Kernel",
        show_frac=True,
        highlight_color="#E8E8E8",
    )

    # --- Panel 3: Computation + result ---
    ax3 = fig.add_subplot(gs[2])
    ax3.axis("off")
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.set_title("Convolution Output", fontsize=13, fontweight="bold", fontfamily="sans-serif", pad=12)

    # Build the computation text
    vals = region.flatten()
    sum_str = " + ".join(f"{int(v)}" for v in vals)
    total = np.sum(vals)

    lines = [
        ("Multiply each pixel by 1/9,\nthen sum the products:", 9.2, 12),
        (f"({sum_str})", 7.6, 10),
        (f"÷ 9", 6.6, 10),
        (f"= {total:.0f} / 9", 5.6, 11),
    ]

    for text, y, fs in lines:
        ax3.text(5, y, text, ha="center", va="center", fontsize=fs,
                 fontfamily="monospace", color="#333333")

    # Big result box
    result_box = patches.FancyBboxPatch(
        (2.0, 2.4), 6, 2.2,
        boxstyle="round,pad=0.3",
        facecolor="#4A90D9",
        edgecolor="#2C6FAC",
        linewidth=2,
    )
    ax3.add_patch(result_box)
    ax3.text(
        5,
        3.5,
        f"Output pixel = {output_val:.1f}",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color="white",
        fontfamily="sans-serif",
    )

    fig.tight_layout(pad=1.5)
    out_path = OUT_DIR / "kernel-convolution.webp"
    fig.savefig(str(out_path), format="webp", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  Saved {out_path}")


# ===================================================================
# Main
# ===================================================================
if __name__ == "__main__":
    print("Generating filtering images...")
    generate_blur_comparison()
    generate_kernel_convolution()
    print("Done.")
