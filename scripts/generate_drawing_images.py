"""
Generate example images for the Drawing & Annotations documentation section.

Usage:
    python scripts/generate_drawing_images.py

Requires: opencv-python, matplotlib, numpy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "src" / "assets" / "images" / "drawing"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# drawing-basics.mdx images
# ---------------------------------------------------------------------------


def generate_coordinate_system() -> None:
    """Show the OpenCV coordinate system with origin, axes, and labels."""
    canvas = np.ones((400, 500, 3), dtype=np.uint8) * 255

    # Draw axes
    cv2.arrowedLine(canvas, (50, 50), (450, 50), (200, 60, 50), 2, cv2.LINE_AA, tipLength=0.03)
    cv2.arrowedLine(canvas, (50, 50), (50, 350), (200, 60, 50), 2, cv2.LINE_AA, tipLength=0.03)

    # Labels
    cv2.putText(canvas, "(0, 0)", (55, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(canvas, "x", (455, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 60, 50), 2, cv2.LINE_AA)
    cv2.putText(canvas, "y", (35, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 60, 50), 2, cv2.LINE_AA)

    # Tick marks
    for i in range(100, 450, 50):
        cv2.line(canvas, (i, 45), (i, 55), (150, 150, 150), 1, cv2.LINE_AA)
        cv2.putText(canvas, str(i - 50), (i - 10, 75), cv2.FONT_HERSHEY_PLAIN, 0.8, (100, 100, 100), 1, cv2.LINE_AA)
    for j in range(100, 350, 50):
        cv2.line(canvas, (45, j), (55, j), (150, 150, 150), 1, cv2.LINE_AA)
        cv2.putText(canvas, str(j - 50), (10, j + 5), cv2.FONT_HERSHEY_PLAIN, 0.8, (100, 100, 100), 1, cv2.LINE_AA)

    # Example point
    cv2.circle(canvas, (250, 200), 6, (0, 0, 220), -1, cv2.LINE_AA)
    cv2.putText(canvas, "(200, 150)", (258, 198), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 220), 1, cv2.LINE_AA)

    # Dashed lines to point
    for k in range(50, 250, 8):
        cv2.line(canvas, (k, 200), (min(k + 4, 250), 200), (180, 180, 220), 1)
    for k in range(50, 200, 8):
        cv2.line(canvas, (250, k), (250, min(k + 4, 200)), (180, 180, 220), 1)

    fig, ax = plt.subplots(1, 1, figsize=(6, 5), facecolor="white")
    ax.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    ax.set_title("OpenCV Coordinate System", fontsize=13, fontweight="bold", pad=10)
    ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "coordinate-system.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> coordinate-system.webp")


def generate_basic_shapes() -> None:
    """Show lines, rectangles, circles, ellipses, and polygons in a grid."""
    panels = []

    # Panel 1: Lines — grid + crosshair
    p1 = np.zeros((300, 300, 3), dtype=np.uint8)
    for x in range(0, 301, 50):
        cv2.line(p1, (x, 0), (x, 300), (50, 50, 50), 1)
    for y in range(0, 301, 50):
        cv2.line(p1, (0, y), (300, y), (50, 50, 50), 1)
    cv2.line(p1, (150, 0), (150, 300), (0, 200, 0), 2, cv2.LINE_AA)
    cv2.line(p1, (0, 150), (300, 150), (0, 200, 0), 2, cv2.LINE_AA)
    cv2.circle(p1, (150, 150), 5, (0, 200, 0), -1, cv2.LINE_AA)
    panels.append((p1, "Lines: Grid & Crosshair"))

    # Panel 2: Rectangles
    p2 = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.rectangle(p2, (20, 20), (140, 120), (0, 255, 0), 2, cv2.LINE_AA)
    cv2.rectangle(p2, (160, 30), (280, 140), (0, 165, 255), -1, cv2.LINE_AA)
    # Semi-transparent rectangle
    overlay = p2.copy()
    cv2.rectangle(overlay, (50, 160), (250, 280), (255, 100, 100), -1, cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.4, p2, 0.6, 0, p2)
    cv2.rectangle(p2, (50, 160), (250, 280), (255, 100, 100), 2, cv2.LINE_AA)
    panels.append((p2, "Rectangles"))

    # Panel 3: Circles
    p3 = np.zeros((300, 300, 3), dtype=np.uint8)
    colors = [(0, 0, 255), (0, 150, 255), (0, 255, 255), (0, 255, 0), (255, 0, 0)]
    for i, r in enumerate(range(20, 140, 25)):
        cv2.circle(p3, (150, 150), r, colors[i % len(colors)], 2, cv2.LINE_AA)
    # Dot markers
    for pt in [(60, 60), (240, 60), (60, 240), (240, 240)]:
        cv2.circle(p3, pt, 8, (255, 255, 255), -1, cv2.LINE_AA)
    panels.append((p3, "Circles"))

    # Panel 4: Ellipses
    p4 = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.ellipse(p4, (150, 100), (120, 50), 0, 0, 360, (255, 200, 0), 2, cv2.LINE_AA)
    cv2.ellipse(p4, (150, 100), (120, 50), 30, 0, 360, (0, 200, 255), 2, cv2.LINE_AA)
    cv2.ellipse(p4, (150, 230), (100, 60), 0, 0, 270, (200, 100, 255), -1, cv2.LINE_AA)
    panels.append((p4, "Ellipses & Arcs"))

    # Panel 5: Polygons
    p5 = np.zeros((300, 300, 3), dtype=np.uint8)
    # Triangle outline
    tri = np.array([[150, 20], [50, 150], [250, 150]], dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(p5, [tri], True, (0, 255, 255), 2, cv2.LINE_AA)
    # Filled pentagon
    angles = np.linspace(0, 2 * np.pi, 6)[:-1] - np.pi / 2
    pent = np.column_stack([150 + 60 * np.cos(angles), 230 + 60 * np.sin(angles)]).astype(np.int32).reshape((-1, 1, 2))
    cv2.fillPoly(p5, [pent], (180, 0, 180), cv2.LINE_AA)
    panels.append((p5, "Polygons"))

    # Panel 6: Bounding boxes with labels
    p6 = np.zeros((300, 300, 3), dtype=np.uint8)
    detections = [
        ((20, 40, 120, 140), "Cat", (0, 255, 0)),
        ((140, 60, 280, 200), "Dog", (0, 165, 255)),
        ((50, 180, 200, 280), "Bird", (255, 80, 80)),
    ]
    for (x1, y1, x2, y2), label, color in detections:
        cv2.rectangle(p6, (x1, y1), (x2, y2), color, 2, cv2.LINE_AA)
        (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(p6, (x1, y1 - th - 8), (x1 + tw + 6, y1), color, -1, cv2.LINE_AA)
        cv2.putText(p6, label, (x1 + 3, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    panels.append((p6, "Bounding Boxes + Labels"))

    fig, axes = plt.subplots(2, 3, figsize=(12, 8), facecolor="white")
    for ax, (img, title) in zip(axes.flat, panels):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
        ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "basic-shapes-overview.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> basic-shapes-overview.webp")


# ---------------------------------------------------------------------------
# text-rendering.mdx images
# ---------------------------------------------------------------------------


def generate_font_comparison() -> None:
    """Display all OpenCV Hershey font faces on a single canvas."""
    fonts = [
        (cv2.FONT_HERSHEY_SIMPLEX, "FONT_HERSHEY_SIMPLEX"),
        (cv2.FONT_HERSHEY_PLAIN, "FONT_HERSHEY_PLAIN"),
        (cv2.FONT_HERSHEY_DUPLEX, "FONT_HERSHEY_DUPLEX"),
        (cv2.FONT_HERSHEY_COMPLEX, "FONT_HERSHEY_COMPLEX"),
        (cv2.FONT_HERSHEY_TRIPLEX, "FONT_HERSHEY_TRIPLEX"),
        (cv2.FONT_HERSHEY_COMPLEX_SMALL, "FONT_HERSHEY_COMPLEX_SMALL"),
        (cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, "FONT_HERSHEY_SCRIPT_SIMPLEX"),
        (cv2.FONT_HERSHEY_SCRIPT_COMPLEX, "FONT_HERSHEY_SCRIPT_COMPLEX"),
        (cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC, "SIMPLEX + FONT_ITALIC"),
    ]

    canvas = np.zeros((len(fonts) * 45 + 20, 600, 3), dtype=np.uint8)
    for i, (font, name) in enumerate(fonts):
        y = 35 + i * 45
        cv2.putText(canvas, name, (15, y), font, 0.7, (200, 200, 200), 1, cv2.LINE_AA)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5.5), facecolor="white")
    ax.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
    ax.set_title("OpenCV Hershey Font Faces", fontsize=13, fontweight="bold", pad=10)
    ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "font-comparison.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> font-comparison.webp")


def generate_text_features() -> None:
    """Show text scaling, centering, background boxes, and detection labels."""
    panels = []

    # Panel 1: Scale and thickness variations
    p1 = np.zeros((300, 400, 3), dtype=np.uint8)
    scales = [0.4, 0.7, 1.0, 1.5]
    for i, s in enumerate(scales):
        y = 40 + i * 70
        cv2.putText(p1, f"Scale {s}", (15, y), cv2.FONT_HERSHEY_SIMPLEX, s, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(p1, f"Bold", (280, y), cv2.FONT_HERSHEY_SIMPLEX, s * 0.8, (100, 200, 255), 2, cv2.LINE_AA)
    panels.append((p1, "Font Scale & Thickness"))

    # Panel 2: Centered text with background
    p2 = np.zeros((300, 400, 3), dtype=np.uint8)
    text = "Centered!"
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1.5
    thickness = 2
    (tw, th), baseline = cv2.getTextSize(text, font, scale, thickness)
    cx, cy = 200 - tw // 2, 150 + th // 2
    # Background box
    pad = 12
    cv2.rectangle(p2, (cx - pad, cy - th - pad), (cx + tw + pad, cy + baseline + pad), (80, 40, 20), -1, cv2.LINE_AA)
    cv2.rectangle(p2, (cx - pad, cy - th - pad), (cx + tw + pad, cy + baseline + pad), (200, 120, 60), 2, cv2.LINE_AA)
    cv2.putText(p2, text, (cx, cy), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)
    # Show baseline
    cv2.line(p2, (cx - pad, cy + baseline), (cx + tw + pad, cy + baseline), (0, 0, 200), 1, cv2.LINE_AA)
    cv2.putText(p2, "baseline", (cx + tw + pad + 5, cy + baseline + 5), cv2.FONT_HERSHEY_PLAIN, 0.9, (0, 0, 200), 1, cv2.LINE_AA)
    panels.append((p2, "Centered Text + Background"))

    # Panel 3: Detection labels
    p3 = np.zeros((300, 400, 3), dtype=np.uint8)
    dets = [
        ((15, 30, 180, 180), "Person", 0.95, (0, 220, 0)),
        ((200, 50, 380, 260), "Car", 0.87, (255, 100, 0)),
    ]
    for (x1, y1, x2, y2), label, conf, color in dets:
        text = f"{label} {conf:.0%}"
        cv2.rectangle(p3, (x1, y1), (x2, y2), color, 2, cv2.LINE_AA)
        (tw, th), bl = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
        cv2.rectangle(p3, (x1, y1 - th - bl - 6), (x1 + tw + 6, y1), color, -1, cv2.LINE_AA)
        cv2.putText(p3, text, (x1 + 3, y1 - bl - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)
    panels.append((p3, "Detection Labels"))

    # Panel 4: FPS overlay
    p4 = np.zeros((300, 400, 3), dtype=np.uint8)
    # Fake "scene" with some shapes
    cv2.circle(p4, (200, 180), 60, (60, 60, 60), -1)
    cv2.rectangle(p4, (50, 100), (130, 250), (40, 40, 40), -1)
    fps_text = "FPS: 30.2"
    (tw, th), bl = cv2.getTextSize(fps_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
    overlay = p4.copy()
    cv2.rectangle(overlay, (8, 8), (tw + 20, th + bl + 16), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, p4, 0.4, 0, p4)
    cv2.putText(p4, fps_text, (14, th + 12), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    panels.append((p4, "FPS Counter Overlay"))

    fig, axes = plt.subplots(2, 2, figsize=(10, 7), facecolor="white")
    for ax, (img, title) in zip(axes.flat, panels):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
        ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "text-features.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> text-features.webp")


# ---------------------------------------------------------------------------
# markers-and-arrows.mdx images
# ---------------------------------------------------------------------------


def generate_markers_and_arrows() -> None:
    """Show all marker types and arrow examples."""
    panels = []

    # Panel 1: Arrows — cardinal directions
    p1 = np.zeros((300, 300, 3), dtype=np.uint8)
    center = (150, 150)
    length = 100
    directions = [
        ((0, -length), "N", (0, 200, 255)),
        ((0, length), "S", (255, 100, 0)),
        ((-length, 0), "W", (0, 255, 100)),
        ((length, 0), "E", (200, 0, 255)),
    ]
    for (dx, dy), label, color in directions:
        end = (center[0] + dx, center[1] + dy)
        cv2.arrowedLine(p1, center, end, color, 2, cv2.LINE_AA, tipLength=0.15)
        lx = center[0] + int(dx * 1.2) - 5
        ly = center[1] + int(dy * 1.2) + 5
        cv2.putText(p1, label, (lx, ly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)
    panels.append((p1, "Arrows — Cardinal Directions"))

    # Panel 2: All marker types
    p2 = np.zeros((300, 500, 3), dtype=np.uint8)
    markers = [
        (cv2.MARKER_CROSS, "CROSS"),
        (cv2.MARKER_TILTED_CROSS, "TILTED_CROSS"),
        (cv2.MARKER_STAR, "STAR"),
        (cv2.MARKER_DIAMOND, "DIAMOND"),
        (cv2.MARKER_SQUARE, "SQUARE"),
        (cv2.MARKER_TRIANGLE_UP, "TRIANGLE_UP"),
        (cv2.MARKER_TRIANGLE_DOWN, "TRIANGLE_DOWN"),
    ]
    cols = [(0, 200, 255), (0, 255, 100), (255, 200, 0), (200, 100, 255),
            (255, 100, 100), (100, 255, 255), (200, 200, 0)]
    for i, ((mtype, name), color) in enumerate(zip(markers, cols)):
        x = 70 + (i % 4) * 110
        y = 80 + (i // 4) * 150
        cv2.drawMarker(p2, (x, y), color, mtype, 30, 2, cv2.LINE_AA)
        cv2.putText(p2, name, (x - 45, y + 45), cv2.FONT_HERSHEY_PLAIN, 0.8, (180, 180, 180), 1, cv2.LINE_AA)
    panels.append((p2, "All Marker Types"))

    # Panel 3: Motion vectors / optical flow simulation
    p3 = np.zeros((300, 300, 3), dtype=np.uint8)
    rng = np.random.default_rng(42)
    for _ in range(25):
        x, y = rng.integers(20, 280, size=2)
        dx, dy = rng.integers(-30, 30, size=2)
        mag = np.sqrt(dx**2 + dy**2)
        # Color by magnitude: blue (slow) to red (fast)
        t = min(mag / 40.0, 1.0)
        color = (int(255 * (1 - t)), int(100 * (1 - t)), int(255 * t))
        cv2.arrowedLine(p3, (int(x), int(y)), (int(x + dx), int(y + dy)), color, 1, cv2.LINE_AA, tipLength=0.3)
    panels.append((p3, "Optical Flow Vectors"))

    # Panel 4: Rich annotation combining elements
    p4 = np.zeros((300, 400, 3), dtype=np.uint8)
    # Fake regions
    cv2.rectangle(p4, (20, 40), (160, 180), (60, 60, 60), -1)
    cv2.rectangle(p4, (220, 80), (370, 250), (50, 50, 50), -1)
    # Annotate
    cv2.rectangle(p4, (20, 40), (160, 180), (0, 255, 0), 2, cv2.LINE_AA)
    cv2.putText(p4, "Region A", (30, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.rectangle(p4, (220, 80), (370, 250), (0, 165, 255), 2, cv2.LINE_AA)
    cv2.putText(p4, "Region B", (230, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 165, 255), 1, cv2.LINE_AA)
    cv2.arrowedLine(p4, (165, 110), (215, 140), (255, 255, 0), 2, cv2.LINE_AA, tipLength=0.2)
    cv2.drawMarker(p4, (90, 110), (0, 0, 255), cv2.MARKER_CROSS, 20, 2, cv2.LINE_AA)
    cv2.drawMarker(p4, (295, 165), (0, 0, 255), cv2.MARKER_CROSS, 20, 2, cv2.LINE_AA)
    panels.append((p4, "Combined Annotation"))

    fig, axes = plt.subplots(2, 2, figsize=(11, 7), facecolor="white")
    for ax, (img, title) in zip(axes.flat, panels):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
        ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "markers-arrows-overview.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> markers-arrows-overview.webp")


# ---------------------------------------------------------------------------
# mouse-interaction.mdx images
# ---------------------------------------------------------------------------


def generate_mouse_interaction() -> None:
    """Simulate results of interactive drawing tools."""
    panels = []

    # Panel 1: Freehand drawing simulation
    p1 = np.zeros((300, 400, 3), dtype=np.uint8)
    rng = np.random.default_rng(7)
    colors = [(0, 0, 255), (0, 200, 0), (255, 100, 0)]
    for c in colors:
        # Simulate a smooth freehand stroke
        cx, cy = rng.integers(80, 320), rng.integers(80, 220)
        pts = []
        for t in np.linspace(0, 4 * np.pi, 80):
            x = int(cx + (40 + 15 * np.sin(t * 0.7)) * np.cos(t))
            y = int(cy + (30 + 10 * np.cos(t * 0.5)) * np.sin(t))
            pts.append((x, y))
        for i in range(len(pts) - 1):
            cv2.line(p1, pts[i], pts[i + 1], c, 2, cv2.LINE_AA)
    panels.append((p1, "Freehand Drawing Tool"))

    # Panel 2: ROI selection
    p2 = np.zeros((300, 400, 3), dtype=np.uint8)
    # Fake content
    cv2.circle(p2, (120, 150), 50, (80, 80, 80), -1)
    cv2.rectangle(p2, (220, 80), (350, 220), (60, 60, 60), -1)
    # ROI rectangle (dashed-like with solid for clarity)
    cv2.rectangle(p2, (80, 70), (200, 220), (0, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(p2, "ROI", (85, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
    # Corner handles
    for pt in [(80, 70), (200, 70), (80, 220), (200, 220)]:
        cv2.circle(p2, pt, 4, (0, 255, 255), -1, cv2.LINE_AA)
    panels.append((p2, "ROI Selector"))

    # Panel 3: Point collector
    p3 = np.zeros((300, 400, 3), dtype=np.uint8)
    points = [(80, 60), (200, 40), (320, 100), (280, 200), (150, 250), (60, 180)]
    for i, (x, y) in enumerate(points):
        cv2.circle(p3, (x, y), 6, (0, 200, 255), -1, cv2.LINE_AA)
        cv2.circle(p3, (x, y), 8, (0, 200, 255), 1, cv2.LINE_AA)
        cv2.putText(p3, str(i + 1), (x + 12, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1, cv2.LINE_AA)
        cv2.putText(p3, f"({x},{y})", (x + 12, y + 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (140, 140, 140), 1, cv2.LINE_AA)
    # Connect with polyline
    pts_arr = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
    cv2.polylines(p3, [pts_arr], False, (80, 80, 80), 1, cv2.LINE_AA)
    panels.append((p3, "Point Collector"))

    fig, axes = plt.subplots(1, 3, figsize=(13, 4), facecolor="white")
    for ax, (img, title) in zip(axes.flat, panels):
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(title, fontsize=11, fontweight="bold", pad=8)
        ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "mouse-interaction-examples.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> mouse-interaction-examples.webp")


# ---------------------------------------------------------------------------
# trackbars-and-controls.mdx images
# ---------------------------------------------------------------------------


def generate_trackbar_examples() -> None:
    """Show typical outputs from trackbar-based tools."""
    panels = []

    # Panel 1: HSV color range — show a colorful image + mask + result
    # Create a synthetic colorful image with shapes
    scene = np.zeros((250, 300, 3), dtype=np.uint8)
    cv2.circle(scene, (80, 80), 50, (0, 0, 220), -1, cv2.LINE_AA)       # Red circle
    cv2.rectangle(scene, (160, 40), (280, 140), (220, 180, 0), -1, cv2.LINE_AA)  # Cyan-ish rectangle
    cv2.ellipse(scene, (150, 200), (80, 35), 0, 0, 360, (0, 200, 0), -1, cv2.LINE_AA)  # Green ellipse
    cv2.circle(scene, (260, 200), 35, (0, 100, 255), -1, cv2.LINE_AA)    # Orange circle

    hsv = cv2.cvtColor(scene, cv2.COLOR_BGR2HSV)
    # Mask for "red" range
    mask = cv2.inRange(hsv, np.array([0, 100, 100]), np.array([10, 255, 255]))
    result = cv2.bitwise_and(scene, scene, mask=mask)

    p_scene = cv2.cvtColor(scene, cv2.COLOR_BGR2RGB)
    p_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    p_result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), facecolor="white")
    axes[0].imshow(p_scene)
    axes[0].set_title("Original", fontsize=11, fontweight="bold", pad=8)
    axes[0].axis("off")
    axes[1].imshow(p_mask)
    axes[1].set_title("HSV Mask (Red Range)", fontsize=11, fontweight="bold", pad=8)
    axes[1].axis("off")
    axes[2].imshow(p_result)
    axes[2].set_title("Filtered Result", fontsize=11, fontweight="bold", pad=8)
    axes[2].axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "trackbar-hsv-picker.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> trackbar-hsv-picker.webp")

    # Panel 2: Canny edge detection at different thresholds
    # Create a synthetic image with various edges
    canvas = np.zeros((250, 300), dtype=np.uint8)
    cv2.rectangle(canvas, (30, 30), (120, 120), 200, -1)
    cv2.circle(canvas, (200, 80), 50, 180, -1)
    cv2.ellipse(canvas, (150, 200), (100, 30), 0, 0, 360, 160, -1)
    # Add gradient
    grad = np.linspace(0, 100, 300, dtype=np.uint8)
    canvas = cv2.add(canvas, np.tile(grad, (250, 1)).astype(np.uint8))
    canvas = cv2.GaussianBlur(canvas, (3, 3), 0)

    edges_low = cv2.Canny(canvas, 30, 80)
    edges_mid = cv2.Canny(canvas, 80, 160)
    edges_high = cv2.Canny(canvas, 150, 300)

    fig, axes = plt.subplots(1, 4, figsize=(13, 3.5), facecolor="white")
    axes[0].imshow(canvas, cmap="gray")
    axes[0].set_title("Source Image", fontsize=10, fontweight="bold", pad=8)
    axes[0].axis("off")
    titles = ["Canny (30, 80)", "Canny (80, 160)", "Canny (150, 300)"]
    for ax, edges, title in zip(axes[1:], [edges_low, edges_mid, edges_high], titles):
        ax.imshow(edges, cmap="gray")
        ax.set_title(title, fontsize=10, fontweight="bold", pad=8)
        ax.axis("off")
    plt.tight_layout()
    fig.savefig(str(OUTPUT_DIR / "trackbar-canny-tuner.webp"), format="webp", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  -> trackbar-canny-tuner.webp")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("Generating Drawing & Annotations images...")
    print()

    print("[drawing-basics]")
    generate_coordinate_system()
    generate_basic_shapes()
    print()

    print("[text-rendering]")
    generate_font_comparison()
    generate_text_features()
    print()

    print("[markers-and-arrows]")
    generate_markers_and_arrows()
    print()

    print("[mouse-interaction]")
    generate_mouse_interaction()
    print()

    print("[trackbars-and-controls]")
    generate_trackbar_examples()
    print()

    print("Done! All images saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
