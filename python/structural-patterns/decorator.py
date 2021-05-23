# decorator.py

from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractNotifier():
    """Interface that defines operations that can be altered by decorators."""

    def send(self) -> str:
        pass



class TextNotifier(AbstractNotifier):
    """TextNotifier is a concrete component that provides default implementations."""

    def send(self) -> str:
        return "Text notifier"



class NotifierDecorator(AbstractNotifier):
    """NotifierDecorator is a BaseDecorator. This class defines the wrapping interface 
    for all concrete decorators. 
    
    The default implementation of the wrapping code might include a field for storing 
    a wrapped component and the means to initialize it.

    """

    _notifier: AbstractNotifier = None

    def __init__(self, notifier: AbstractNotifier) -> None:
        self._notifier = notifier

    @property
    def notifier(self) -> str:
        """The decorator delegates all work to the wrapped component."""
        return self._notifier

    def send(self) -> str:
        return self._notifier.send()


# Concrete Decorators call the wrapped object and alter its result in some way.

class SMSDecorator(NotifierDecorator):
    
    def send(self) -> str:
        """Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.

        """
        return f"SMSDecorator({self.notifier.send()})"

class FacebookDecorator(NotifierDecorator):

    def send(self) -> str:
        return f"FacebookDecorator({self.notifier.send()})"

class SlackDecorator(NotifierDecorator):

    def send(self) -> str:
        return f"SlackDecorator({self.notifier.send()})"



def client_code(component: AbstractNotifier) -> None:
    """The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works with.
    """
    
    print(f"RESULT: {component.send()}", end="")



if __name__ == "__main__":

    simple_notifier = TextNotifier()
    print("Client: Simple notifier:")

    client_code(simple_notifier)
    print("\n")

    sms_decorator = SMSDecorator(simple_notifier)
    facebook_decorator = FacebookDecorator(sms_decorator)
    print("Client: Now I've got a decorated component:")
    client_code(facebook_decorator)
    print("\n")


    """
    Result:

        Client: Simple notifier:
        RESULT: Text notifier

        Client: Now I've got a decorated component:
        RESULT: FacebookDecorator(SMSDecorator(Text notifier))
        
    """
