# Chain of resposibility

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class AutomationHandler(ABC):
    """The Handler interface declares a method for building the chain of handlers. It also declares a method for executing a request."""

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractAutomationHandler(AutomationHandler):
    """The default chaining behavior can be implemented inside a base handler class."""

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None



"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""

class AutomationA(AbstractAutomationHandler):

    def handle(self, request: Any) -> str:
        if request == "A":
            return f"AutomationA: {request}"
        else:
            return super().handle(request)


class AutomationB(AbstractAutomationHandler):
    
    def handle(self, request: Any) -> str:
        if request == "B":
            return f"AutomationB: {request}"
        else:
            return super().handle(request)


class AutomationC(AbstractAutomationHandler):
    
    def handle(self, request: Any) -> str:
        if request == "C":
            return f"AutomationC {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for automation in ['A', 'D', 'B', 'C']:
        print(f"\nClient: Start automation {automation}?")
        result = handler.handle(automation)
        if result:
            print(f"\t{result}", end="")
        else:
            print(f"\t Automation {automation} has not been initiated.", end="")


if __name__ == "__main__":
    automation_a = AutomationA()
    automation_b = AutomationB()
    automation_c = AutomationC()

    automation_a.set_next(automation_b).set_next(automation_c)

    print("Chain: Automation A > Automation B > Automation C")
    client_code(automation_a)
    print("\n")

    print("Subchain: Automation B > Automation C")
    client_code(automation_b)
    print("\n")
    
    """
    Result:

        Chain: Automation A > Automation B > Automation C

        Client: Start automation A?
                AutomationA: A
        Client: Start automation D?
                Automation D has not been initiated.
        Client: Start automation B?
                AutomationB: B
        Client: Start automation C?
                AutomationC C

        Subchain: Automation B > Automation C

        Client: Start automation A?
                Automation A has not been initiated.
        Client: Start automation D?
                Automation D has not been initiated.
        Client: Start automation B?
                AutomationB: B
        Client: Start automation C?
                AutomationC C

    """


