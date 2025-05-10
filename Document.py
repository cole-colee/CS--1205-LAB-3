from abc import ABC, abstractmethod
from datetime import datetime

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

    @abstractmethod
    def create_new(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def print_document(self):
        pass

    def document_status(self):
        return (f"Document: {self._name}\n"
                f"Author: {self._author}\n"
                f"Paper Size: {self._paper_size}\n"
                f"Margin: {self._margin if self._margin else 'N/A'} mm\n"
                f"Text Count: {self._text_count} letters\n"
                f"Date Created: {self._date_created}\n"
                f"Printed: {'Yes' if self._printed else 'No'}")


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


class Pdf(Document):
    def __init__(self, name, paper_size, author, margin=None):
        super().__init__(name, paper_size, author, margin, initial_text_count=44)

    def create_new(self):
        print(f"{self._author} created \"{self._name}\" (.pdf).")

    def save(self):
        self._saved = True
        print(f"{self._author} saved \"{self._name} document.\"")

    def print_document(self):
        self._printed = True
        print(f"{self._author} printed \"{self._name} document.\"")


class Txt(Document):
    def __init__(self, name, paper_size, author):
        super().__init__(name, paper_size, author, None, initial_text_count=36)

    def create_new(self):
        print(f"{self._author} created \"{self._name}\" (.txt).")

    def save(self):
        self._saved = True
        print(f"{self._author} saved \"{self._name} document.\"")

    def print_document(self):
        self._printed = True
        print(f"{self._author} printed \"{self._name} document.\"")


class Xls(Document):
    def __init__(self, name, paper_size, author):
        super().__init__(name, paper_size, author, None, initial_text_count=317)

    def create_new(self):
        print(f"{self._author} created \"{self._name}\" (.xls).")

    def save(self):
        self._saved = True
        print(f"{self._author} saved \"{self._name} document.\"")

    def print_document(self):
        self._printed = True
        print(f"{self._author} printed \"{self._name} document.\"")


def main():
    documents = [
        Doc('RPH Final Project', 'A4', 'Andrea'),
        Pdf('ART APPRECIATION Activity', 'A4', 'Venice'),
        Txt('Lecture Summary - Math 407', 'A5', 'Eume'),
        Xls('Student Grades In PE', 'Letter', 'Coleen')
    ]

    for doc in documents:
        print()
        doc.create_new() 
        print()
        doc.add_text_count()
        doc.save()
        doc.print_document()
        print()
        print(doc.document_status(), "\n")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

if __name__ == "__main__":
    main()
