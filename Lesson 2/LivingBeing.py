from abc import ABC
from functools import total_ordering
from typing import Self
from datetime import date

from .enums.Gender import Gender

@total_ordering
class LivingBeing(ABC):

    def __init__(self, name: str, birthDate: date, gender: Gender) -> None:
        self._name = name
        self._set_birthDate(birthDate)
        self._gender = gender

    @property
    def Name(self):
        return self._name
    
    @property
    def Age(self):
        today = date.today()
        age = today.year - self._birthDate.year
        if today.month < self._birthDate.month or (today.month == self._birthDate.month and today.day < self._birthDate.day):
            age -= 1
        return age
    
    def _set_birthDate(self, birthDate: date):
        if date.today() >= birthDate:
            self._birthDate = birthDate
        else:
            raise ValueError(f"Date {birthDate} is after today")
    
    @property
    def BirthDate(self):
        return self._birthDate
    
    @property
    def Gender(self) -> str:
        return str(self._gender)
    
    def __eq__(self, other: Self):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return ((self._name.lower(), self._birthDate, self._gender) ==
                (other._name.lower(), other._birthDate, other._gender))
    
    def __lt__(self, other: Self):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return ((self._name.lower(), self._birthDate, self._gender) <
                (other._name.lower(), other._birthDate, other._gender))
    
    def __str__(self) -> str:
        return f"{self.Gender} called {self.Name} of age {self.Age}"
    
    def rename(self, new_name: str):
        if new_name:
            self._name = new_name.strip()