from PIL import Image, ImageFont, ImageDraw

# with Image.open('todo_app.png').convert("RGBA") as base:
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", base.size, (255,255,255,0))

#     # getting font
#     font = ImageFont.truetype("Roboto.ttf", 40)

#     # get a drawing context
#     draw = ImageDraw.Draw(txt)
#     # half opacity
#     draw.text((10,10), "Hello", font=font, fill=(255,255,255,128))
#     # full opacity
#     draw.text((10,60), "World", font=font, fill=(255,255,255,255))

#     out = Image.alpha_composite(base, txt)
#     out.show()

with Image.open('todo_app.png').convert("RGBA") as image:
    txt = Image.new("RGBA", image.size, (255,255,255,0))

    draw = ImageDraw.Draw(txt)

    w, h = image.size
    x, y = int(w/3), int(h/3)

    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype("Roboto.ttf", int(font_size/6))

    # addwatermark
    draw.text((x , y), "todo-app", fill=(0, 0, 0), font=font, anchor="ms")

    # add watermark
    draw.text((x, y), "todo_app", fill=(255, 255, 255), font=font, anchor='ms')
    
    watermark_image = Image.alpha_composite(image, txt)
    watermark_image.show()


