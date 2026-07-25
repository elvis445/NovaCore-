import os
import subprocess


def open_foldeer(path):
    try:

        os.startfile(path)
        return "File opened"
    except:
        return "Folder not found"


def create_file(filename):
    try:
        with open(filename, "w")as file:
            file.write("Created by NovaCore\n")
        return "File created successfully."
    except:
        return "Unable to create file."


def read_file(filename):
    try:
        with open(filename, "r")as file:
            return file.read()
    except:
        return "File not found"


def delete_file(filename):
    try:
        os.remove(filename)
        return "File deleted successfully."
    except:
        return "Unable to delete file."
