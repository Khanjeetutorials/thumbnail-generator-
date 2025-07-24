import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io

# --- Streamlit UI ---
st.title("🎬 No-Error Thumbnail Generator")
st.markdown("100% API-free with reliable fonts")

# User Inputs
title = st.text_input("Title:", "MIND-BLOWING REVEAL!")
style = st.selectbox("Style:", ["Dark", "Light", "Dramatic"])

# Generate Button
if st.button("✨ Generate Thumbnail"):
    try:
        # 1. Create blank image
        img = Image.new("RGB", (1280, 720), color="#222222" if style != "Light" else "#f5f5f5")
        draw = ImageDraw.Draw(img)
        
        # 2. Use default font (works everywhere)
        try:
            # Try built-in font first
            font = ImageFont.load_default()
            font.size = 60  # Adjust size for default font
        except:
            # Ultimate fallback
            class SimpleFont:
                def getlength(self, text):
                    return len(text) * 30
                def getsize(self, text):
                    return (self.getlength(text), 40)
            font = SimpleFont()
        
        # 3. Add text (with manual centering)
        wrapped_title = textwrap.fill(title, width=20)
        text_width = len(wrapped_title) * 30  # Approximate width
        x = (1280 - text_width) / 2
        y = 300
        
        draw.text((x, y), wrapped_title, 
                 fill="#FFFFFF" if style != "Light" else "#000000", 
                 font=font)
        
        # 4. Add border
        draw.rectangle([50, 50, 1230, 670], outline="#FF0000", width=5)
        
        # 5. Display and download
        st.image(img, use_column_width=True)
        
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG")
        st.download_button(
            "💾 Download",
            data=img_bytes.getvalue(),
            file_name="thumbnail.png",
            mime="image/png"
        )
        
    except Exception as e:
        st.error(f"Simplified error handling: {str(e)}")
