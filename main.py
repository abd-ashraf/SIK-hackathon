import pytesseract
from PIL import Image
import pandas as pd

# Configure Tesseract to use Finnish language
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
tessdata_dir_config = '--tessdata-dir "/opt/homebrew/Cellar/tesseract-lang/4.1.0/share/tessdata" -l fin'

# Function to extract text and its location
def extract_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    data = pytesseract.image_to_data(img, config=tessdata_dir_config, output_type=pytesseract.Output.DATAFRAME)

    # Filter out rows where text is not detected
    text_data = data[data.text.notnull()]

    # Selecting relevant columns
    relevant_data = text_data[['text', 'left', 'top', 'width', 'height']]

    return relevant_data

# Path to your image
image_path = '010-droneDJIM3-002.jpg'

# Extract text
extracted_data = extract_text(image_path)

# Save to CSV
extracted_data.to_csv('extracted_text_010-droneDJIM3-002.csv', index=False)

print("Text extraction complete. Data saved to 'extracted_text.csv'.")
