# Importing necessary libraries
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os 
import streamlit as st
from PIL import Image

# Loading Google API key from the .env file

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Configuring the Google Generative AI model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to send prompt, image, and input to the Gemini API and get a response
def get_gemini_response(input,image,prompt):
    response = model.generate_content([prompt,image[0],input])
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="BS Extractor")
st.header("BS Extractor")

# Input field for the user prompt

input = st.text_input("Input Prompt : ",key="input")
# File uploader for the user to upload an image of the bank statement
uploaded_file = st.file_uploader("Choose a image of bs ", type=['jpg','png','jpeg'])
image = ""

# Display the uploaded image if present

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

# Button for submitting the request to the AI model

submit = st.button("Tell me about image?")

# Defining the prompt to be sent to the Gemini API
prompt = """
    You are an expert in understanding bankstatements.We will upload an image and bankstatement
    and you will have to answer any questions based on uploaded bankstatement.
"""
# Function to convert the uploaded image to bytes for the AI API
def get_image_bytes(uploaded_image):
    if uploaded_image is not None:
        # read the uploaded image in bytes
        image_bytes = uploaded_image.getvalue()

        image_info = [
            {
            "mime_type": uploaded_image.type,
            "data": image_bytes
        }
        ]
        return image_info
    else:
        raise FileNotFoundError("Upload Valid image file!")

# If the submit button is clicked and input is provided, get the AI response

if submit and input:
    image_data = get_image_bytes(uploaded_file)
    response = get_gemini_response(input,image_data,prompt)
    st.subheader("The response is ")
    st.write(response)