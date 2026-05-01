#create_file()
#read_file()
#delete_file
#rename_file

#core features: create file, read file, update file, delete file, 
# rename file, navigate directories

import os

def list_files(path):
    try:
        return os.listdir(path)
    except Exception as e:
        return str(e)
    
def create_file(path, content =" "):
    if os.path.exists(path):
        return "File aalready exists."
    try:
        with open(path, "w") as f:
            f.write(content)
        return "File created."
    except Exception as e:
        return str(e)
    
def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)
    
def update_file(path, content):
    try:
        with open(path, "w") as f:
            f.write(content)
        return "File updated."
    except Exception as e:
        return str(e)

def delete_file(path):
    try:
        os.remove(path)
        return "File deleted."
    except Exception as e:
        return str(e)
    
def rename_file(old,new):
    try:
        os.rename(old, new)
        return "File renamed."
    except Exception as e:
        return str(e)
    
def create_directory(path):
    try:
        os.mkdir(path)
        return "Directory created."
    except Exception as e:
        return str(e)

def delete_directory(path):
    try:
        os.rmdir(path)
        return "Directory deleted."
    except Exception as e:
        return str(e)