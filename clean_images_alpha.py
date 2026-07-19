import os
from rembg import remove
from PIL import Image

products_dir = './products'
print("Starting transparent background removal...")

for filename in os.listdir(products_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.webp')):
        filepath = os.path.join(products_dir, filename)
        # Create a new filename with .png extension
        new_filename = filename.rsplit('.', 1)[0] + '.png'
        new_filepath = os.path.join(products_dir, new_filename)
        
        print(f"Processing {filename}...")
        
        try:
            input_img = Image.open(filepath)
            
            # Remove background (outputs transparent RGBA)
            output_img = remove(input_img)
            
            # Save as PNG to preserve transparency
            output_img.save(new_filepath, format="PNG")
            print(f"Successfully processed {filename} to {new_filename}")
            
            # If the original wasn't .png, delete it so we don't have duplicates
            if filepath != new_filepath:
                os.remove(filepath)
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All images processed successfully!")
