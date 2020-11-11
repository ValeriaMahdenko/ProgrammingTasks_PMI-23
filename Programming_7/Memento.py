from __future__ import annotations
from abc import ABC, abstractmethod
from Composition import *

class Memento(ABC):

    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


class Originator:

    def __init__(self):
        self.note = Composition()

    def setNote(self, note):
        self.note = note

    def getNote(self):
        return self.note

    def save(self):
        return Memento(self.note.copy())

    def restore(self, memObj):
        self.note = memObj.getState()

    def write_txt(self):
        try:
            f = open("Information", "w")
            f.writelines(str(i) + "\n" for i in self.note)
            f.close()
        except FileNotFoundError:
            raise ("File not exit")


class CareTaker:

    def __init__(self):
        self.history = []
        self.currState = -1
        self._max_size = 6

    def addMemento(self, memObj):
        if len(self.history) >= self._max_size:
            self.history.pop(0)
            self.history.append(memObj)
            self.currState = len(self.history) - 1
        else:
            self.history.append(memObj)
            self.currState = len(self.history) - 1

    def getMemento(self, index):
        return self.history[index]

    def undo(self):
        if self.currState == 0:
            print("It is your first action of the last five")
            return self.getMemento(0)
        else:
            self.currState = self.currState - 1
            return self.getMemento(self.currState)

    def redo(self):
        if self.currState >= len(self.history) - 1:
            self.currState = len(self.history) - 1
            print("It is your last action!")
            return self.getMemento(self.currState)

        else:
            self.currState = self.currState + 1
            return self.getMemento(self.currState)
