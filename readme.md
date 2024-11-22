File Organizer:-
This Python script categorizes files in a specified directory into broad folders by file extensions. The script will automatically scan the subdirectories and move each file to the appropriate folder: audio, video, docs, zips, software, or unknown.

Characteristics:-
-Automatic categorization: File is categorized under audio, video, documents, and the like by the file extension.
-Nested Directory Support: Recursively scans subfolders, organizing files regardless of their depth in the directory structure.
-Duplicate Handling: It will search for the presence of duplicate files in the destination folder. Once locating, it will bypass their movement.

Folder Structure:-
Now, after it has executed the script, that generates folders within a specified directory:

-Audio: For audio files(.mp3, .wav, .aac, etc.)
-video: For video file types (.mp4, .mkv, .avi, etc.)
-docs: For document files (.pdf, .docx, .txt, etc.)
-zips Files end per compressed (.zip, .rar, .7z, etc.)
-software: executable and installation files (.exe, .msi, .apk, etc.)
-unknown: For files with unsupported or unknown file extensions


Usage:-
Requirement-
Python 3.x
OS: Windows. Adapt paths as needed to other OSs

How to Use:-
Set directory path: Within the above lines of code, the path variable gets assigned the desired directory to be arranged.

path = "D:\\python\Project\file organizer\sample folder nested"
Run the Script: Run the script with Python:
python file_organizer.py Running After file reorganization in the chosen directory, the files get automatically arranged into the proper folders.

Example
After running the script, a directory with files of various types will transform as follows:

-Initial Directory
-Organized Directory

Code Overview:-
 The main function, organize_files(), scans through each file in the specified directory and its subdirectories by using os.walk(). According to the file type, it moves every file into the corresponding category folder. If the file is already found in the destination folder, it skips moving and indicates you, showing a completion notice for not moving the file. 
 
 Error Handling:-
 If the target file exists in the folder, it will print a message and skip that movement for the file.


 sample images:-
1.-
![location](https://github.com/user-attachments/assets/9ad10bec-46dd-4f50-90ba-00d94a07305f)

2.-
![organized](https://github.com/user-attachments/assets/46e792f4-7c28-4bcd-a409-d64efa8fbb27)

3.-
![source1](https://github.com/user-attachments/assets/665c4b85-cdd7-40f5-97c2-d7e74073d31b) 

4.-
![correctfiles](https://github.com/user-attachments/assets/dbf7ba97-34a8-48f2-890d-4806da91baef) 

5.-
![first3](https://github.com/user-attachments/assets/073dada5-f1fa-4996-872d-259e3dd08cab) 

6.- 
![last4](https://github.com/user-attachments/assets/a71f6556-67fa-44de-9cbb-69cee731a4dc)
