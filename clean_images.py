import os
from rembg import remove
from PIL import Image

products_dir = './products'
print("Starting background removal...")

for filename in os.listdir(products_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        filepath = os.path.join(products_dir, filename)
        print(f"Processing {filename}...")
        
        try:
            input_img = Image.open(filepath)
            
            # Remove background
            output_img = remove(input_img)
            
            # Create a new white background image
            new_bg = Image.new("RGB", output_img.size, (255, 255, 255))
            
            # Paste the transparent image on top of the white background
            # The third argument is the mask (alpha channel)
            new_bg.paste(output_img, (0, 0), output_img)
            
            # Save it back to the original file
            new_bg.save(filepath, format=input_img.format)
            print(f"Successfully processed {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All images processed successfully!")
