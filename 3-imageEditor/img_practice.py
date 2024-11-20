from PIL import Image, ImageFilter, ImageEnhance

with Image.open('./figma.png', 'r') as pic:
    # pic.show()
    black_white = pic.convert("L")
    black_white.save("gray.png")

    mirror = pic.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("mirror.png")

    blur = pic.filter(ImageFilter.BLUR)
    blur.save("blur.png")

    contrast = ImageEnhance.Contrast(pic).enhance(1.5)
    contrast.save("contrast.png")

    ImageEnhance.Color(pic).enhance(2.5).save("color.png")
