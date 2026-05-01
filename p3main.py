#buttons
#file list
#text editor


import tkinter as tk
from tkinter import messagebox
import os
import file_ops

current_path = os.getcwd()

#functions

def refresh():
    path_label.config(text=current_path)
    file_list.delete(0, tk.END)
    files = file_ops.list_files(current_path)

    if isinstance(files, str):
        messagebox.showerror("Error", files)
        return

    for f in files:
        file_list.insert(tk.END, f)


def get_selected_path():
    try:
        selected = file_list.get(file_list.curselection())
        return os.path.join(current_path, selected)
    except:
        messagebox.showerror("Error", "No file selected")
        return None


def open_item(event=None):
    global current_path
    path = get_selected_path()
    if not path:
        return

    if os.path.isdir(path):
        current_path = path
        refresh()
    else:
        open_file()


def open_file():
    path = get_selected_path()
    if not path:
        return

    if os.path.isdir(path):
        messagebox.showerror("Error", "Cannot open a folder as a file")
        return

    content = file_ops.read_file(path)
    open_editor(path, content)



def create_file():
    name = simple_input("Enter file or folder name:")
    if not name:
        return

    choice = messagebox.askyesno("Type", "Create a folder? (Yes = Folder, No = File)")

    path = os.path.join(current_path, name)

    if choice:
        result = file_ops.create_directory(path)
    else:
        result = file_ops.create_file(path)

    messagebox.showinfo("Create", result)
    refresh()


def delete_file():
    path = get_selected_path()
    if not path:
        return

    confirm = messagebox.askyesno("Confirm", "Delete this item?")
    if confirm:
        if os.path.isdir(path):
            result = file_ops.delete_directory(path)
        else:
            result = file_ops.delete_file(path)

        messagebox.showinfo("Delete", result)
        refresh()


def rename_file():
    path = get_selected_path()
    if not path:
        return

    new_name = simple_input("New name:")
    if new_name:
        new_path = os.path.join(current_path, new_name)
        messagebox.showinfo("Rename", file_ops.rename_file(path, new_path))
        refresh()


def go_back():
    global current_path
    parent = os.path.dirname(current_path)
    if parent != current_path:
        current_path = parent
        refresh()


def simple_input(prompt):
    win = tk.Toplevel(root)
    win.title(prompt)

    entry = tk.Entry(win)
    entry.pack()

    result = []

    def submit():
        result.append(entry.get())
        win.destroy()

    tk.Button(win, text="OK", command=submit).pack()
    root.wait_window(win)

    return result[0] if result else None

def open_editor(path, content):
    editor = tk.Toplevel(root)
    editor.title(f"Editing: {os.path.basename(path)}")
    editor.geometry("600x400")

    text_area = tk.Text(editor)
    text_area.pack(fill=tk.BOTH, expand=True)

    text_area.insert("1.0", content)

    def save_changes():
        new_content = text_area.get("1.0", tk.END)
        result = file_ops.update_file(path, new_content)
        messagebox.showinfo("Save", result)

    tk.Button(editor, text="Save", command=save_changes).pack()


#gui

root = tk.Tk()
root.title("File Manager")


path_label = tk.Label(root, text=current_path)
path_label.pack()

file_list = tk.Listbox(root, width=40)
file_list.pack(side=tk.LEFT, fill=tk.Y)

#navigation
file_list.bind("<Double-Button-1>", open_item)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Back", command=go_back).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Refresh", command=refresh).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Open", command=open_file).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Create", command=create_file).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Delete", command=delete_file).pack(side=tk.LEFT)
tk.Button(btn_frame, text="Rename", command=rename_file).pack(side=tk.LEFT)

refresh()
root.mainloop()