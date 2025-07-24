import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import textwrap
import io

# --- Streamlit UI ---
st.title("🆓 No-API Thumbnail Generator")
st.markdown("Create viral thumbnails without any API calls")

# User Inputs
title = st.text_input("Title:", "YOU WON'T BELIEVE THIS!")
subtitle = st.text_input("Subtitle (optional):", "SHOCKING REVEAL!")
style = st.selectbox("Style:", ["Dark", "Bright", "Gradient", "Pattern"])

# Generate Button
if st.button("🎨 Generate Thumbnail"):
    # 1. Create blank image (1280x720 pixels)
    img = Image.new("RGB", (1280, 720), color="#222222")
    draw = ImageDraw.Draw(img)
    
    # 2. Apply selected style
    if style == "Gradient":
        # Create horizontal gradient
        arr = np.linspace(0, 255, 1280)
        gradient = np.tile(arr, (720, 1))
        gradient_img = Image.fromarray(gradient.astype(np.uint8))
        img = ImageOps.colorize(gradient_img, "#FF0000", "#0000FF")
    
    elif style == "Pattern":
        # Draw diagonal lines
        for i in range(0, 1280, 30):
            draw.line([(i, 0), (0, i)], fill="#FFFFFF", width=2)
    
    # 3. Add text
    try:
        # Try loading a bold font (works on Streamlit Cloud)
        font = ImageFont.truetype("arialbd.ttf", 80)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Main title
    wrapped_title = textwrap.fill(title, width=15)
    title_width = draw.textlength(wrapped_title, font=font)
    draw.text(
        ((1280-title_width)/2, 200), 
        wrapped_title, 
        fill="#FFFFFF", 
        font=font,
        stroke_width=3,
        stroke_fill="#000000"
    )
    
    # Subtitle (smaller)
    if subtitle:
        subfont = ImageFont.truetype("arial.ttf", 40)
        sub_width = draw.textlength(subtitle, font=subfont)
        draw.text(
            ((1280-sub_width)/2, 350), 
            subtitle, 
            fill="#FFD700", 
            font=subfont
        )
    
    # 4. Add decorative border
    draw.rectangle([50, 50, 1230, 670], outline="#FFFFFF", width=5)
    
    # 5. Display and download
    st.image(img, use_column_width=True)
    
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    st.download_button(
        "💾 Download Thumbnail",
        data=img_bytes.getvalue(),
        file_name="thumbnail.png",
        mime="image/png"
    )
