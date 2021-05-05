# Template method

from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    """The Abstract Class defines a template method that contains a skeleton of some algorithm."""

    def get_pages(self) -> int:
        """Skeleton of an algorithm."""
        self.open_document()
        self.read_document()
        self.hook1()
        num_pages = self.count_pages()
        num_pages = self.hook2(num_pages)

        return num_pages

    # These operations already have implementations.

    def open_document(self) -> None:
        print("The document is open")

    def read_document(self) -> None:
        print("The document is read")

    # These operations have to be implemented in subclasses.

    @abstractmethod
    def count_pages(self) -> int:
        pass

    # Additional extension points

    def hook1(self) -> None:
        pass

    def hook2(self, result) -> int:
        return result


class Word(AbstractDocument):

    def count_pages(self) -> int:
        return 10

    def hook2(self, num_pages) -> int:
        print("Custom hook2 add a page")
        return num_pages + 1

class PDF(AbstractDocument):

    def count_pages(self) -> int:
        return 5


if __name__ == '__main__':
    print("--- WORD ---")
    result = Word().get_pages()
    print(result)
    print("\n")

    print("--- PDF ---")
    result = PDF().get_pages()
    print(result)
    print("\n")

    """
    Result:

        --- WORD ---
        The document is open
        The document is read
        Custom hook2 add a page
        11


        --- PDF ---
        The document is open
        The document is read
        5

    """
