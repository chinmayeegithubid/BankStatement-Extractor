# Bank Statement Extractor - End-to-End Generative AI Project

## Overview
This project demonstrates how to build an end-to-end Bank Statement Extractor using Google Gemini (Generative AI) and Streamlit. The user can upload a bank statement image and provide a prompt, and the model will respond with relevant information based on the image and prompt.

## Project Flow

1. **Input Prompt**: The user provides an input text (query) related to the bank statement.
2. **Upload Image**: The user uploads an image of the bank statement (JPG, PNG, JPEG).
3. **Google Generative AI Model**: The uploaded image and input prompt are sent to Google Gemini, which generates a response based on the provided input.
4. **Response**: The model's generated response is displayed in the Streamlit app.

## Features
- **User Input**: Allows the user to input a custom query.
- **Image Upload**: Accepts image files of type JPG, PNG, or JPEG.
- **Generative AI**: Uses Google Gemini (Generative AI) to generate responses based on the input and uploaded image.
  
## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bank-statement-extractor.git

2. Set up a virtual environment
python -m venv env
source env/bin/activate  # macOS/Linux
.\env\Scripts\activate   # Windows
3. Install the required dependencies
pip install -r requirements.txt
4. Set up your Google API Key
Get a Google API key from Google Cloud.
Create a .env file and add your key:
GOOGLE_API_KEY=your-google-api-key-here
5. Run the Streamlit app
streamlit run app.py
6. Access the app
Open your browser and go to http://localhost:8501
Code Explanation
Google API Setup: The dotenv library is used to load the API key from an .env file.
Streamlit Web App: The app provides an input box for a prompt and a file uploader for the image. Once both are provided, the app sends this data to Google Generative AI.
Response Generation: The AI model processes the image and the prompt and returns a response.
Example Input
Prompt: "Tell me the total amount credited in the last month."
Example Output:
Response: "The total amount credited in the last month is $5000."
Dependencies
Python 3.8+
Streamlit
Pillow
python-dotenv
google-generativeai