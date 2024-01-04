from PIL import ImageFont, Image, ImageDraw, ImageChops, ImageOps,features

print ("RAQM Status: ",features.check('raqm'))
w, h = 64, 64
w0, h0 = 256, 256
blank = Image.new('L', (w0 * 5, h0 * 3), 255)
font = 'siyam.ttf'
font = ImageFont.truetype(font=font, size=20, layout_engine=ImageFont.Layout.RAQM)
char = 'হানিফ আলী সোহাগ'
img = Image.new("L", (w0 * 5, h0 * 3), 255)
draw = ImageDraw.Draw(img)
draw.text((w0, h0), char, font=font)
diff = ImageChops.difference(img, blank)
lx, ly, hx, hy = diff.getbbox()
img = img.crop((lx, ly, hx, hy))

# Display the image
img.show()

# Save the image
img.save('image.png')

