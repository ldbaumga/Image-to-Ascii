import sys
import PIL.Image

ASCII_STR = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
ASCII_STR2 = "@#S%?*+;:,."
ASCII_CHAR = list(ASCII_STR2)


def resize_image(image, new_width=100):
    width, hight = image.size
    ratio = hight / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def greyify(image):
    greyscale_image = image.convert("L")
    return greyscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    maxVal = -(max(pixels) // -len(ASCII_CHAR))
    characters = ""
    for pixel in pixels:
        if pixel == 0:
            characters += ' '
        else:
            characters += ASCII_CHAR[pixel // maxVal]
    return characters


def main():
    inputPath = input("Path to Image:")
    new_width = int(input("New width: "))

    try:
        image = PIL.Image.open(inputPath)
    except:
        print(inputPath, "is not a valid path to an image")
        sys.exit()

    new_image_data = pixels_to_ascii(greyify(resize_image(image, new_width)))

    pixel_count = len(new_image_data)
    ascii_image = ""
    for i in range(0, pixel_count, new_width):
        ascii_image += "\n" + new_image_data[i : (i + new_width)]
    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


if __name__ == "__main__":
    main()
