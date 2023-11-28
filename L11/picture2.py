import cv2
from PIL import Image

image_path = 'cat.jpeg'
image = cv2.imread(image_path)
cat_face_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
cat_face = cat_face_cascade.detectMultiScale(image)
glasses = Image.open('glasses.png')
cat = Image.open(image_path)
glasses = glasses.convert("RGBA")
cat = cat.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w,h//3))
    cat.paste(glasses, (x,y+h//4), glasses)
    cat.save("res.png")
    res = cv2.imread("res.png")
    cv2.imshow("Result", res)
    cv2.waitKey()