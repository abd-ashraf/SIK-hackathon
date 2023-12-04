import easyocr
import pandas as pd

# Create a reader instance for Finnish
reader = easyocr.Reader(['fi'])  # 'fi' is the language code for Finnish

# Function to extract text and its location
def extract_text_easyocr(image_path):
    results = reader.read(image_path)
    
    # Convert results to a DataFrame
    df = pd.DataFrame(results, columns=['bbox', 'text', 'confidence'])
    
    # Expand the 'bbox' column into separate columns
    df[['left', 'top', 'right', 'bottom']] = pd.DataFrame(df['bbox'].tolist(), index=df.index)
    
    # Calculate width and height from the bbox coordinates
    df['width'] = df['right'] - df['left']
    df['height'] = df['bottom'] - df['top']
    
    # Select relevant columns
    relevant_data = df[['text', 'left', 'top', 'width', 'height', 'confidence']]
    
    # Drop the now unnecessary 'right' and 'bottom' columns
    relevant_data = relevant_data.drop(columns=['right', 'bottom'])
    
    return relevant_data

# Path to your image
image_path = '005-iPhone13Pro-002.jpg'

# Extract text
extracted_data_easyocr = extract_text_easyocr(image_path)

# Save to CSV
extracted_data_easyocr.to_csv('extracted_text_easyocr.csv', index=False)

print("Text extraction with easyOCR complete. Data saved to 'extracted_text_easyocr.csv'.")
