from dataclasses import dataclass


class UseDataclass(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        return dataclass(clsobj, init=False)  # type: ignore

    def __call__(cls, *args, **kwargs):
        for key, value in kwargs.items():
            if value is None:
                kwargs[key] = {}

        if not kwargs:
            return None

        instance = super().__call__(*args, **kwargs)

        return instance


class Resource(metaclass=UseDataclass):
    pass
