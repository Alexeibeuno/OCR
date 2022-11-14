try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text
