import os
import re

REPO_ROOT = "/home/director/villa-thaifa"
IGNORE_DIRS = {'.git', '.claude', '.gemini', '.venv', 'node_modules', '__pycache__', 'tmp'}
ROOM_KEYWORDS = [r'\bR0[1-9]\b', r'\bR1[0-2]\b', r'(?i)deluxe triple', r'(?i)presidential suite', r'(?i)chambre double']

def audit_repo():
    scattered_files = []
    
    # Compile regexes
    patterns = [re.compile(kw) for kw in ROOM_KEYWORDS]
    
    for root, dirs, files in os.walk(REPO_ROOT):
        # Mutate dirs in-place to ignore certain directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            # Skip non-text files based on extension for safety (basic check)
            if not file.endswith(('.md', '.json', '.yaml', '.yml', '.txt', '.csv')):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, REPO_ROOT)
            
            # We EXPECT room data to be in data/rooms/ or ops/archive/
            # If it's elsewhere, we want to know about it.
            if rel_path.startswith('data/rooms/') or rel_path.startswith('ops/archive/'):
                continue
                
            # Check file name first
            if 'room' in file.lower() or 'chambre' in file.lower():
                scattered_files.append((rel_path, "Filename matches room/chambre"))
                continue
                
            # Check content
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in patterns:
                        if pattern.search(content):
                            scattered_files.append((rel_path, f"Content matches keyword: {pattern.pattern}"))
                            break # Move to next file
            except Exception:
                pass # Ignore files we can't read

    return scattered_files

if __name__ == "__main__":
    findings = audit_repo()
    if not findings:
        print("✅ SUCCESS: No scattered room data found outside `data/rooms/` (and archives).")
    else:
        print(f"⚠️ FOUND {len(findings)} POTENTIALLY SCATTERED FILES:")
        for path, reason in findings:
            print(f" - {path} ({reason})")
