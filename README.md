### CS--1205-LAB-3 
## 📝 Document Management System 📝
👋 Welcome to Our Project !

Welcome to our project, where we code an amazing document-handling system with clean and functional Python code! 
This project is created with the goal of **learning**, **growing**, and **building something meaningful** as part of our journey as aspiring developers.

---

## 👥 Meet Our Team Members
- Andrea
- Eume
- Coleen
- Venice

---

## 📄 Short Description of the System
This Document Management System simulates how digital files are created, managed, and tracked using Python. It supports four file types (.doc, .pdf, .txt, and .xls) each represented by a subclass that inherits from an abstract base class. The system allows users to create documents with author details, add text, and simulate saving and printing actions. It also records metadata such as creation time, paper size, and text count. 

Features:
- 🧠 Inherits from an abstract base class `Document`
- 🧾 Supports margin and metadata for different file types
- ⌛ Tracks creation time and text content
- 💾 Can be saved and printed (simulated)
- 📄 Types supported: `.pdf`, `.doc`, `.txt`, `.xls`

---

## ▶️ How to Run the Program
1. Ensure Python is installed (version 3.x).
2. Place all source code files in the same folder, with the main file named main.py.
3. Open a terminal or code editor.
4. Run the program using:

   python main.py

## ⚙️ How the Program Works
This system simulates a document manager using object-oriented programming.
Structure and Flow:
- Document (abstract class):
  - Base class with attributes: name, paper_size, author, margin, etc.
  - Contains abstract methods: create_new(), save(), print_document()
  - Provides add_text_count() to simulate typing, and document_status() to display details.

* DocumentType (inherits Document):
  - Implements save() and print_document() for all document types.

* Subclasses of DocumentType:
  - Doc, Pdf, Txt, Xls
  - Each defines create_new() with its respective file format (e.g., .doc, .pdf, etc.)

* Txt and Xls:
  - Override the constructor to remove the margin argument (since it's not used in those file types).

Program Execution (in main function):
- Creates document objects with various details.
- For each document:
  - Calls create_new() to simulate creation.
  - Adds 5 letters using add_text_count().
  - Saves and prints the document.
  - Displays full details using document_status().

---
## 🔍 What to Expect in This Project
In this project, you can expect:
- 🧠 Understand and apply abstract base classes using Python’s abc module
- 🧾 Learn inheritance and constructor chaining with file types like .doc, .pdf, .txt, and .xls
- 📊 Simulate real-world document systems including saving, printing, margin handling, and text counting
- 🕓 Use the datetime module to track creation timestamps for each document

> Whether you're just starting or reviewing your basics, this project is designed to help you become more confident in coding! 🤗

---
## 🙏 Acknowledgement
We give our utmost gratitude to our instructor for helping us understand the basics of object-oriented programming, this project wouldn’t have come together without that guidance. We’re also really grateful to each team member for putting in the effort, staying involved, and working well together. This project would not have been possible without everyone's teamwork.

---
## 💡 Final Reminders
> We believe in 🤗 collaboration and constant improvement. If you have feedback, ideas, or want to contribute, you're more than welcome💖!

> I hope you find this project useful, inspiring, and easy to explore!
