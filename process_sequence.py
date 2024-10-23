import os
from PIL import Image

def process_images():
    source_dir = r"c:\Users\pieta\Documents\GitHub\homepage\assets\gfx"
    files = sorted([f for f in os.listdir(source_dir) if f.startswith("Image Sequence") and f.endswith(".jpg")])
    
    print(f"Found {len(files)} images.")

    for i, filename in enumerate(files):
        old_path = os.path.join(source_dir, filename)
        new_filename = f"helsinki_slide_{i+1}.webp"
        new_path = os.path.join(source_dir, new_filename)
        
        try:
            with Image.open(old_path) as img:
                # Resize if too big (optional, but good for web)
                if img.width > 1920:
                    ratio = 1920 / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
                
                img.save(new_path, "WEBP", quality=85)
                print(f"Converted {filename} to {new_filename}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    process_images()
