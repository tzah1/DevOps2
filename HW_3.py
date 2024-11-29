# 1 2
# try:
#     a = 1 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# 3 yes

# 4
# 5
# 6
# 7 8
# with open("words.txt", "a") as file:
#     # Optionally, write something to the file
#     file.write("Hod Marciano \n")
# # 9
# with open("words.txt", "r") as file:
#     file_read = file.read()
#     print(file_read)

# 10

# 11
from PIL import Image, ImageDraw, ImageFont

# Define image size and color
width, height = 200, 100
background_color = (255, 255, 255)  # White

# Create a blank image
image = Image.new("RGB", (width, height), background_color)

# Draw on the image
draw = ImageDraw.Draw(image)
text = "Hello, Pillow!"
text_color = (0, 0, 0)  # Black
font = ImageFont.load_default()

# Get text size to center it
text_width, text_height = draw.textsize(text, font=font)
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

# Add text to image
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save the image
image.save("image.png")
print("Image saved as 'image.png'")
