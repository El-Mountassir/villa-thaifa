import os
import shutil
import re

TEXT_EXTENSIONS = {'.md'}
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.pdf'}

def organize_room_images(base_dir):
    if not os.path.exists(base_dir):
        print(f"Directory not found: {base_dir}")
        return

    for item in os.listdir(base_dir):
        room_dir = os.path.join(base_dir, item)
        if not os.path.isdir(room_dir):
            continue

        print(f"Processing room: {item}")
        
        images_dir = os.path.join(room_dir, "images")
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
            print(f"  Created images directory: {images_dir}")

        moved_files = {}

        # Move files
        for filename in os.listdir(room_dir):
            file_path = os.path.join(room_dir, filename)
            if not os.path.isfile(file_path):
                continue
            
            ext = os.path.splitext(filename)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                new_path = os.path.join(images_dir, filename)
                shutil.move(file_path, new_path)
                moved_files[filename] = f"images/{filename}"
                print(f"  Moved: {filename} -> images/{filename}")

        # Update Markdown links
        for filename in os.listdir(room_dir):
            if filename.endswith(".md"):
                md_path = os.path.join(room_dir, filename)
                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                updated_content = content
                for old_name, new_rel_path in moved_files.items():
                    # Regex to match markdown image links: ![...](filename) or just (filename)
                    # Be careful not to replace if already in images/
                    
                    # Pattern 1: Standard markdown image ![alt](url)
                    # We look for (filename) and replace with (images/filename)
                    pattern = re.compile(re.escape(f"({old_name})"))
                    updated_content = pattern.sub(f"(images/{old_name})", updated_content)
                    
                    # Pattern 2: HTML img tag <img src="filename" ...>
                    pattern_html = re.compile(r'src=["\']' + re.escape(old_name) + r'["\']')
                    updated_content = pattern_html.sub(f'src="images/{old_name}"', updated_content)

                if updated_content != content:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"  Updated links in: {filename}")

if __name__ == "__main__":
    base_dir = "docs/content/pending/reference/rooms"
    organize_room_images(base_dir)
