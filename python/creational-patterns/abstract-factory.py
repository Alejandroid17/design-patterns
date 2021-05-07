# abstract-factory.py

from __future__ import annotations

from abc import ABC, abstractmethod


class GUIFactory(ABC):
    """Abstract Factory interface declares a set of methods that return different abstract products."""

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowFactory(GUIFactory):
    """Concrete Factories produce a family of products that belong to a single variant (Window variant)."""

    def create_button(self) -> Button:
        return WindowButton()

    def create_checkbox(self) -> Checkbox:
        return WindowCheckbox()


class MacFactory(GUIFactory):
    """Concrete Factories produce a family of products that belong to a single variant (Mac variant)."""

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()




class AbstractButton(ABC):
    """Each distinct product of a product family should have a base interface (Button)."""

    @abstractmethod
    def on_click(self) -> str:
        pass


class WindowButton(AbstractButton):
    """Window button variant"""

    def on_click(self) -> str:
        return "On click Window button."


class MacButton(AbstractButton):
    """Mac button variant"""

    def on_click(self) -> str:
        return "On click Mac button."




class AbstractCheckbox(ABC):
    """Each distinct product of a product family should have a base interface (Checkbox)."""

    @abstractmethod
    def on_click(self) -> None:
        pass

    @abstractmethod
    def on_paint(self, collaborator: AbstractButton) -> None:
        pass


class WindowCheckbox(AbstractCheckbox):
    """Window checkbox variant"""

    def on_click(self) -> str:
        return "On click Window checkbox."

    def on_paint(self, collaborator: AbstractButton) -> str:
        result = collaborator.on_click()
        return f"The result of the Window Checkbox collaborating with the ({result})"


class MacCheckbox(AbstractCheckbox):
    """Mac checkbox varian"""

    def on_click(self) -> str:
        return "On click Max checkbox."

    def on_paint(self, collaborator: AbstractButton) -> str:
        result = collaborator.on_click()
        return f"The result of the Mac Checkbox collaborating with the ({result})"




def client_code(factory: GUIFactory) -> None:

    button = factory.create_button()
    checkbox = factory.create_checkbox()

    result = button.on_click()
    print(result)
    
    result = checkbox.on_click()
    print(result)

    result = checkbox.on_paint(button)
    print(result)


if __name__ == "__main__":

    print("Client: Testing client code with the first factory type (Window):")
    client_code(WindowFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type (MAC):")
    client_code(MacFactory())
    
    print("\n")

    """
    Result:

        Client: Testing client code with the first factory type (Window):
        On click Window button.
        On click Window checkbox.
        The result of the Window Checkbox collaborating with the (On click Window button.)


        Client: Testing the same client code with the second factory type (MAC):
        On click Mac button.
        On click Max checkbox.
        The result of the Mac Checkbox collaborating with the (On click Mac button.)
        
    """
