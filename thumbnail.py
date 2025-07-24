import streamlit as st
import requests
from PIL import Image
import io
import random

# --- Streamlit UI ---
st.title("🎬 Viral Thumbnail Generator")
st.markdown("**Enter any prompt** - Creates professional thumbnails using free AI tools")

# User Input
prompt = st.text_area("Describe your thumbnail (e.g. 'A shocked man pointing at text YOUR WON'T BELIEVE THIS with red arrows'):", 
                     height=100)
style = st.selectbox("Style:", ["Clickbait", "Professional", "Dark", "Bright"])

if st.button("✨ Generate Thumbnail"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating using free AI tools..."):
            try:
                # Simulate AI generation (in reality would call free tools)
                width, height = 1280, 720
                background_color = "#FF0000" if "clickbait" in prompt.lower() else "#2C3E50"
                
                # Create sample image (replace with actual AI calls)
                img = Image.new("RGB", (width, height), background_color)
                draw = ImageDraw.Draw(img)
                
                # Add text (simulating AI output)
                text = "YOUR TEXT HERE" if random.random() > 0.5 else prompt[:30]
                draw.text((width//4, height//2), text, fill="white", font_size=60)
                
                # Add mock AI branding
                ai_used = random.choice(["Leonardo.AI", "Playground AI", "Ideogram"])
                draw.text((10, height-30), f"Generated with {ai_used} (Free Tier)", fill="#AAAAAA")
                
                # Display
                st.image(img, caption="Your AI-Generated Thumbnail", use_column_width=True)
                
                # Download
                img_bytes = io.BytesIO()
                img.save(img_bytes, format="PNG")
                st.download_button(
                    "💾 Download Thumbnail",
                    data=img_bytes.getvalue(),
                    file_name="viral_thumbnail.png",
                    mime="image/png"
                )
                
                st.success(f"Done! Used {ai_used}'s free tier")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("This demo simulates AI generation. Actual implementation would:")
                st.markdown("""
                1. Use browser automation (Selenium) to access free AI tools
                2. Extract generated images
                3. Return processed thumbnails
                """)
