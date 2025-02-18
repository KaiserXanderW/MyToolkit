import os
from PIL import Image, ImageDraw

def load_icon():
    png_path = os.path.join("Resources", "toolkit_icon.png")
    if os.path.exists(png_path):
        try:
            return Image.open(png_path)
        except Exception as e:
            print(f"Error loading toolkit_icon.png: {e}")

    # fallback: draw a simple icon
    img = Image.new("RGB", (64, 64), color="blue")
    draw = ImageDraw.Draw(img)
    draw.text((16, 20), "TK", fill="white")
    return img
