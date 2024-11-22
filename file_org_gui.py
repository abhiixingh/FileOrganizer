import tkinter as tk
from tkinter import filedialog, messagebox
from fileee_org import organize_files

def browse_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)

def start_organizing():
    path = path_entry.get()
    if not path or not os.path.isdir(path):
        messagebox.showerror("Error", "Please select a valid folder path.")
        return
    try:
        organize_files(path)
        messagebox.showinfo("Success", "Files have been organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

path_label = tk.Label(frame, text="Select Folder:")
path_label.grid(row=0, column=0, padx=10, pady=5)

path_entry = tk.Entry(frame, width=40)
path_entry.grid(row=0, column=1, padx=10, pady=5)

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=5)

start_button = tk.Button(root, text="Organize Files", command=start_organizing, bg="green", fg="white")
start_button.pack(pady=20)

root.mainloop()
