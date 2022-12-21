from PIL import Image

def convert_image(image_path):
    image = Image.open(image_path)

    if image.mode != 'RGB':
        image = image.convert('RGB')

    width, height = image.size
    
    hsl_image = Image.new(image.mode, image.size)


    for x in range(width):
        for y in range(height):

            r, g, b = image.getpixel((x, y))


            h, s, l = rgb_to_hsl(r, g, b)


            hsl_image.putpixel((x, y), (int(h), int(s * 255), int(l * 255)))


    hsl_image.save('hsl_image.jpg')


def rgb_to_hsl(r, g, b):

    r /= 255
    g /= 255
    b /= 255


    max_color = max(r, g, b)
    min_color = min(r, g, b)


    if max_color == min_color:
        hue = 0
    elif max_color == r:
        hue = (60 * (g - b) / (max_color - min_color)) % 360
    elif max_color == g:
        hue = 60 * (b - r) / (max_color - min_color) + 120
    elif max_color == b:
        hue = 60 * (r - g) / (max_color - min_color) + 240


    lightness = (max_color + min_color) / 2


    if lightness == 0 or max_color == min_color:
        saturation = 0
    elif lightness > 0 and lightness <= 0.5:
        saturation = (max_color - min_color) / (2 * lightness)
    elif lightness > 0.5:
        saturation = (max_color - min_color) / (2 - 2 * lightness)

    return (hue, saturation, lightness)

convert_image('picture1.jpg')