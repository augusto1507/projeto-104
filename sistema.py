import cv2

img=cv2.imread("solar-system.jpg")

sol="sol"

mercurio="mercurio"

venus="venus"

terra="terra"

marte="marte"

jupter="jupter"

saturno="saturno"

urano="urano"

netuno="netuno"


cv2.putText(img, sol, (100, 80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1.0, color=(0,0,255) )

cv2.putText(img, mercurio, (120, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, venus, (200, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, terra, (300, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, marte, (400, 160), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, jupter, (500, 60), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, saturno, (700, 120), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, urano, (950, 140), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.putText(img, netuno, (1100, 140), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(0,0,255) )

cv2.imshow("tela",img)

cv2.waitKey(0)