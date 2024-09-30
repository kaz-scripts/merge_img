from PIL import Image
import os

folder_path = 'images'
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')], key=lambda x: int(os.path.splitext(x)[0]))

images = [Image.open(os.path.join(folder_path, file)) for file in image_files]

widths, heights = zip(*(img.size for img in images))

total_height = sum(heights)

new_image = Image.new('RGB', (max(widths), total_height))

y_offset = 0
for img in images:
    new_image.paste(img, (0, y_offset))
    y_offset += img.height

new_image.save('output_image.png')
