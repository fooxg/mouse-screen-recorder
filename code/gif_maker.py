from PIL import Image

def make_gif(name, image_count, framerate = 50, loop_gif = True):
    images = []

    for i in range(0,image_count):
        images.append(Image.open("../img/screen_" + "0"*(5-len(str(i))) + str(i) + ".png"))

    images[0].save("../output/" + name + ".gif",
                   save_all=True, append_images=images[1:], optimize=True, duration=int(1000/framerate), loop=loop_gif)
