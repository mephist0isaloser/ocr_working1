
# Flask OCR Summarizer

This is a Flask application that allows users to upload images, perform Optical Character Recognition (OCR) on them using Tesseract, and then summarize the extracted text. Additionally, it includes functionality to monitor a directory for newly uploaded images and automatically process them.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/flask-ocr-summarizer.git
   cd flask-ocr-summarizer
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have Tesseract OCR installed on your system:
   - On Windows: Download and install from [here](https://github.com/tesseract-ocr/tesseract).
   - On Linux: Install using your package manager (e.g., `sudo apt-get install tesseract-ocr`).

## Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the upload form to select an image file and submit it.

4. The uploaded image will be processed using OCR, and a summary of the extracted text will be displayed.

## Components

### `app.py`

- The Flask application that handles user requests for uploading images and processing them.

### `main.py`

- Contains functions for extracting text from images using Tesseract OCR and summarizing the extracted text.

### `pyfile1.py`

- Monitors a directory for newly uploaded images and triggers the OCR and summarization process.

## File Structure

```
flask-ocr-summarizer/
│
├── app.py
├── main.py
├── pyfile1.py
├── requirements.txt
├── README.md
└── upload.html
```

## Notes

- This application assumes Tesseract OCR is properly installed and configured on your system.
- Ensure that the directory specified for image uploads (`UPLOAD_FOLDER`) is writable by the application.
- The summarization algorithm used can be adjusted based on your requirements by modifying the `summarize_text()` function in `main.py`.
```

Feel free to modify the paths, descriptions, or any other details to fit your project's structure and requirements.
