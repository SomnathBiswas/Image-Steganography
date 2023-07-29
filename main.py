import cv2
from random import randint

#Alphabet List 
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~`!@#$%^&*()_+-=.,'*/ "

# img_data = cv2.imread('BG.png')


def encrypt(mes, img):
    img_data = cv2.imread(img, 1)
    num = []
    locs = []

    for i in mes:
        num.append(alpha.index(i))
    for i in range(len(num)):
        locs.append((randint(0, len(img_data) - 1), randint(0, len(img_data[0]) - 1), randint(0, 2)))
    for i, j in zip(locs, num):
        img_data[i[0]][i[1]][i[2]] = j
    
    return cv2.imwrite('encrypted.png', img_data), locs

def decrypt(img, locs):
    img_data = cv2.imread(img, 1)
    str_ = ""
    for i in locs:
        str_ += alpha[img_data[i[0]][i[1]][i[2]]]
    
    return str_


img_new, locs = encrypt('HI', 'CODE.png')

print(decrypt('encrypted.png', locs))
