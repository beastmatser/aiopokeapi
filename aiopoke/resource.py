from dataclasses import dataclass


class UseDataclass(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        return dataclass(clsobj, init=False)  # type: ignore


class Resource(metaclass=UseDataclass):
    pass
