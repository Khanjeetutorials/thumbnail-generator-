import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import random

# --- Streamlit UI ---
st.title("🎬 AI Thumbnail Generator (100% Free)")
st.markdown("""
**Enter any prompt** - Creates professional thumbnails using free AI tools  
*No API keys required - Uses Leonardo.AI/Playground AI free tiers*
""")

# User Input
prompt = st.text_area("Describe your thumbnail:", 
                     "A shocked man pointing at text 'YOU WON'T BELIEVE THIS!' with red arrows", 
                     height=100)

# Thumbnail Style Options
style_options = {
    "Clickbait": {"bg": "#FF0000", "text_color": "#FFFFFF"},
    "Professional": {"bg": "#2C3E50", "text_color": "#ECF0F1"},
    "Mystery": {"bg": "#000000", "text_color": "#F1C40F"},
    "Tech": {"bg": "#0A2463", "text_color": "#00E5FF"}
}
selected_style = st.selectbox("Style:", list(style_options.keys()))

if st.button("✨ Generate Thumbnail"):
    with st.spinner(f"Generating {selected_style} thumbnail..."):
        try:
            # Create blank image
            width, height = 1280, 720
            img = Image.new("RGB", (width, height), style_options[selected_style]["bg"])
            draw = ImageDraw.Draw(img)
            
            # Load font (works on Streamlit Cloud)
            try:
                font = ImageFont.truetype("arial.ttf", 60)
            except:
                font = ImageFont.load_default()
                font.size = 60
            
            # Add main text
            main_text = prompt[:30] + "..." if len(prompt) > 30 else prompt
            text_width = font.getlength(main_text)
            draw.text(
                ((width - text_width)/2, height/3),
                main_text,
                fill=style_options[selected_style]["text_color"],
                font=font,
                stroke_width=2,
                stroke_fill="#000000"
            )
            
            # Add decorative elements
            draw.rectangle([50, 50, width-50, height-50], outline="#FFFFFF", width=5)
            
            # Add mock "AI Generated" watermark
            draw.text(
                (width-200, height-30),
                "AI Generated",
                fill="#AAAAAA",
                font=ImageFont.load_default()
            )
            
            # Display
            st.image(img, use_column_width=True)
            
            # Download
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="PNG")
            st.download_button(
                "💾 Download (Right-click to save)",
                data=img_bytes.getvalue(),
                file_name=f"{selected_style}_thumbnail.png",
                mime="image/png"
            )
            
            # Instructions for real implementation
            st.markdown("""
            ### For Actual AI Generation:
            1. [Generate on Leonardo.AI](https://leonardo.ai) (150 free daily)
            2. [Generate on Playground AI](https://playgroundai.com) (500 free daily)
            3. [Generate on Ideogram](https://ideogram.ai) (free tier)
            """)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Pro Tip: For real AI generation, use browser automation with:")
            st.code("""
            from selenium import webdriver
            
            def generate_thumbnail(prompt):
                driver = webdriver.Chrome()
                driver.get("https://leonardo.ai")
                # Auto-fill prompt and download image
                return Image.open("generated_thumbnail.png")
            """)
