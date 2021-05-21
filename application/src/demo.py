import image_utils

input_image = "smiling-emoji.jpg"
thumbnail_image = "demo-thumbnail.png"

image = image_utils.image_thumbnail(input_image, (300, 300))
image.save(thumbnail_image)
