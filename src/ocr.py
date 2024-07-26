import pytesseract
from PIL import Image


def ocr(image_path, lang='eng'):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text



if __name__ == '__main__':
    print(ocr('test_img2.png', lang='dan'))