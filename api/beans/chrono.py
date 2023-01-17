class Chrono:
    _name: str
    _number: int

    def __init__(self, name: str, number: int) -> None:
        self._name = name
        self._number = number

    @property
    def name(self) -> str:
        return self._name

    @property
    def number(self) -> int:
        return self._number
