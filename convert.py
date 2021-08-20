from PIL import Image
from PIL import Image
import os

def make_square(input_image, fill_color=(0, 0, 200), min_size=300):
    x, y = input_image.size
    size = max(min_size, x, y)

    new_input_image = Image.new('RGB', (size, size), fill_color)
    new_input_image.paste(input_image, (int((size - x) / 2), int((size - y) / 2)))

    return new_input_image


# for file in os.listdir("./data/Roofs/input/"):
#     im1 = Image.open("./data/Roofs/input/" + file)
#     im1 = im1.convert('RGB')
#     im1.save("./data/roof/input/" + file[:-3] + "jpg")
#
#     im1 = Image.open("./data/Roofs/real/" + file)
#     im1 = im1.convert('RGB')
#     im1.save("./data/roof/real/" + file[:-3] + "jpg")

for file in os.listdir("./data/dataset1"):
    if file[-3:] == "jpg":
        im1 = Image.open("./data/dataset1/" + file)

        make_square(im1,(0,0,0)).save("./data/combined_dataset/real/" + file)

    if file[-3:] == "png":
        im1 = Image.open("./data/dataset1/" + file)
        im1 = im1.convert('RGB')

        make_square(im1,(0,0,0)).save("./data/combined_dataset/input/" + file[:-3] + "jpg")

# for file in os.listdir("./data/dataset2/trainA"):
#     im1 = Image.open("./data/dataset2/trainA/" + file)
#     im1.save("./data/combined_dataset/real/" + file.replace("_A", ""))
#     im1 = Image.open("./data/dataset2/trainB/" + file.replace("_A", "_B"))
#     im1.save("./data/combined_dataset/input/" + file.replace("_A", ""))
#
# for file in os.listdir("./data/dataset2/testA"):
#     im1 = Image.open("./data/dataset2/testA/" + file)
#     im1.save("./data/combined_dataset/real/" + str(len(os.listdir("./data/dataset2/trainA")) + int(file[:-4])) + '.jpg')
#     im1 = Image.open("./data/dataset2/testB/" + file)
#     im1.save("./data/combined_dataset/input/" + str(len(os.listdir("./data/dataset2/trainA")) + int(file[:-4])) + '.jpg')