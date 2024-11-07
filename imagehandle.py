import cv2
import pytesseract
import numpy as np
def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

#get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#noise removal function
def remove_noise(image):
    return cv2.medianBlur(image,5)

#thresholding
def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

def get_text(img):
    # Convert PIL image to OpenCV format
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # Process the image with OpenCV
    img_cv = get_grayscale(img_cv)
    img_cv = thresholding(img_cv)
    #img_cv = remove_noise(img_cv)
    img_cv = deskew(img_cv)
    text = pytesseract.image_to_string(img_cv)
    print("Extracted Text:", text)
    res=ocr_core(img)
    return res