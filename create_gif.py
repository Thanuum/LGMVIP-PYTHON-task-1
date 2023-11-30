# Create a GIF using python

import imageio

filenames = ['image1.jpg', 'image2.jpg']
images = [ ]

for filename in filenames:
  images.append(imageio.imread(filename))

imageio.mimsave('v.gif', images, duration=1000,loop=50)
