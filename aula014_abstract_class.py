from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = nome
        self.nome = nome

    @property
    @abstractmethod
    def nome(self): ...

    @nome.setter
    def nome(self, nome): ...


class Foo(AbstractFoo):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


l = LogPrintMixin()
l.log_success("Oi")

foo = Foo("Ola")
print(foo.nome)
