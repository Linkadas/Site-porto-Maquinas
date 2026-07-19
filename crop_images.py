from PIL import Image
import os
import glob

def crop_to_content(image_path):
    try:
        img = Image.open(image_path).convert("RGBA")
        bbox = img.getbbox()
        if bbox:
            cropped_img = img.crop(bbox)
            cropped_img.save(image_path)
            print(f"Cropped {image_path}")
        else:
            print(f"Empty image {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

if __name__ == "__main__":
    png_files = glob.glob('products/*.png')
    for filepath in png_files:
        crop_to_content(filepath)
    print("Done cropping all images!")
