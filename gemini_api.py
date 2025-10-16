
import os
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image
import io

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the generative AI model
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    print("Gemini API key not found. Please set it in the .env file.")

def generate_image(fabric_image, model_image, garment_type, drape_style, accessories, view_type):
    """
    Generates an image using the Gemini 2.5 Flash model with image generation capabilities.
    """
    try:
        # The model to use for image generation
        model = genai.GenerativeModel('gemini-2.5-flash-image')

        # Open the uploaded images
        fabric_img = PIL.Image.open(fabric_image)
        model_img = PIL.Image.open(model_image)

        # The prompt to send to the model
        prompt = f"Apply this uploaded fabric to the model. Create a realistic {garment_type} with {drape_style}, include {accessories}, show {view_type}."

        # The content to send to the model, including the prompt and the images
        contents = [prompt, fabric_img, model_img]

        # Call the model to generate content
        response = model.generate_content(contents)

        # The response for this model should contain image data.
        # This part of the code assumes the response structure for image generation.
        # It might need adjustment based on the actual API response.
        if response.parts:
            # Assuming the first part is the generated image
            image_data = response.parts[0].inline_data.data
            return io.BytesIO(image_data)
        else:
            print("Error: No image data found in the response.")
            return None

    except Exception as e:
        print(f"An error occurred during image generation: {e}")
        return None

