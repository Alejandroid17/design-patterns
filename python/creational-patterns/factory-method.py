# Factory method

from __future__ import annotations

from abc import ABC, abstractmethod


class DocumentFormat(ABC):
    """The DocumentFormat class declares the factory method that is supposed to return an object of a Document class."""

    @abstractmethod
    def factory_method(self):
        """DocumentFormat may also provide some default implementation of the factory method."""
        pass

    def get_pages(self) -> str:
        """Core business logic that relies on Document objects, returned by the factory method."""
        print("Start business logic")
        document = self.factory_method()
        print("Do something")
        return document.get_pages()



class WordFormat(DocumentFormat):

    def factory_method(self) -> Document:
        return Word()

class ExcelFormat(DocumentFormat):

    def factory_method(self):
        return Excel()

class PDFFormat(DocumentFormat):

    def factory_method(self) -> Document:
        return PDF()



class Document(ABC):
    """Document interface that declares the operations that all concrete documents must implement."""

    @abstractmethod
    def get_pages(self) -> str:
        pass

class Word(Document):

    def get_pages(self) -> str:
        return "Word document: 2"

class PDF(Document):

    def get_pages(self) -> str:
        return "PDF document: 5"

class Excel(Document):

    def get_pages(self) -> str:
        return "Excel document: 7"


if __name__ == "__main__":
    print("--- PDF ---")
    result = PDFFormat().get_pages()
    print(result)
    print("\n")

    print("--- Excel ---")
    result = ExcelFormat().get_pages()
    print(result)
    print("\n")

    print("--- WORD ---")
    result = WordFormat().get_pages()
    print(result)

    """
    Result:

        --- PDF ---
        Start business logic
        Do something
        PDF document: 5


        --- Excel ---
        Start business logic
        Do something
        Excel document: 7


        --- WORD ---
        Start business logic
        Do something
        Word document: 2
        
    """
