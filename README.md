.・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜✭・..・。.・゜

<div align="center">

<h3> CS--1205-LAB-3 </h3>
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

### UML DIAGRAM 📈
![image](https://github.com/user-attachments/assets/5e565aca-204a-48a0-a86c-774c03b7e6c7)

──────────────────────────────────────────୨ৎ────────────────────────────────────────────

### CODE SAMPLES 😃

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

## 🌟 A Heartfelt Acknowledgment 🌟

We extend our utmost gratitude to our amazing instructor, Ms. Fatima Marie Agdon, MSCS, for guiding us through the basics of object-oriented programming! 🙌✨ This project wouldn’t have come together without that invaluable support and shared wisdom.

A huge shoutout to each of our fantastic team members! 💪💖 Your dedication, involvement, and teamwork have made this project more fun. Together, we have overcome challenges and celebrated victories! 🎉🌈
Until Next Time Again! 😘

𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ ⋆ 𓂃 ₊ ⊹𐔌 ﹒ ⋆ ꩜ 
