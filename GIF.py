import imageio.v2 as imageio

filenames = ['Python Projects/GIF/TamGIF_1.png',
             'Python Projects/GIF/TamGIF_2.png',
             'Python Projects/GIF/TamGIF_3.png',
             'Python Projects/GIF/TamGIF_4.png'
             ]
images = []

for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('Bicho.gif', images, duration = 0.25)

