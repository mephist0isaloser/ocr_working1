from PIL import Image
import pytesseract
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
import nltk

# Download necessary NLTK data packages if not already installed
# nltk.download('punkt')
# nltk.download('stopwords')

# Your existing code for OCR and summarization...


def extract_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


def summarize_text(text, sentences_count=4, language="english"):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = Summarizer()
    summarizer.stop_words = nltk.corpus.stopwords.words(language)

    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])


def ocr_notes_summarizer(image_path):
    # Extract text from the image
    extracted_text = extract_text(image_path)
    print("Extracted Text:\n", extracted_text)

    # Summarize the extracted text
    summary = summarize_text(extracted_text)
    print("\nSummary:\n", summary)


# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Example usage
#image_path = 'img1.png'  # Replace with your image path
#ocr_notes_summarizer(image_path)
