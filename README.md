# Text Extraction From Driving License

## Tools Used(BACKEND)

1. Flask
2. Tesseract OCR
3. GEMINI API

### Flask

Flask is the backend framework used to create and manage apis. It makes managing data consumption and sending easy.

### Tesseract Optical Character Recognition(OCR)

Tesseract OCR is used to extract text from the image. All the text from the image is extracted and is send to Gemini api.

### GEMINI API

Driving license varies from State to State in India. The text in the license varies from State to State as well. So to make the extracted data more consistent when sending data to the frontend Gemini API is used to get the required values from the list of extracted words.

## Instruction to execute Backend

1. Download and install Tesseract. Also make sure to add it to the PATH variable to access in the terminal. You can follow a tutorial on youtube.
2. Install all the required packages for running the project using `pip install -r requirements.txt`
3. Run the project using `python route.py`
