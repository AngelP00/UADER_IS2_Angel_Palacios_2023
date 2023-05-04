#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class Ping(Subject):
    
    def execute(self, string) -> None:
        #print(string[0:4])
        if(string[0:4]!='192.'):
            for i in range(1, 11):
                print(i)
                print('intentando conectarse a:', string)
        else:
            print('ip no valida.')
    
    def executefree(self, string) -> None:
        for i in range(1, 11):
            #print(i)
            print(f"{i}: intentando conectarse a:", string)

class PingProxy(Subject):
    def __init__(self, _real_ping: Ping) -> None:
        self._real_ping = _real_ping
    
    def execute(self, string) -> None:
        print(f"intentando conectarse a'{string}':")
        if(string=='192.168.0.254'):
            self._real_ping.executefree('www.google.com')
        else:
            self._real_ping.execute(string)

def client_code(subject: Subject) -> None:

    # ...

    #subject.request()
    subject.execute('192.423.231')
    subject.execute('192.168.0.254')

    # ...

if __name__ == "__main__":
    real_ping = Ping()
    pingProxy = PingProxy(real_ping)

    client_code(pingProxy)