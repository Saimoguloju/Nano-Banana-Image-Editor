import streamlit as st
import gemini_api

st.title("AI Fashion Styler")


# UI Components

# 1. Fabric Upload
fabric_image = st.file_uploader("Upload Fabric", type=["png", "jpg", "jpeg"])

garment_type = st.selectbox(
    "Garment Type",
    ["saree", "lehenga", "kurta", "dress", "gown"]
)

# 2. Model Upload
model_image = st.file_uploader("Upload Model/Mannequin Image", type=["png", "jpg", "jpeg"])

# 3. Styling Prompt
prompt = st.text_area("Enter a detailed description of the outfit you want to create.")


# Generate Button
if st.button("Generate Style"):
    if fabric_image and model_image and prompt:
        st.write("Generating your styled outfit...")
        
        full_prompt = f"Create a high-resolution, photorealistic image of a model wearing a {garment_type}. The garment should be made from the provided fabric image. {prompt}. The model's face in the output image must be the same as in the provided model image. The final image should be clear, professionally lit, and look like a fashion photograph."

        # Call the Gemini API function
        generated_image = gemini_api.generate_image(
            fabric_image=fabric_image,
            model_image=model_image,
            prompt=full_prompt
        )

        

        if generated_image:

            st.image(generated_image, caption="Your AI Styled Outfit", width='stretch')

            generated_image.seek(0)
            st.download_button(
                label="Download Image",
                data=generated_image,
                file_name="styled_outfit.png",
                mime="image/png"
            )

        else:

            st.error("Failed to generate image. Please check the console for errors.")

    else:

        st.warning("Please upload a fabric image, a model image, and enter a prompt.")
