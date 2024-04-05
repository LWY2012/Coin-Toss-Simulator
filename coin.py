import matplotlib.pyplot as plt
import random
from PIL import Image

try:
    times = int(input('Times?'))
except ValueError:
    print('Error type,re-enter')
    times = int(input('Times?'))

img1 = Image.open('Obverse side.png')#your coin picture path
img2 = Image.open('flip side.png') #your coin picture path


for i in range(times):
    a=random.randint(1,2)

    if a==1:
        plt.subplot(121)
        plt.imshow(img1)
        plt.axis('off')
    if a==2:
        plt.subplot(122)
        plt.imshow(img2)
        plt.axis('off')
    plt.tight_layout()
    plt.show()
