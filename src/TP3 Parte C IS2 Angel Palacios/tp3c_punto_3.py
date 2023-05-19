from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):

    _id: str = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)


    def notify(self) -> None:

        #print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, id: str) -> None:

        #print("\nSubject: I'm doing something important.")
        print("\n")
        self._id = id

        print(f"Subject: Mi id fue cambiado a: {self._id}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass




class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        id= 'ab10'
        #print('ConcreteObserverA id:',id)
        if subject._id == id:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        id= 'ab14'
        #print('ConcreteObserverB id:',id)
        if subject._id == id:
            print("ConcreteObserverB: Reacted to the event")

class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        id= 'ab16'
        #print('ConcreteObserverB id:',id)
        if subject._id == id:
            print("ConcreteObserverC: Reacted to the event")

class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        id= 'ab17'
        #print('ConcreteObserverB id:',id)
        if subject._id == id:
            print("ConcreteObserverD: Reacted to the event")


if __name__ == "__main__":
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    observer_c = ConcreteObserverC()
    subject.attach(observer_c)

    observer_d = ConcreteObserverD()
    subject.attach(observer_d)

    subject.some_business_logic('ab10')
    subject.some_business_logic('ab11')
    subject.some_business_logic('ab12')
    subject.some_business_logic('ab13')
    subject.some_business_logic('ab14')
    subject.some_business_logic('ab15')
    subject.some_business_logic('ab16')
    subject.some_business_logic('ab17')

    #subject.detach(observer_a)
    
    #subject.some_business_logic('ab123')
