
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



def generate_image(fabric_image, model_image, prompt):
    """
    Generates an image using the Gemini 2.5 Flash Image model with image generation capabilities.
    This version uses a text prompt and a fabric image to influence the color.
    """
    try:
        # The model to use for image generation
        model = genai.GenerativeModel('gemini-2.5-flash-image')

        fabric_image_pil = PIL.Image.open(fabric_image)

        # The prompt to send to the model
        full_prompt = f"{prompt}. The color of the output should be the same as the provided fabric image."

        # Call the model to generate content from the text prompt and fabric image
        response = model.generate_content([full_prompt, fabric_image_pil])



        # The response for this model should contain image data.
        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    image_data = part.inline_data.data
                    return io.BytesIO(image_data)

        # If no image, maybe there is text? Print it for debugging.
        if hasattr(response, 'text') and response.text:
            print(f"No image data in response. Response: {response.text}")
        else:
            print("No image data in response and no text either.")
        return None



    except Exception as e:

        print(f"An error occurred during image generation: {e}")

        return None
