.・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜

<div align="center">

<h3> ### CS--1205-LAB-3 </h3>
<h2> 📝 Document Management System 📝 </h2>
<h3> 🎉 Welcome to Our Document Handling Adventure! 🚀 </h3>

</div>

Get ready to dive into an exciting journey where we code an amazing document-handling system using clean and functional Python! 🐍✨

This project is all about learning, growing, and building something meaningful as we embark on our adventure as aspiring developers. 🌱💻 Together, we’ll explore new concepts, tackle challenges, and unleash our creativity to create a system that truly shines!

Let’s make coding fun and impactful! 🎊💪

---

## 👥 Meet Our Team Members 

- ── ⟢ ・⸝⸝ Andrea | [username: wydtmrz] (https://github.com/wydtmrz) 💙🌼
- ── ⟢ ・⸝⸝ Eume   | [username: eumung] (https://github.com/eumung) 💜🌷
- ── ⟢ ・⸝⸝ Coleen | [username: cole-colee] (https://github.com/cole-colee) 🩷🌺
- ── ⟢ ・⸝⸝ Venice | [username: venieeeee] (https://github.com/venieeeee) 💛🌹

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

   ```
   python main.py
   ```

## ⚙️ Check How the Program Works!

# UML DIAGRAM
![class diagram](https://www.messenger.com/messenger_media/?attachment_id=9693614007426266&message_id=mid.%24gACIbP4iYX0ic5omqHWWtURbODvnD&thread_id=9600108896739144)

```python

#Take a peek on the parent class' of our code:

class Document(ABC):
    def __init__(self, name, paper_size, author, margin=None, initial_text_count=0):
        self._name = name
        self._paper_size = paper_size
        self._margin = margin
        self._author = author
        self._text_count = initial_text_count
        self._saved = False
        self._printed = False
        self._date_created = datetime.now()

    def add_text_count(self):
        self._text_count += 5
        print(f"The document \"{self._name}\" created by {self._author} was added 5 letters, total: {self._text_count} letters.")

#These shows the properties and methods under the parent class (Document)...
```

──────────────────────────────────────────୨ৎ────────────────────────────────────────────

```python

#Here's a snippet of our code showing our subclass:

class Doc(Document):
    def __init__(self, name, paper_size, author, margin=None):
        super().__init__(name, paper_size, author, margin, initial_text_count=240)

    def create_new(self):
        print(f"{self._author} created \"{self._name}\" (.doc).")

    def save(self):
        self._saved = True
        print(f"{self._author} saved \"{self._name} document.\"")

    def print_document(self):
        self._printed = True
        print(f"{self._author} printed \"{self._name} document.\"")

#This code shows the inheritance of the subclasses' methods from the superclass

```

──────────────────────────────────────────୨ৎ────────────────────────────────────────────

```bash

#Below is the sample output of our code:

Venice created "ART APPRECIATION Activity" (.pdf).

The document "ART APPRECIATION Activity" created by Venice was added 3 letters, total: 49 letters.
Venice saved "ART APPRECIATION Activity document."
Venice printed "ART APPRECIATION Activity document."

Document: ART APPRECIATION Activity
Author: Venice
Paper Size: A4
Margin: N/A mm
Text Count: 49 letters
Date Created: 2025-05-09 13:09:03.149780
Printed: Yes 

-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

```

──────────────────────────────────────────୨ৎ────────────────────────────────────────────

## 🙏 Acknowledgement
We give our utmost gratitude to our instructor for helping us understand the basics of object-oriented programming, this project wouldn’t have come together without that guidance. We’re also really grateful to each team member for putting in the effort, staying involved, and working well together. This project would not have been possible without everyone's teamwork.

𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ 
