import sys  #used to access command line argument

from PIL import Image   #using Pillow library to treat those files as images

images = []     #using a list to accummulate the images

#ln 8-10 use of loop to iterate
for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

#Save the first image and append other images together
images[0].save(
    "costumes.git", save_all=True, append_images=[images[1]], duration=200, loop=0
)