# File Management System

A desktop file management application built with Python and Tkinter to demonstrate operating-system file handling concepts.

## Overview

This project implements a graphical file management system that allows users to interact with files and directories through a desktop GUI.

The application was developed as an individual operating systems project and focuses on practical file-system operations, file handling, and interaction with the operating system through Python.

## Features

- Create files and directories
- Open and edit files
- Save file changes
- Delete files and directories
- Rename files and directories
- Navigate through folders
- Error handling for file operations

## Operating System Concepts

The project demonstrates several operating-system file handling concepts, including:

- File creation, reading, writing, and closing
- File and directory operations
- File descriptors and resource management
- File metadata
- Interaction with operating-system file APIs

Python's `with open()` pattern is used for file handling to support proper allocation and release of file resources.

## Architecture

The application is organized into three primary layers:

1. **GUI Layer** — Tkinter interface used for user interaction
2. **File Operations Layer** — Application logic responsible for file and directory operations
3. **Operating System APIs** — Interfaces used to interact with the underlying operating system

## Technologies

- Python
- Tkinter
- Operating System File APIs

## Requirements

- Python 3.x
- Tkinter

## Running the Application

Clone the repository and navigate to the project directory:

```bash
cd FileManagerProject
