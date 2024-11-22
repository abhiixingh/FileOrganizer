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
 ![source1](D:/python/Project/file organizer/images/source1.png)

2.-
 ![first3](D:/python/Project/file organizer/images/first3.png)

3.-
 ![last4](D:/python/Project/file organizer/images/last4.png)

4.-
 ![location](D:/python/Project/file organizer/images/location.png)

5.-
 ![organized](D:/python/Project/file organizer/images/organized.png)

6.- 
 ![correctfiles](D:/python/Project/file organizer/images/correctfiles.png)