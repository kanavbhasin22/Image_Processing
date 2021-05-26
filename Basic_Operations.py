import cv2

img=cv2.imread('Microsoft.jpg')
img2=cv2.imread('Temple.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

#dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,0.5,img2,0.5,0)
cv2.imshow('image',dst)
cv2.waitKey()
cv2.destroyAllWindows()