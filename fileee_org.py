import os

audio = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".alac", ".aiff", ".opus"]
video = [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp"]
docs = [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt", ".ods", ".odp"]
zips = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".tar.gz", ".tar.bz2"]
software = [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".app", ".apk", ".bat", ".sh", ".bin"]

def organize_files(path):
    os.makedirs(path + "\\audio", exist_ok=True)
    os.makedirs(path + "\\video", exist_ok=True)
    os.makedirs(path + "\\docs", exist_ok=True)
    os.makedirs(path + "\\zips", exist_ok=True)
    os.makedirs(path + "\\software", exist_ok=True)
    os.makedirs(path + "\\unknown", exist_ok=True)

    for root, dirs, files in os.walk(path):
        for file in files:
            extension = os.path.splitext(file)[1].lower()
            if extension == "":
                continue

            if extension in audio:
                dest_path = os.path.join(path, "audio", file)
            elif extension in video:
                dest_path = os.path.join(path, "video", file)
            elif extension in docs:
                dest_path = os.path.join(path, "docs", file)
            elif extension in zips:
                dest_path = os.path.join(path, "zips", file)
            elif extension in software:
                dest_path = os.path.join(path, "software", file)
            else:
                dest_path = os.path.join(path, "unknown", file)

            if os.path.exists(dest_path):
                print(f"File {file} already exists in the destination, skipping...")
            else:
                source_path = os.path.join(root, file)
                os.rename(source_path, dest_path)
                print(f"Moved: {source_path} -> {dest_path}")
