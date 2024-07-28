import os
import json
from PIL import Image

# Define paths
input_folder = 'src'
output_folder = 'dist'
watermark_path = 'watermark.png'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

watermark = Image.open(watermark_path)
watermark_width, watermark_height = watermark.size

# List to store paths of watermarked images
watermarked_images = []

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        image_width, image_height = image.size
        # Ensure the watermark is in the center of the target image
        x = (image_width - watermark_width) // 2
        y = (image_height - watermark_height) // 2
        # Copying the original image to avoid tampering the original image
        watermarked_image = image.copy()
        watermarked_image.paste(watermark, (x, y), watermark)
        output_path = os.path.join(output_folder, filename)
        watermarked_image.save(output_path)
        watermarked_images.append(output_path)
        print(f'Watermarked {filename} and saved to {output_path}')

# Print the JSON array of all watermarked images
print(json.dumps(watermarked_images, indent=4))
