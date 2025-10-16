import streamlit as st
import gemini_api

st.title("AI Fashion Styler")


# UI Components

# 1. Fabric Upload
fabric_image = st.file_uploader("Upload Fabric", type=["png", "jpg", "jpeg"])

# 2. Garment Type Dropdown
garment_type = st.selectbox(
    "Garment Type",
    ["saree", "lehenga", "kurta", "dress", "gown"]
)

# 3. Model Upload
model_image = st.file_uploader("Upload Model/Mannequin Image", type=["png", "jpg", "jpeg"])

# 4. Styling Options
st.header("Styling Options")

drape_style = st.selectbox(
    "Draping Style",
    ["Nivi", "Bengali", "Lehenga style", "Gujarati", "Maharashtrian"]
)

accessories = st.multiselect(
    "Accessories",
    ["jewelry", "belt", "dupatta", "handbag", "sunglasses"]
)

view_type = st.selectbox(
    "View Type",
    ["Full body", "Portrait", "Back view"]
)

# Generate Button
if st.button("Generate Style"):
    if fabric_image and model_image:
        st.write("Generating your styled outfit...")
        
        # Convert accessories list to a string
        accessories_str = ", ".join(accessories) if accessories else "none"
        
        # Call the Gemini API function
        generated_image = gemini_api.generate_image(
            fabric_image=fabric_image,
            model_image=model_image,
            garment_type=garment_type,
            drape_style=drape_style,
            accessories=accessories_str,
            view_type=view_type
        )
        
        if generated_image:
            st.image(generated_image, caption="Your AI Styled Outfit", use_container_width=True)
        else:
            st.error("Failed to generate image. Please check the console for errors.")
    else:
        st.warning("Please upload both a fabric and a model image.")


