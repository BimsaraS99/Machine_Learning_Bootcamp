import os
from PIL import Image, ImageDraw
import numpy as np

# Parameters
image_size = 100
num_images_per_class = 10
output_dir = "testset"
shape_size = 40  # Fixed shape size

os.makedirs(f"{output_dir}/0", exist_ok=True)
os.makedirs(f"{output_dir}/1", exist_ok=True)

def generate_image_with_random_position(label):
    img = Image.new("L", (image_size, image_size), color=0)  # Black background
    draw = ImageDraw.Draw(img)
    
    # Random top-left coordinate ensuring shape fits inside the image
    max_pos = image_size - shape_size
    top_left_x = np.random.randint(0, max_pos)
    top_left_y = np.random.randint(0, max_pos)
    bottom_right_x = top_left_x + shape_size
    bottom_right_y = top_left_y + shape_size
    
    if label == 0:
        # Draw square
        draw.rectangle([top_left_x, top_left_y, bottom_right_x, bottom_right_y], fill=255)
    else:
        # Draw circle
        draw.ellipse([top_left_x, top_left_y, bottom_right_x, bottom_right_y], fill=255)
    
    return img

for label in [0, 1]:
    for i in range(num_images_per_class):
        img = generate_image_with_random_position(label)
        img.save(f"{output_dir}/{label}/img_{i}.png")

print("✅ Dataset with fixed-size shapes at random positions generated!")
